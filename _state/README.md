# _state Directory

Runtime artifacts live here (logs, temporary sync files). This folder is ignored via .gitignore.

Scripts (`scripts/hummbl-inventory.sh`, `scripts/hummbl-sync.sh`) must check for prerequisites (remote hosts, environment variables) before writing to `_state/` to avoid accidental operations.
