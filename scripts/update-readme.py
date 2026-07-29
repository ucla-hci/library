#!/usr/bin/env python3
"""
Regenerate README.md as an index of every note in the library.

Notes are grouped by folder: top-level folders become ## sections, nested
folders become ### (and deeper) subsections. Each note is listed by its first
`# ` heading, falling back to the filename.

Everything below the header is generated, so edit `_readme-header.md` rather
than the top of README.md — changes made to README.md directly are overwritten.
"""

import re
import sys
from pathlib import Path
from urllib.parse import quote

# Hand-edited preamble placed at the top of the generated README.
HEADER_FILE = "_readme-header.md"
DEFAULT_HEADER = "# Library\nNotes of what we read"

# Folders at the repo root that hold no notes.
SKIP_DIRS = {"scripts"}

# Notion exports suffix every page with a 32-char hex id.
NOTION_ID = re.compile(r"\s+[0-9a-f]{32}$")

# Words with a fixed capitalization, used when prettifying a slug folder name.
ACRONYMS = {
    "ai": "AI",
    "cs": "CS",
    "genui": "GenUI",
    "hci": "HCI",
    "llm": "LLM",
    "nlp": "NLP",
    "ui": "UI",
    "ux": "UX",
    "xr": "XR",
}


def strip_notion_id(name):
    """Drop the trailing Notion page id from a file or folder name."""
    return NOTION_ID.sub("", name)


def get_title(filepath):
    """Extract the first `# ` heading from a markdown file, ignoring code fences."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            in_fence = False
            for line in f:
                line = line.strip()
                if line.startswith("```") or line.startswith("~~~"):
                    in_fence = not in_fence
                    continue
                if in_fence:
                    continue
                if line.startswith("# "):
                    title = " ".join(line[2:].split()).rstrip("#").strip()
                    if title:
                        return title
    except OSError:
        pass
    # Fallback to the filename.
    return strip_notion_id(filepath.stem).replace("_", " ").strip()


def section_title(dirname):
    """Human-readable heading for a folder name."""
    # Folders named by hand (e.g. "HCI Foundations") already read correctly;
    # only prettify lowercase slugs such as "hypothesis-generation".
    if dirname != dirname.lower():
        return dirname
    words = re.split(r"[-_\s]+", dirname)
    return " ".join(ACRONYMS.get(w, w.capitalize()) for w in words if w)


def link(title, filepath, repo_root):
    """Render a markdown list item, escaping both the label and the URL."""
    label = title.replace("\\", "\\\\").replace("[", r"\[").replace("]", r"\]")
    rel_path = filepath.relative_to(repo_root).as_posix()
    return f"- [{label}]({quote(rel_path, safe='/')})"


def collect(dirpath, repo_root, depth):
    """Build the markdown blocks for one folder. Returns [] if it holds no notes."""
    entries = []
    subdirs = []

    for item in sorted(dirpath.iterdir()):
        if item.name.startswith("."):
            continue
        if item.is_dir():
            if item.name.startswith("_"):
                continue
            subdirs.append(item)
        elif item.suffix == ".md":
            entries.append((get_title(item), item))

    # Notion stores a page's attachments in a sibling folder named after the
    # page; those folders hold assets, not notes of their own.
    note_names = {strip_notion_id(f.stem) for _, f in entries}
    subdirs = [d for d in subdirs if strip_notion_id(d.name) not in note_names]

    blocks = []
    if entries:
        entries.sort(key=lambda e: (e[0].casefold(), e[1].name))
        blocks.append([link(title, path, repo_root) for title, path in entries])

    for subdir in sorted(subdirs, key=lambda d: section_title(d.name).casefold()):
        sub_blocks = collect(subdir, repo_root, depth + 1)
        if not sub_blocks:  # Skip folders with no notes anywhere beneath them.
            continue
        heading = "#" * min(depth + 1, 6)
        blocks.append([f"{heading} {section_title(subdir.name)}"])
        blocks.extend(sub_blocks)

    return blocks


def read_header(repo_root):
    """Load the hand-edited preamble, falling back to a built-in default."""
    header_path = repo_root / HEADER_FILE
    if header_path.exists():
        header = header_path.read_text(encoding="utf-8").strip()
        if header:
            return header
    return DEFAULT_HEADER


def generate_readme(repo_root):
    repo_root = Path(repo_root)
    blocks = [[read_header(repo_root)]]
    count = 0

    for item in sorted(repo_root.iterdir(), key=lambda p: p.name.casefold()):
        if not item.is_dir() or item.name.startswith((".", "_")):
            continue
        if item.name in SKIP_DIRS:
            continue

        section = collect(item, repo_root, depth=2)
        if not section:
            continue
        blocks.append([f"## {section_title(item.name)}"])
        blocks.extend(section)
        count += sum(len(b) for b in section if b and b[0].startswith("- "))

    # One blank line between every block guarantees headings are never glued
    # to the list above them.
    content = "\n\n".join("\n".join(block) for block in blocks) + "\n"

    readme_path = repo_root / "README.md"
    previous = readme_path.read_text(encoding="utf-8") if readme_path.exists() else None
    if previous == content:
        print(f"README.md already up to date ({count} notes)")
        return False

    readme_path.write_text(content, encoding="utf-8", newline="\n")
    print(f"Updated {readme_path} ({count} notes)")
    return True


if __name__ == "__main__":
    try:
        generate_readme(Path(__file__).resolve().parent.parent)
    except Exception as exc:  # noqa: BLE001 - surface the reason to the hook
        print(f"update-readme.py: {exc}", file=sys.stderr)
        sys.exit(1)
