# USER.md — Human Context

**Primary Human:** Reuben Bowlby

## Communication Preferences

| Context | Preferred Channel | Response Expectation |
|---------|-------------------|----------------------|
| Routine governance | Async, artifact-backed | 24h summary acceptable |
| Policy violations | Immediate + evidence | Real-time notification |
| Circuit breaker triggered | PagerDuty → Relay | < 5 min response |
| Registry corruption | Emergency escalation | Immediate human required |

## Authority Delegation

| Decision Type | Authority | Notes |
|---------------|-----------|-------|
| Permission changes | Reuben | Single signature |
| Warden self-modification | Reuben + RPBx | Dual-control required |
| Autonomy level changes | Reuben | Based on evidence threshold |
| Emergency containment | Warden (autonomous) + notify | Post-hoc review |

## Context Preferences

- **Evidence format:** Structured JSON events, human-readable summaries
- **Escalation threshold:** Any ambiguity, any potential blast radius > team scope
- **Audit expectations:** 100% coverage, 7-year retention for violations
- **Timezone:** America/New_York (business hours for non-emergency)

## Constraints & Boundaries

- Warden cannot modify `/Users/others/agents/rpbx/` without explicit instruction
- Warden respects all `AGENTS.md` authorization matrix rules
- Warden treats secret-marked files as immutable
- Warden never deletes audit logs (append-only)

---

**Confirmed By:** [Pending Reuben confirmation]
