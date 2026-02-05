#!/bin/bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
GENERATOR="$ROOT_DIR/avatars/generate_compass_avatar.py"

if [[ ! -f "$GENERATOR" ]]; then
  echo "Generator not found at $GENERATOR" >&2
  exit 1
fi

python3 "$GENERATOR" "$@"
