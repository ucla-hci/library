#!/usr/bin/env python3
"""Assign coding-schema front matter to uncoded notes using headless Claude.

Uncoded notes are those without YAML front matter. A note in `inbox/` is moved
into `papers/` once it is coded; a note already in `papers/` is coded in place.

The controlled vocabulary is read from `rebuild_indexes.py` so the prompt and
the validator can never disagree.

Usage:
    code_paper.py                 # code every uncoded note in inbox/ and papers/
    code_paper.py PATH [PATH ...] # consider only these notes
    code_paper.py --dry-run       # print the codes without writing anything
"""

import argparse
import importlib.util
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAPERS = ROOT / "papers"
INBOX = ROOT / "inbox"

# A note this long is truncated before being sent; the head carries the title,
# abstract and key points, which is what the codes are drawn from.
MAX_NOTE_CHARS = 24000
CLAUDE_TIMEOUT = 300


def load_schema():
    """Import rebuild_indexes.py as the single source of truth for the vocabulary."""
    # Importing by path would otherwise leave a __pycache__/ beside the notes.
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location("rebuild_indexes", ROOT / "rebuild_indexes.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def is_coded(path):
    """A coded note begins with a YAML front matter fence."""
    with open(path, encoding="utf-8") as handle:
        return handle.readline().rstrip("\n") == "---"


def find_uncoded(candidates=None):
    """Return uncoded notes, restricted to `candidates` when given."""
    if candidates is None:
        notes = sorted(INBOX.glob("*.md")) + sorted(PAPERS.glob("*.md"))
    else:
        notes = [Path(c).resolve() for c in candidates]
    return [
        note
        for note in notes
        if note.suffix == ".md"
        and note.exists()
        and note.name != "README.md"
        and note.parent in (PAPERS, INBOX)
        and not is_coded(note)
    ]


def build_prompt(schema, note_text):
    """Describe the vocabulary and coding rule, and ask for front matter only."""
    def vocabulary(field):
        return "\n".join(
            f"  {code}: {meaning}" for code, meaning in schema.DEFINITIONS[field].items()
        )

    return f"""You are coding a literature note for a research library on computational scientific discovery.

Assign metadata from this controlled vocabulary. Use ONLY these codes, spelled exactly as shown.

activities (choose all that apply, at least one):
{vocabulary("activities")}

contributions (choose all that apply, at least one):
{vocabulary("contributions")}

domains (choose all that apply, at least one):
{vocabulary("domains")}

scope (choose exactly one):
{vocabulary("scope")}

Coding rule: assign a code only when the topic is a SUBSTANTIVE OBJECT of the paper,
not merely mentioned in passing. Be selective — most papers take three to six
activities and two to four contributions. Use `general` for a cross-domain account
rather than guessing a specific field the note does not establish.

Scope guidance: `end-to-end` is reserved for a near-complete iterative discovery
pipeline spanning most of the research loop. A system that connects several
activities but omits whole phases such as problem formulation or literature
discovery is `multi-activity`.

Here is the note:

<note>
{note_text}
</note>

Respond with ONLY a YAML front matter block, starting and ending with `---`, in exactly
this shape and field order, and nothing else — no explanation, no code fence:

---
activities:
  - <code>
contributions:
  - <code>
domains:
  - <code>
scope: <code>
coding_status: coded
---"""


def call_claude(prompt):
    """Run headless Claude and return its stdout."""
    try:
        result = subprocess.run(
            ["claude", "-p"],
            input=prompt,
            capture_output=True,
            text=True,
            timeout=CLAUDE_TIMEOUT,
        )
    except FileNotFoundError:
        raise RuntimeError("the `claude` CLI is not on PATH")
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"claude did not respond within {CLAUDE_TIMEOUT}s")
    if result.returncode != 0:
        detail = (result.stderr or result.stdout or "").strip().splitlines()
        raise RuntimeError(f"claude exited {result.returncode}: {detail[-1] if detail else 'no output'}")
    return result.stdout


def extract_front_matter(response):
    """Pull the YAML block out of a model response, tolerating a code fence."""
    text = response.strip()
    fence = re.search(r"```(?:yaml)?\s*\n(.*?)```", text, re.DOTALL)
    if fence:
        text = fence.group(1).strip()
    match = re.search(r"^---\s*\n(.*?)\n---\s*$", text, re.DOTALL | re.MULTILINE)
    if not match:
        raise RuntimeError("no YAML front matter found in the response")
    return f"---\n{match.group(1).strip()}\n---\n"


def validate(schema, front_matter, note_text, note_name):
    """Parse the proposed front matter with the real validator before writing it."""
    probe = ROOT / f".code_paper_probe_{os.getpid()}.md"
    probe.write_text(front_matter + "\n" + note_text, encoding="utf-8")
    try:
        parsed = schema.parse_paper(probe)
    except ValueError as error:
        raise RuntimeError(str(error).replace(str(probe), note_name))
    finally:
        probe.unlink(missing_ok=True)
    return parsed


def summarize(parsed):
    return (
        f"activities: {', '.join(parsed['activities'])}\n"
        f"    contributions: {', '.join(parsed['contributions'])}\n"
        f"    domains: {', '.join(parsed['domains'])}\n"
        f"    scope: {parsed['scope']}"
    )


def code_note(schema, note, dry_run=False):
    """Code one note; return the destination path it now lives at."""
    note_text = note.read_text(encoding="utf-8")
    prompt_text = note_text[:MAX_NOTE_CHARS]
    front_matter = extract_front_matter(call_claude(build_prompt(schema, prompt_text)))

    # The note needs a level-one title for the indexes; validate the real body.
    parsed = validate(schema, front_matter, note_text, note.name)
    print(f"  {note.name}\n    {summarize(parsed)}")
    if dry_run:
        return note

    note.write_text(front_matter + "\n" + note_text, encoding="utf-8")
    if note.parent == INBOX:
        destination = PAPERS / note.name
        if destination.exists():
            raise RuntimeError(f"{destination.name} already exists in papers/")
        shutil.move(str(note), str(destination))
        print(f"    moved to papers/{destination.name}")
        return destination
    return note


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("paths", nargs="*", help="notes to consider (default: all uncoded)")
    parser.add_argument("--dry-run", action="store_true", help="print codes without writing")
    args = parser.parse_args()

    schema = load_schema()
    uncoded = find_uncoded(args.paths or None)
    if not uncoded:
        return 0

    print(f"coding {len(uncoded)} uncoded note(s) with claude...")
    failures = []
    for note in uncoded:
        try:
            code_note(schema, note, dry_run=args.dry_run)
        except RuntimeError as error:
            failures.append(f"{note.name}: {error}")
            print(f"  {note.name}\n    FAILED: {error}", file=sys.stderr)

    if failures:
        print(f"\n{len(failures)} note(s) left uncoded; code them by hand.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
