# Spark Avatar Brief

**Concept:** Innovation spark badge with magenta telemetry grid and molten ember tip.

## Visual Notes
- Cosmic plum gradient (#1a021d → #040005) and neon grid (#ff66d0).
- Needle base warm gold (#ffe396); tip ember orange (#ff5f1f).
- Highlight (#ffd7b5) keeps the glow lively.

## Generator Flags
```bash
scripts/generate-avatar.sh \
  --output avatars/spark-avatar.png \
  --mode color \
  --bg-top '#1a021d' \
  --bg-bottom '#040005' \
  --grid '#ff66d0' \
  --needle-tip '#ff5f1f' \
  --needle-base '#ffe396' \
  --tail-cutout '#08000a' \
  --highlight '#ffd7b5' \
  --needle-angle 28 \
  --grid-spacing 48
scripts/generate-avatar.sh --output avatars/spark-avatar-mono.png --mode mono --needle-angle 28 --grid-spacing 48
```

Approval: ✅ Reuben (2026-02-05).
