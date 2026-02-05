# Scout Avatar Brief

**Concept:** Edge-on satellite dish orbiting a HUMMBL-blue planet with neon telemetry arc. Emoji 🛰 translated into a crisp mission-patch badge.

## Visual Notes
- **Shape:** Circular badge 512×512.
- **Background:** Deep midnight gradient (#050918 → #0c1f3f) with subtle orbital grid arcs in aqua (#64ffc9 at 20% opacity).
- **Satellite:** Stylized dish + solar wing silhouette in cool silver (#c9d6ff) with electric violet accent (#ad7bff) on the tip.
- **Telemetry arc:** Neon mint (#64ffc9) swoosh trailing the dish, implying motion.
- **Highlights:** Minimal glints (#f5f5ff) on dish edges; drop shadow toward southeast.
- **Mono variant:** Same geometry, grayscale gradient for CLI use.

## Generator Flags
```
scripts/generate-avatar.sh \
  --output avatars/scout-avatar.png \
  --mode color \
  --bg-top #0c1f3f \
  --bg-bottom #050918 \
  --grid #64ffc9 \
  --needle-tip #ad7bff \
  --needle-base #c9d6ff \
  --tail-cutout #03060f \
  --highlight #f5f5ff \
  --needle-angle 28 \
  --grid-spacing 56
```

Approved by Reuben? **Pending** (share preview alongside mono variant).
