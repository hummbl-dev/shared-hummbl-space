#!/usr/bin/env bash
set -euo pipefail
# Final Verified Allowlist
ALLOWLIST=(
  "hummbl-agent|/Users/others/workspace/active/hummbl-agent|repo|agentic-kernel|active"
  "hummbl-gpts|/Users/others/workspace/active/hummbl-gpts|repo|gpt-schemas|active"
  "base120|/Users/others/workspace/active/base120-framework|repo|canonical-spec|active"
  "hummbl-production|/Users/others/Documents/GitHub/hummbl-io|repo|web-prod|active"
  "hummbl-monorepo|/Users/others/workspace/active/hummbl-projects/hummbl|repo|monorepo-core|active"
  "hummbl-systems|/Users/others/workspace/active/HUMMBL-Systems|repo|sys-arch|active"
)
DEFAULT_ARTIFACT_PATH="_state/inventory/projects.json"
require_cmd() { command -v "$1" >/dev/null 2>&1 || { echo "Missing required command: $1" >&2; exit 2; }; }
json_escape() { /usr/bin/python3 - <<'PY' "$1"
import json,sys
print(json.dumps(sys.argv[1]))
PY
}
require_cmd /usr/bin/python3
require_cmd /bin/date
require_cmd /usr/bin/stat
require_cmd /bin/pwd
host="$(/bin/hostname -s 2>/dev/null || /bin/hostname)"
generated_at="$(/bin/date -u +"%Y-%m-%dT%H:%M:%SZ")"
cwd="$(/bin/pwd)"
printf '{'
printf '"schema_version":"%s",' "0.1"
printf '"host":"%s",' "$host"
printf '"generated_at":"%s",' "$generated_at"
printf '"generated_from_cwd":%s,' "$(json_escape "$cwd")"
printf '"artifact_suggested_path":%s,' "$(json_escape "$DEFAULT_ARTIFACT_PATH")"
printf '"projects":['
first=1
for entry in "${ALLOWLIST[@]}"; do
  IFS='|' read -r id path type role status <<<"$entry"
  exists=false
  [[ -e "$path" ]] && exists=true
  mtime_epoch=""; size_bytes=""
  if $exists; then
    mtime_epoch="$(/usr/bin/stat -f "%m" "$path" 2>/dev/null || true)"
    size_bytes="$(/usr/bin/stat -f "%z" "$path" 2>/dev/null || true)"
  fi
  [[ $first -eq 1 ]] || printf ','
  first=0
  printf '{"id":"%s","path":%s,"type":"%s","role":"%s","status":"%s","exists":%s,"mtime_epoch":%s,"size_bytes":%s}' \
    "$id" "$(json_escape "$path")" "$type" "$role" "$status" "$exists" \
    "$( [[ -n "$mtime_epoch" ]] && printf '%s' "$mtime_epoch" || printf 'null' )" \
    "$( [[ -n "$size_bytes" ]] && printf '%s' "$size_bytes" || printf 'null' )"
done
printf ']}\n'
