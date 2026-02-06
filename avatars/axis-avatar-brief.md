# Axis Avatar Brief

**Concept:** Balanced compass for alignment strategist. Teal grid + gold tip show equilibrium between strategy and execution.

## Visual Notes
- Gradient (#051b2b → #030b13) evokes calm starchart.
- Grid in aqua-mint (#7ef2d1) with ivory base needle (#d0f4ff) and golden tip (#f4c76a).
- Subtle highlight (#fdf5d3) keeps premium finish.

## Generator Flags
```bash
scripts/generate-avatar.sh \
  --output avatars/axis-avatar.png \
  --mode color \
  --bg-top '#051b2b' \
  --bg-bottom '#030b13' \
  --grid '#7ef2d1' \
  --needle-tip '#f4c76a' \
  --needle-base '#d0f4ff' \
  --tail-cutout '#031019' \
  --highlight '#fdf5d3' \
  --needle-angle 8 \
  --grid-spacing 56
scripts/generate-avatar.sh --output avatars/axis-avatar-mono.png --mode mono --needle-angle 8 --grid-spacing 56
```

Approval: ✅ Reuben (2026-02-05).
