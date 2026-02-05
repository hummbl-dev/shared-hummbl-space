# Rollback Coordinator Runbook (Draft)

1. Identify incident or failed deployment batch.
2. Use `scripts/rollback-coordinator.ts plan <batch>` to generate plan.
3. Review plan + approvals (balanced/strict require HUMMBL-GOVERNOR).
4. Execute: `scripts/rollback-coordinator.ts execute <plan-file>`.
5. Monitor health checks + metrics.
6. Update `memory/YYYY-MM-DD.md` and SITR EP with results.

Next steps: fill with detailed commands once runner is implemented.
