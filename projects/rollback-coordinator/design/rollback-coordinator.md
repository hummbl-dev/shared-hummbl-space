# HUMMBL Cross-Service Rollback Coordinator

## Purpose
Build a governance-aware rollback orchestrator that can rewind multi-service deployments (API, worker, automation scripts, DB migrations) while respecting HUMMBL Base120 reasoning and Flow/Balanced/Strict profiles.

## Base120 Mapping
| Stage | Implementation |
|-------|----------------|
| P (Perspective) | Enumerate services, dependencies, release tooling (SITREP-2026-02-04-* references). |
| IN (Inversion) | Model failure cases (partial rollback, schema mismatch, missing approvals). |
| CO (Composition) | Architecture below (git watcher + dependency graph + runner + audit). |
| DE (Decomposition) | Workstreams WS1-WS9 (see `WORKSTREAMS.md`). |
| RE (Recursion) | Each workstream loops plan→execute→lint/tests via Sentinel scripts. |
| SY (Systems) | Integration with shared workspace, governance logging, GitHub repo.

## Architecture Overview

```text
┌────────────┐     ┌────────────────┐     ┌─────────────────┐
│ Git Watcher├────▶│ Dependency Map │────▶│ Rollback Planner │
└────────────┘     └────────────────┘     └─────────────────┘
         │                     │                      │
         ▼                     ▼                      ▼
  Release metadata      services.yaml          Governance Binder
         │                     │                      │
         └────────────┬────────┴────────────┬─────────┘
                      ▼                     ▼
              Rollback Runner       Migration Verifier
                      │                     │
                      ├────────┬────────────┤
                      ▼        ▼            ▼
            Health Checks   Audit Logger   Notification Bus
```
- **Git Watcher**: Detects deployment batches (commits with shared ticket/label).
- **Dependency Map**: YAML describing service order, rollback scripts, approvals.
- **Rollback Planner**: Builds execution graph per Flow/Balanced/Strict profile.
- **Migration Verifier**: Confirms DB state safe to rewind.
- **Runner**: Executes scripts with governance hooks; writes to audit bus.
- **Health Checks**: Ensures services healthy before/after rollback.
- **Audit Logger**: Writes artifacts to `memory/` + Git.
- **Notification Bus**: Notifies Whisper/Nexus/Chronos of status.

## Governance Integration
- **Flow**: audit basic, separation none → single runner allowed.
- **Balanced**: audit full, separation propose_only → planner vs runner split.
- **Strict**: audit signed, separation full_split → requires GOV approval & dual runners.
- Use HUMMBL-GOVERNOR contract for `AUTHORIZE/ DENY` decisions (see HUMMBL-GOVERNOR spec).

## Data Model
```yaml
services:
  api:
    depends_on: [db]
    rollback_script: scripts/api-rollback.sh
    approvals: [guardian]
  worker:
    depends_on: [api]
    rollback_script: scripts/worker-rollback.sh
  db:
    migrations:
      tool: prisma
      state_command: scripts/check-db-state.sh
    rollback_script: scripts/db-rollback.sh
```

## Interfaces
- CLI: `scripts/rollback-coordinator.ts` (future) with subcommands:
  - `plan <batch>`
  - `execute <plan-file>`
  - `status <batch>`
- API hooks: Governance SDK (see `docs/plans/2026-02-04-governance-modes-design.md`).

## Observability
- Metrics -> Matrix/Ember: duration, success/failure, service health.
- Logs -> Vault: append to `memory/YYYY-MM-DD.md` + `RUN_LOG.md`.

## Next Steps
- Fill workstreams (`WORKSTREAMS.md`).
- Flesh out config schema (`config/services.schema.yaml`).
- Prototype runner stubs.
- Integrate lint/test automation.
