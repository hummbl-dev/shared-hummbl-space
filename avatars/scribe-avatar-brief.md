# Scribe Avatar Brief

**Concept:** Archival parchment badge for HUMMBL’s historian. Warm sepia field with quill-tinted needle.

## Visual Notes
- Background gradient (#20160b → #0c0703) plus gold grid (#f3d18b).
- Needle base parchment ivory (#f8f0db); tip bronze ink (#c98d3a).
- Highlight (#fff7da) simulates aged vellum.

## Generator Flags
```bash
scripts/generate-avatar.sh \
  --output avatars/scribe-avatar.png \
  --mode color \
  --bg-top '#20160b' \
  --bg-bottom '#0c0703' \
  --grid '#f3d18b' \
  --needle-tip '#c98d3a' \
  --needle-base '#f8f0db' \
  --tail-cutout '#120a04' \
  --highlight '#fff7da' \
  --needle-angle 10 \
  --grid-spacing 62
scripts/generate-avatar.sh --output avatars/scribe-avatar-mono.png --mode mono --needle-angle 10 --grid-spacing 62
```

Approval: ✅ Reuben (2026-02-05).
