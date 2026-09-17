# Computational Scientific Discovery

This collection contains literature notes coded along overlapping dimensions rather than separated into mutually exclusive research phases.

## Browse the collection

- [All papers](indexes/all-papers.md)
- [Research activities](indexes/research-activities.md)
- [Contribution types](indexes/contribution-types.md)
- [Domains](indexes/domains.md)
- [Scope](indexes/scopes.md)
- [Coding schema](coding-schema.md)

## Structure

- `papers/` contains one canonical note for every coded paper.
- `inbox/` is for new notes that have not yet been coded.
- `indexes/` contains generated views over the metadata.
- `coding-schema.md` defines the controlled vocabulary and coding rule.

## Adding a paper

Drop an uncoded note in `inbox/` and commit it. The `post-commit` hook (installed
by `scripts/install-hooks.sh`) reads the note with headless Claude, writes the
front matter, moves the note into `papers/`, and rebuilds the indexes.

Nothing is committed on your behalf — the results are left **unstaged** so you can
check the codes before keeping them:

```shell
git status && git diff          # review
git add -A && git commit -m "Code new papers and rebuild indexes"
```

Assigned codes are a starting point, not a verdict. The model is not consistent
run to run, and it will code any note you give it even when the paper is a poor
fit for this collection, so read them before committing.

To do either step by hand:

```shell
python3 computational-scientific-discovery/code_paper.py --dry-run   # propose codes only
python3 computational-scientific-discovery/rebuild_indexes.py        # validate + rebuild
```

Set `CSD_SKIP_CODING=1` to commit without invoking Claude; the index rebuild still runs.

