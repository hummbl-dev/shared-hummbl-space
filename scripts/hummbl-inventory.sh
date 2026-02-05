#!/bin/bash
set -euo pipefail

STATE_DIR="$(cd "$(dirname "$0")/.." && pwd)/_state"
mkdir -p "$STATE_DIR"

if [ -z "${HUMMBL_REMOTE:-}" ]; then
  echo "HUMMBL_REMOTE not set. Aborting to avoid unexpected sync." >&2
  exit 1
fi

cat <<LOG
[TBD] Inventory would run against $HUMMBL_REMOTE and log to $STATE_DIR/hummbl-inventory.log
LOG
