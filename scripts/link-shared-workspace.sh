#!/bin/bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="${1:-$PWD}"

items=(
  agents
  avatars
  scripts
  memory
  AGENT_BIRTH_PROCESS.md
  AGENT_BIRTH_LOG_TEMPLATE.md
  AGENT.md
  IDENTITY.md
  USER.md
  SOUL.md
)

mkdir -p "$TARGET"
for item in "${items[@]}"; do
  src="$ROOT/$item"
  dest="$TARGET/$item"
  if [ -e "$dest" ]; then
    echo "Skipping $dest (already exists)"
    continue
  fi
  ln -s "$src" "$dest"
  echo "Linked $dest -> $src"
 done
