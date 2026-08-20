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

After adding or recoding a paper, run:

```shell
python3 computational-scientific-discovery/rebuild_indexes.py
```

