#!/bin/bash
set -euo pipefail

STATE_DIR="$(cd "$(dirname "$0")/.." && pwd)/_state"
mkdir -p "$STATE_DIR"

if [ -z "${HUMMBL_SYNC_TARGET:-}" ]; then
  echo "HUMMBL_SYNC_TARGET not set. Aborting sync." >&2
  exit 1
fi

echo "[TBD] Would sync shared workspace to $HUMMBL_SYNC_TARGET (dry run)."
