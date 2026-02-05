# Dialectical Trio Playbook

Agents: Thesis (💡), Antithesis (⚔️), Synthesis (🔄).

## Cycle
1. **Thesis** collects evidence, drafts structured propositions (numbered, cited) and logs output under `agents/thesis/debates/<topic>.md`.
2. **Antithesis** reads the thesis, highlights contradictions/gaps, and writes counterpoints in `agents/antithesis/debates/<topic>.md`.
3. **Synthesis** reconciles both, producing decisions + action plans in `agents/synthesis/debates/<topic>.md` plus SITREP/memory summaries.

## Rules
- Every step cites files/line numbers or command outputs.
- Each agent updates its `memory/YYYY-MM-DD.md` with the debate summary.
- Synthesis cannot close the loop until both Thesis & Antithesis are logged.
- If Reuben requests iteration 2+, repeat the cycle (Thesis2, Antithesis2, etc.) until satisfied.

## Files
- `agents/<name>/debates/` — create per-topic subfolders.
- `avatars/GALLERY.md` — update status after approvals.
- `memory/YYYY-MM-DD.md` — capture notable debates & decisions.

## Approvals
- Reuben approves each agent's identity/avatar before operation.
- For destructive recommendations, escalate via `EXECUTION_AUTHORITY_PROTOCOL.md`.

## Automation Ideas
- Future `scripts/run-dialectic.sh` could coordinate prompts/logs (not yet built).
