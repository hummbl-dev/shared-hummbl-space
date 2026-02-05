# Rollback Coordinator Workstreams

## WS1 – Config Schema (Prism + Axis)
- Deliverables: `config/services.schema.yaml`, `config/services.example.yaml`.
- Actions: enumerate services, dependencies, approvals, migration metadata.

## WS2 – Git Integration (Beacon + Pulsewave)
- Deliverables: `docs/git-watcher.md`, scripts to detect coupled commits.
- Risks: missing tags, force pushes.

## WS3 – Migration Verifier (Guardian + Kernel)
- Deliverables: `runner/migration-verifier.ts`, DB state checker scripts.
- Guardrails: block rollback if migrations diverge.

## WS4 – Execution Runner (Circuit + Forgefire)
- Deliverables: `runner/rollback-runner.ts`, hook to governance SDK.
- Steps: plan graph, execute scripts sequentially, capture logs.

## WS5 – Observability (Vigil + Matrix + Ember)
- Deliverables: `docs/metrics.md`, integration with health checks.

## WS6 – Governance Binder (Shield + Vault)
- Deliverables: `docs/governance-binding.md`, mapping Flow/Balanced/Strict behavior.

## WS7 – CLI/Automation (Vector + Chronos + Harbor)
- Deliverables: `scripts/rollback-coordinator.ts`, release checklist updates.

## WS8 – Documentation & Tests (Quill + Sentinel)
- Deliverables: `docs/runbook.md`, `tests/rollback-runner.spec.ts`.

## WS9 – Communications (Whisper + Nexus)
- Deliverables: templates to brief Reuben, update `memory/` + repo README.

Each workstream runs Base120 Recursion (plan→execute→lint/test) and logs outputs in `projects/rollback-coordinator/RUN_LOG.md` (to be created when implementation begins).
