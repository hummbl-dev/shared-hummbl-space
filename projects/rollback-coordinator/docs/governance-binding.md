# Governance Binding – Rollback Coordinator

| Profile | Audit | Separation | Behavior |
|---------|-------|------------|----------|
| Flow | basic | none | Single operator (Circuit) may execute; logging to RUN_LOG + git. |
| Balanced | full | propose_only | Planner (Vector) drafts plan, Runner (Circuit) executes; HUMMBL-GOVERNOR AUTHORIZE required. |
| Strict | signed | full_split | Planner, Reviewer (Guardian), Runner (Harbor) all separate; signed audit artifact + dual approval. |

## Integration Steps
1. Coordinator queries current profile (Flow/Balanced/Strict) from governance SDK.
2. For balanced/strict, collect approvals and include HUMMBL-GOVERNOR decision record.
3. Log final action to `memory/YYYY-MM-DD.md` with `AUTHORIZE/DENY` references.
