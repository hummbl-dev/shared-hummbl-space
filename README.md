# HUMMBL Shared Agent Workspace

This directory houses the canonical agent identity stack (agents, avatars, scripts, memory, and governance docs). Every local workspace should link to these files so all HUMMBL agents share the same context.

## Contents
- `agents/` – all individual agent directories + team playbooks
- `avatars/` – avatar PNGs/briefs + gallery
- `scripts/` – tooling (`lint_agents.py`, `check_avatars.py`, `link-shared-workspace.sh`, etc.)
- `memory/` – daily + long-term memory files
- `AGENT*.md`, `IDENTITY.md`, `USER.md`, `SOUL.md` – root identity stack for the primary agent

## Linking into another workspace
```
# Example: link into ~/workspace/my-project
shared-hummbl-space/scripts/link-shared-workspace.sh ~/workspace/my-project
```
This creates symlinks so any agent working inside `~/workspace/my-project` reads/writes the shared files.

## Lint / Health Checks
```
cd shared-hummbl-space
scripts/lint_agents.py
scripts/check_avatars.py
```
Use these before commits to ensure agents, avatars, and directories remain consistent.

## Git Usage
The shared workspace is a git repo. Track changes normally:
```
cd shared-hummbl-space
git add agents/... avatars/... scripts/... memory/... README.md
git commit -m "Update agent identities"
```
Push this repo to your private remote so other machines can clone it and re-link as needed.
