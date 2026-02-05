# Avatar Assets

| File | Purpose | Approval |
|------|---------|----------|
| `codex-avatar.png` | Primary color badge for Codex 🧭 | ✅ Approved |
| `codex-avatar-mono.png` | Monochrome/CLI variant | ✅ Approved |
| `codex-avatar.svg` | Source vector sketch | Not reviewed |
| `generate_compass_avatar.py` | Procedural renderer for compass avatars | Ready |
| `scripts/generate-avatar.sh` | Convenience wrapper for the generator | Ready |
| `GALLERY.md` | Emoji/avatar roster (all agents) | Ready |
| `codex-avatar-brief.md` | Creative direction + palette | Ready |

## Generating Variants
```bash
scripts/generate-avatar.sh --output avatars/<agent>-avatar.png --mode color
scripts/generate-avatar.sh --output avatars/<agent>-avatar-mono.png --mode mono
```

Override colors (hex) or geometry to match a new agent:
```bash
scripts/generate-avatar.sh \
  --output avatars/new-agent.png \
  --bg-top #1a2b3c --bg-bottom #05080f \
  --needle-tip #f94c57 --needle-base #c5d2e8 \
  --grid #7fffd4 --needle-angle 25
```

Record approvals + notes in `AGENT_BIRTH_PROCESS.md` so every agent’s emoji/avatar pairing stays traceable.
