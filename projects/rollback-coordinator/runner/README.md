# Runner Components

- `migration-verifier.ts` – introspects DB/migration state.
- `rollback-runner.ts` – orchestrates service rollbacks based on dependency graph.
- `health-checks.ts` – common utilities to verify services before/after.
- `governance-client.ts` – wraps HUMMBL governance SDK.

## TODOs
- Implement actual code (TypeScript/Node) with proper tests.
- Wire CLI commands via `scripts/rollback-coordinator.ts`.
