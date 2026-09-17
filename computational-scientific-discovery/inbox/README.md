# Inbox

Place new, not-yet-coded literature notes here, then commit. The `post-commit`
hook codes each note against the [coding schema](../coding-schema.md), moves it
into `papers/`, and rebuilds the indexes, leaving the result unstaged for review.

To code a note by hand instead, add the front matter yourself, move it to
`papers/`, and run `python3 rebuild_indexes.py`.
