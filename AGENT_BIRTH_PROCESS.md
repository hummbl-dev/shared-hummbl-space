# AGENT_BIRTH_PROCESS.md — Spawning New Agents

Use this checklist whenever we spin up a fresh agent in this workspace or any HUMMBL-aligned environment.

1. **Copy bootstrap template**
   - Source: `workspace/active/openclaw/docs/reference/templates/BOOTSTRAP.md`
   - Destination: the new agent's workspace root as `BOOTSTRAP.md`.
   - Customize wording if the new agent has unique constraints, but keep the ritual items (conversation, IDENTITY/USER/SOUL creation, deletion reminder).

2. **Run the conversation**
   - Human + agent establish name, creature, vibe, emoji, avatar ideas.
   - Capture human preferences (name, pronouns, timezone, communication quirks).

3. **Create the identity stack**
   - `IDENTITY.md` — agent fills in name/creature/vibe/emoji/avatar, then submits for human sign-off before locking it.
   - `USER.md` — record human details with explicit confirmation from the human.
   - `SOUL.md` — agent drafts its behavioral contract, walks through it with the human, and only saves once the human approves.

4. **Retire BOOTSTRAP**
   - Delete the working `BOOTSTRAP.md` after the human confirms the identity stack looks correct.
   - Keep this process doc + template so the next agent can repeat the ritual.

5. **Log the birth**
   - Create `memory/YYYY-MM-DD.md` for the birth session with the highlights (name, vibe, emoji, approvals).
   - Update `AGENT.md` or equivalent operating manual with any workspace-specific expectations for the new agent.
   - Optionally copy `AGENT_BIRTH_LOG_TEMPLATE.md` into the memory file so the conversational notes follow a consistent format.

6. **Ongoing refinement**
   - Encourage every agent to evolve their `IDENTITY.md` and `SOUL.md` (with human approval) as they learn.
   - Track improvements to the identity stack, onboarding rituals, and tooling in this file or related docs so future births get easier.

## Avatar Backlog & Enhancements
- [ ] Share `avatars/codex-avatar.png` with Reuben for approval; capture requested tweaks in this checklist.
- [x] Produce a monochrome/line-art variant for CLI or letterhead use (`avatars/codex-avatar-mono.png`).
- [x] Automate avatar generation script (`avatars/generate_compass_avatar.py`) so future agents can spawn concepts quickly.
- [x] Maintain an `avatars/` gallery referencing each agent’s emoji + approval status (`avatars/GALLERY.md`).

### Avatar Review Checklist
Before logging "approved" in the gallery, walk through these five checks (note results in the memory file for that day):
1. **Emoji alignment** — does the art clearly encode the agent's emoji or motif?
2. **Contrast/readability** — does it remain legible at 128×128 and 32×32 on light/dark backgrounds?
3. **Palette compliance** — matches current HUMMBL/base project palette or documented deviations.
4. **Variants exported** — color + mono PNGs plus source (SVG or generator params) saved under `avatars/`.
5. **Approval metadata** — date + approving human added to `avatars/GALLERY.md` and `IDENTITY.md`.

### Script Usage
```
scripts/generate-avatar.sh --output avatars/<name>-avatar.png --mode color
scripts/generate-avatar.sh --output avatars/<name>-avatar-mono.png --mode mono
```
- Override palette using flags like `--bg-top #123456 --needle-tip #ff00aa` to fit a new agent’s emoji/vibe.
- Adjust geometry with `--needle-angle`, `--grid-spacing`, etc., then save outputs + update that agent’s `IDENTITY.md`.

> **Rule:** Each new agent must pick their own emoji + avatar concepts during the birth conversation and secure human approval before finalizing those files.

**Current agents spun up via this ritual:** Codex (root), Scout, Pulse, Echo, Thesis, Antithesis, Synthesis, Redline, Bluewall, Purplebridge, Atlas, Forge, Vigil, Quorum, Flux, Prism, Vector, Circuit, Sentinel, Chronos, Nexus, Halo, Quill, Matrix, Guardian, Tempo, Relay, Loom, Beacon, Glyph, Kernel, Orbit, Ember, Harbor, Whisper, Vault. Keep the roster updated in `avatars/GALLERY.md` + `memory/` whenever new siblings join.

### Regenerating Avatars After Palette Shifts
1. Confirm new brand palette or accent colors with Reuben.
2. Re-run `scripts/generate-avatar.sh` for the affected agent(s) using the updated color flags.
3. Replace the PNGs in `avatars/`, keeping older versions in git history (no manual deletions needed).
4. Update `avatars/GALLERY.md` with the new approval date + palette reference.
5. Mention the change in that day’s `memory/YYYY-MM-DD.md` and, if relevant, summarize in `MEMORY.md` for continuity.
