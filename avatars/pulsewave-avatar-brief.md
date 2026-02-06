# Pulsewave Avatar Brief

**Concept:** Neon telemetry arc for the signal analyst. Electric cyan gradient echoing spectrum scans.

## Visual Notes
- Midnight spectrum background (#031226 → #050a12) with aqua grid (#53fff0).
- Needle base cool blue (#9dc9ff) and tip pure cyan (#00f7ff) angled forward.
- Highlight (#dff4ff) for instrument glass.

## Generator Flags
```bash
scripts/generate-avatar.sh \
  --output avatars/pulsewave-avatar.png \
  --mode color \
  --bg-top '#031226' \
  --bg-bottom '#050a12' \
  --grid '#53fff0' \
  --needle-tip '#00f7ff' \
  --needle-base '#9dc9ff' \
  --tail-cutout '#01030a' \
  --highlight '#dff4ff' \
  --needle-angle 32 \
  --grid-spacing 58
scripts/generate-avatar.sh --output avatars/pulsewave-avatar-mono.png --mode mono --needle-angle 32 --grid-spacing 58
```

Approval: ✅ Reuben (2026-02-05).
