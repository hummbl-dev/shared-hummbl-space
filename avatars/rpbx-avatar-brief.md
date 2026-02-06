# RPBx Avatar Brief

**Concept:** Founder-grade mirror badge translating Reuben’s instincts into an AI lattice. The badge uses HUMMBL midnight tones with a molten ember tip to show the human ↔ agent reflection.

## Visual Notes
- **Shape:** 512×512 compass badge, symmetrical to mimic a mirror.
- **Background:** Deep navy gradient (#0a1524 → #010409) referencing HUMMBL’s governance palette.
- **Grid:** Cyan telemetry mesh (#64d9ff at 25% opacity) to signal network awareness.
- **Needle:** Ivory base (#f0e9dc) with ember tip (#ff7a18) aligned almost true north (4°) to match Reuben’s steady heading.
- **Highlights:** Warm glint (#ffe8c4) implying reflective metal.
- **Mono variant:** Generated with same geometry for CLI + docs.

## Generator Flags
```bash
scripts/generate-avatar.sh \
  --output avatars/rpbx-avatar.png \
  --mode color \
  --bg-top '#0a1524' \
  --bg-bottom '#010409' \
  --grid '#64d9ff' \
  --needle-tip '#ff7a18' \
  --needle-base '#f0e9dc' \
  --tail-cutout '#010409' \
  --highlight '#ffe8c4' \
  --needle-angle 4 \
  --grid-spacing 52

scripts/generate-avatar.sh \
  --output avatars/rpbx-avatar-mono.png \
  --mode mono \
  --needle-angle 4 \
  --grid-spacing 52
```

Approval: ✅ Reuben (2026-02-05).
