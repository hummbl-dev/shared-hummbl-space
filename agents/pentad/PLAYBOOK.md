# Pentad Playbook (Atlas • Forge • Vigil • Quorum • Flux)

## Roles
- **Atlas (🧠)** – Strategy lead; defines objectives + dependencies.
- **Forge (🔧)** – Builder; implements approved work.
- **Vigil (👁️)** – Monitoring; watches telemetry for regressions.
- **Quorum (📊)** – Analytics; summarizes progress & metrics.
- **Flux (♻️)** – Automation; wires scripts/heartbeat routines to keep the loop running.

## Flow
1. **Atlas** drafts strategy doc (`agents/atlas/plans/<topic>.md`).
2. **Forge** implements tasks referencing the strategy; logs evidence in `agents/forge/builds/<topic>.md`.
3. **Vigil** monitors after each build; files reports in `agents/vigil/checks/<topic>.md`.
4. **Quorum** compiles metrics into `agents/quorum/dashboards/<topic>.md`.
5. **Flux** automates repeatable steps, updating `scripts/` and documenting in `agents/flux/automations/<topic>.md`.
6. Cycle repeats until objectives satisfied; Atlas/Quorum update `MEMORY.md` and SITREPs.

## Coordination Rules
- Each step references prior artifacts (paths + line numbers).
- Changes to production scripts require Reuben’s approval per `EXECUTION_AUTHORITY_PROTOCOL.md`.
- Daily memory entries should note Pentad status; add long-term lessons to `MEMORY.md`.

## Future Automation
- Potential `scripts/run-pentad.sh` to orchestrate prompts/logging.
