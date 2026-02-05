# Red/Blue/Purple Team Playbook

## Roles
- **Redline (🔴)** — Offensive simulations, produces finding reports.
- **Bluewall (🔵)** — Defensive mitigation/validation, responds to findings.
- **Purplebridge (🟣)** — Coordinator ensuring red+blue outputs become tracked actions.

## Parallel Workflow
1. **Task kickoff:** Purplebridge logs the scenario (SITREP or issue) and assigns Redline/Bluewall objectives.
2. **Parallel execution:**
   - Redline runs approved offensive probes, logs evidence -> `agents/redline/debriefs/<topic>.md`.
   - Bluewall simultaneously reviews existing defenses, prepares mitigations -> `agents/bluewall/debriefs/<topic>.md`.
3. **Sync checkpoint:** Purplebridge aggregates both feeds, highlights gaps, and updates SITREP/memory.
4. **Closure:** Once mitigations verified, Purplebridge archives the cycle and records approvals.

## Documentation
- Each agent maintains `debriefs/` per topic; Purplebridge references them in SITREPs.
- `avatars/GALLERY.md` tracks identity approvals.
- `memory/YYYY-MM-DD.md` records cross-team status.

## Rules
- No destructive commands without approval.
- Redline findings must include reproduction steps + severity.
- Bluewall responses must include verification commands.
- Purplebridge closes out only when verification evidence is logged.

## Future Automation Ideas
- `scripts/run-red-blue-purple.sh` to orchestrate prompts/logging (not yet built).
