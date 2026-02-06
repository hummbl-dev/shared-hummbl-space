# Relayor Avatar Brief

**Concept:** Baton-passing motif with warm gold tip and cool blue base, echoing precise handoffs.

## Visual Notes
- Deep navy field (#0a1426 → #03070d) with pale cyan grid (#8ef2ff).
- Needle base frosted blue (#d9ecff); tip golden signal (#ffd95a) angled backward to represent passing motion.
- Highlight (#fff1c7) adds tactile glow.

## Generator Flags
```bash
scripts/generate-avatar.sh \
  --output avatars/relayor-avatar.png \
  --mode color \
  --bg-top '#0a1426' \
  --bg-bottom '#03070d' \
  --grid '#8ef2ff' \
  --needle-tip '#ffd95a' \
  --needle-base '#d9ecff' \
  --tail-cutout '#050b16' \
  --highlight '#fff1c7' \
  --needle-angle -24 \
  --grid-spacing 60
scripts/generate-avatar.sh --output avatars/relayor-avatar-mono.png --mode mono --needle-angle -24 --grid-spacing 60
```

Approval: ✅ Reuben (2026-02-05).
