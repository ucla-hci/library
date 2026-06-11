#!/usr/bin/env python3
"""
Create a new paper note from _template.md in the root unsorted directory.
"""

import argparse
import re
import sys
import unicodedata
from pathlib import Path


def slugify(value):
    """Return a lowercase, hyphen-separated filename-safe slug."""
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    ascii_value = ascii_value.lower()
    ascii_value = re.sub(r"&", " and ", ascii_value)
    ascii_value = re.sub(r"[^a-z0-9]+", "-", ascii_value)
    return ascii_value.strip("-")


def build_note(template, author, title):
    """Fill the template heading for the requested paper."""
    return template.replace(
        "# Lastname et al.: Title",
        f"# {author} et al.: {title}",
        1,
    )


def create_paper_note(repo_root, author, title):
    template_path = repo_root / "_template.md"
    output_dir = repo_root / "unsorted"

    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")
    if not output_dir.exists():
        raise FileNotFoundError(f"Output directory not found: {output_dir}")

    author_slug = slugify(author)
    title_slug = slugify(title)
    if not author_slug or not title_slug:
        raise ValueError("Author and title must contain at least one letter or number.")

    output_path = output_dir / f"{author_slug}_{title_slug}.md"
    if output_path.exists():
        raise FileExistsError(f"Refusing to overwrite existing file: {output_path}")

    template = template_path.read_text(encoding="utf-8")
    output_path.write_text(build_note(template, author.strip(), title.strip()), encoding="utf-8")
    return output_path


def main():
    parser = argparse.ArgumentParser(
        description="Create a new paper note in unsorted/ from _template.md."
    )
    parser.add_argument("author", help="first author's last name")
    parser.add_argument("title", help="paper title")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent

    try:
        output_path = create_paper_note(repo_root, args.author, args.title)
    except (FileNotFoundError, FileExistsError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    print(output_path.relative_to(repo_root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
