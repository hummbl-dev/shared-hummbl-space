# Pulse Avatar Brief

**Concept:** Neon pulse wave coursing through a shield badge — the ⚡ emoji rendered as a protective waveform.

## Visual Notes
- Circular badge 512×512.
- Background gradient: #040b18 → #101f3c with faint vertical scanlines in cyan (#5cffe6 at 15%).
- Main motif: stylized sine wave shaped like a lightning bolt, metallic silver base (#dde6ff) with electric yellow highlight (#ffd45c).
- Accent: small status LED (#ff5c8a) near bottom.
- Mono version: grayscale gradient.

## Generator Flags
```
scripts/generate-avatar.sh \
  --output avatars/pulse-avatar.png \
  --mode color \
  --bg-top #101f3c \
  --bg-bottom #040b18 \
  --grid #5cffe6 \
  --needle-tip #ffd45c \
  --needle-base #dde6ff \
  --tail-cutout #03050a \
  --highlight #ff5c8a \
  --needle-angle 12 \
  --grid-spacing 48
```

Approved? Pending.
