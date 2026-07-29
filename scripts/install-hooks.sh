#!/bin/bash
# Point git at the tracked hooks in scripts/hooks/.
# Run once per clone: ./scripts/install-hooks.sh
set -euo pipefail

GIT_ROOT=$(git rev-parse --show-toplevel)

chmod +x "$GIT_ROOT/scripts/hooks/"*
git -C "$GIT_ROOT" config core.hooksPath scripts/hooks

echo "Hooks installed: core.hooksPath -> scripts/hooks"
