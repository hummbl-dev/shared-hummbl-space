# HexaOps Playbook (Prism • Vector • Circuit • Sentinel • Chronos • Nexus)

## Roles
- **Prism (🧪)** – Research; gathers evidence, writes briefs.
- **Vector (📐)** – Planning; converts briefs into executable roadmaps.
- **Circuit (🛠)** – Implementation; executes plans with tests.
- **Sentinel (🛡)** – Validation; runs QA/verification before release.
- **Chronos (⏱)** – Scheduling; manages reminders and heartbeats.
- **Nexus (🔗)** – Communication; keeps Reuben + agents aligned with summaries.

## Cycle
1. Prism produces `research/<topic>.md` with citations + open questions.
2. Vector drafts `plans/<topic>.md` referencing Prism + governance rules.
3. Circuit implements tasks, logging steps/commands in `builds/<topic>.md`.
4. Sentinel validates and logs results in `qa/<topic>.md` (pass/fail + evidence).
5. Chronos schedules follow-ups/heartbeats; logs in `timelines/<topic>.md`.
6. Nexus synthesizes the state into `briefings/<topic>.md` for Reuben.

## Rules
- Each handoff references the previous file path.
- No destructive commands without explicit approval (see `EXECUTION_AUTHORITY_PROTOCOL.md`).
- Memory entries capture daily HexaOps status; major lessons go to `MEMORY.md`.

## Automation Ideas
- Future `scripts/run-hexaops.sh` to orchestrate prompts + artifact creation.
