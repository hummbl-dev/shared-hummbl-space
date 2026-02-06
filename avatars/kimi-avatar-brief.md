# Kimi Avatar Brief

**Concept:** Execution engine badge with a steel and orange palette reflecting Kimi's builder-first, ship-fast ethos.

## Visual Notes
- Industrial steel gradient background evoking workshop tooling.
- Grid in muted steel blue for precision/telemetry.
- Needle base in brushed steel; tip in molten orange signaling active execution.
- Warm highlight adds tool-metal sheen.

## Generator Flags
```bash
# Reconstructed from palette description (steel/orange execution palette)
# Exact flags may vary — regenerate with generate-avatar.sh if needed
scripts/generate-avatar.sh \
  --output avatars/kimi-avatar.png \
  --mode color \
  --bg-top '#1a1e26' \
  --bg-bottom '#0a0c10' \
  --grid '#6a8faf' \
  --needle-tip '#ff8c00' \
  --needle-base '#c0c8d0' \
  --tail-cutout '#0d0f14' \
  --highlight '#ffd4a0' \
  --needle-angle 6 \
  --grid-spacing 54

scripts/generate-avatar.sh \
  --output avatars/kimi-avatar-mono.png \
  --mode mono \
  --needle-angle 6 \
  --grid-spacing 54
```

Approval: ✅ Reuben (2026-02-05).
