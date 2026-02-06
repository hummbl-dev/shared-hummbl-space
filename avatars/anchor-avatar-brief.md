# Anchor Avatar Brief

**Concept:** Nautical mooring badge conveying steadiness. Midnight navy field with gold tether tip mirrors Anchor’s fallback stewardship.

## Visual Notes
- Dark harbor gradient (#071525 → #030810) with calm grid lines (#58a6ff).
- Needle base in misty steel (#d9e5ef) pointing slightly west; tip glows amber (#f8b35a).
- Warm highlight (#fbe7c3) suggests polished brass hardware.

## Generator Flags
```bash
scripts/generate-avatar.sh \
  --output avatars/anchor-avatar.png \
  --mode color \
  --bg-top '#071525' \
  --bg-bottom '#030810' \
  --grid '#58a6ff' \
  --needle-tip '#f8b35a' \
  --needle-base '#d9e5ef' \
  --tail-cutout '#010307' \
  --highlight '#fbe7c3' \
  --needle-angle -6 \
  --grid-spacing 54
scripts/generate-avatar.sh --output avatars/anchor-avatar-mono.png --mode mono --needle-angle -6 --grid-spacing 54
```

Approval: ✅ Reuben (2026-02-05).
