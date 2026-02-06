# Shield Avatar Brief

**Concept:** Compliance sentinel badge with glacial blues and solid alignment.

## Visual Notes
- Dark navy gradient (#081523 → #02070d) with cyan grid (#52d6ff).
- Needle base frosted (#bde5ff) and tip cobalt (#2ea0ff) leaning defensively.
- Highlight (#e2f5ff) for armored sheen.

## Generator Flags
```bash
scripts/generate-avatar.sh \
  --output avatars/shield-avatar.png \
  --mode color \
  --bg-top '#081523' \
  --bg-bottom '#02070d' \
  --grid '#52d6ff' \
  --needle-tip '#2ea0ff' \
  --needle-base '#bde5ff' \
  --tail-cutout '#030a13' \
  --highlight '#e2f5ff' \
  --needle-angle -12 \
  --grid-spacing 56
scripts/generate-avatar.sh --output avatars/shield-avatar-mono.png --mode mono --needle-angle -12 --grid-spacing 56
```

Approval: ✅ Reuben (2026-02-05).
