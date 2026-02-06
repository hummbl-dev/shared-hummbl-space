# HUMMBL Shared Agent Workspace

This directory houses the canonical agent identity stack (agents, avatars, scripts, memory, and governance docs). Every local workspace should link to these files so all HUMMBL agents share the same context.

## Contents

- `agents/` – all individual agent directories + team playbooks
- `avatars/` – avatar PNGs/briefs + gallery
- `scripts/` – tooling (`lint_agents.py`, `check_avatars.py`, `link-shared-workspace.sh`, etc.)
- `memory/` – daily + long-term memory files
- `AGENT*.md`, `IDENTITY.md`, `USER.md`, `SOUL.md` – root identity stack for the primary agent

## Linking into another workspace

```bash
# Example: link into ~/workspace/my-project
shared-hummbl-space/scripts/link-shared-workspace.sh ~/workspace/my-project
```
This creates symlinks so any agent working inside `~/workspace/my-project` reads/writes the shared files.

## Lint / Health Checks

```bash
cd shared-hummbl-space
scripts/lint_agents.py
scripts/check_avatars.py
```
Use these before commits to ensure agents, avatars, and directories remain consistent.

## Git Usage

The shared workspace is a git repo. Track changes normally:

```bash
cd shared-hummbl-space
git add agents/... avatars/... scripts/... memory/... README.md
git commit -m "Update agent identities"
```
Push this repo to your private remote so other machines can clone it and re-link as needed.

## Local CI
Run `npm run ci` to mirror the GitHub lint/avatar checks before pushing.

## Registries

See `registries/` for machine-readable inventories:

- `agents.json` – generated map of agents/teams. Each record exposes a `callsign` (directory slug usable by tooling), display `name`, `emoji`, `summary`, `status`, canonical `home`, artifact folders, and `type` (agent or team).
- `playbooks.json` – team playbooks with member lists.
- `tools.json` – lint/test/automation scripts with descriptions.
- `governance.json` – policy references (HUMMBL-GOVERNOR, Flow/Balanced/Strict, PLAN).
- `workstreams.json` – active initiatives (e.g., rollback coordinator).
- `memory.json` – memory cadence + promotion guidelines.

Use `scripts/agent_lookup.py <callsign>` to inspect any entry:

```bash
scripts/agent_lookup.py axis
scripts/agent_lookup.py octave --json
```

## Git Sync Procedure

Before committing:

1. `git pull --rebase origin main`
2. Run `npm run ci` (lint + avatar checks) and `npm run markdownlint`/`npm run cspell` (coming via package.json scripts).
3. After the Flow-mode run log and memory updates, `git push origin main` (or feature branch if protections require).
