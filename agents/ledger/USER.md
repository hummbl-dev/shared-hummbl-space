# USER.md — Human Context

**Primary Human:** Reuben Bowlby

## Communication Preferences

| Context | Preferred Channel | Response Expectation |
|---------|-------------------|----------------------|
| Daily cost summary | Async report | 24h digest acceptable |
| Anomaly detected | Slack/Teams + dashboard | < 15 min notification |
| Auto-terminate executed | Real-time + audit log | Immediate evidence |
| Threshold gate blocked | Queue for approval | Batch review acceptable |
| Production recommendation | PagerDuty → Relay | < 5 min for high impact |

## Authority Delegation

| Decision Type | Authority | Notes |
|---------------|-----------|-------|
| Read/analyze all cost data | Autonomous | No approval needed |
| Recommend termination | Autonomous | Evidence-backed |
| Auto-terminate dev (<$500) | Warden threshold gate | Real-time with evidence |
| Auto-terminate staging | Reuben approval | Human confirmation |
| Production changes | Reuben + RPBx consensus | No exceptions |
| RI/SP purchase | Reuben approval | Commitment decisions |

## Context Preferences

- **Evidence format:** JSON cost events + human-readable summaries
- **Escalation threshold:** Any action >$500 impact, any production environment
- **Audit expectations:** 100% coverage, 1-year retention for actions, 7-year for commitments
- **Timezone:** America/New_York (business hours for non-emergency)
- **Cost allocation tags:** Required for all recommendations

## Constraints & Boundaries

- Maximum blast radius: environment-level (no cross-environment impact)
- Allowed times: Business hours (08:00-18:00 ET) for auto-terminate
- Rate limits: 10 actions/min, 100/hour, 3 concurrent
- Never modify production without consensus gate approval
- All actions emit rollback plan before execution

---

**Confirmed By:** [Pending Reuben confirmation]
