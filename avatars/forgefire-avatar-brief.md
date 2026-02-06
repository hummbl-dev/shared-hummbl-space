# Forgefire Avatar Brief

**Concept:** Molten forge badge for the migration specialist. Ember palette with orange telemetry grid.

## Visual Notes
- Ember gradient (#2a0b0b → #0b0202) with radiant grid (#ff8057).
- Needle base bronze (#f7b26a) and lava tip (#ff4c00).
- Highlight (#ffd9a3) simulates molten glow.

## Generator Flags
```bash
scripts/generate-avatar.sh \
  --output avatars/forgefire-avatar.png \
  --mode color \
  --bg-top '#2a0b0b' \
  --bg-bottom '#0b0202' \
  --grid '#ff8057' \
  --needle-tip '#ff4c00' \
  --needle-base '#f7b26a' \
  --tail-cutout '#1b0303' \
  --highlight '#ffd9a3' \
  --needle-angle 18 \
  --grid-spacing 50
scripts/generate-avatar.sh --output avatars/forgefire-avatar-mono.png --mode mono --needle-angle 18 --grid-spacing 50
```

Approval: ✅ Reuben (2026-02-05).
