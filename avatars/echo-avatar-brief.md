# Echo Avatar Brief

**Concept:** Dual concentric waves echoing around a core orb; captures the 🔁 emoji and context-mirroring role.

## Visual Notes
- Background gradient: #0b1121 → #05060b with concentric circular gridlines (#7f9cff at 20%).
- Needle renders as double-ended arc referencing repeated signals in violet (#c78bff) and teal (#7df9ff).
- Mono variant: clean grayscale.

## Generator Flags
```
scripts/generate-avatar.sh \
  --output avatars/echo-avatar.png \
  --mode color \
  --bg-top #0b1121 \
  --bg-bottom #05060b \
  --grid #7f9cff \
  --needle-tip #7df9ff \
  --needle-base #c78bff \
  --tail-cutout #05060b \
  --highlight #f5f7ff \
  --needle-angle 0 \
  --grid-spacing 60
```

Approved? Pending.
