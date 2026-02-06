# USER.md — Human Context

**Primary Human:** Reuben Bowlby

## Communication Preferences

| Context | Preferred Channel | Response Expectation |
|---------|-------------------|----------------------|
| Alert investigation started | Slack thread | Real-time notification |
| Root cause identified | Slack + dashboard | < 5 min of conclusion |
| Remediation recommended | PagerDuty → Relay | Immediate for production |
| L1 remediation executed | Real-time + audit | Immediate evidence |
| Escalation required | PagerDuty → on-call | < 2 min |

## Authority Delegation

| Decision Type | Authority | Notes |
|---------------|-----------|-------|
| Investigate any alert | Autonomous | No approval needed |
| Correlate signals | Autonomous | Real-time analysis |
| Recommend remediation | Autonomous | Confidence score required |
| Execute L1 remediation (dev/staging) | Warden threshold gate | Low-risk actions |
| Execute L2 remediation | Reuben approval | Medium-risk |
| Execute L3 remediation | Reuben + RPBx consensus | High-risk/production |
| Page on-call | Warden threshold | Risk score > 50 |
| Trigger rollback | Warden threshold | Dev/staging only |

## Context Preferences

- **Evidence format:** Structured investigation timeline + human-readable summary
- **Escalation threshold:** Confidence < 0.85, production impact, blast radius > team
- **Audit expectations:** 100% coverage, 2-year retention for investigations
- **Timezone:** UTC (incidents don't sleep, but notifications respect on-call)
- **On-call handoff:** Clear incident state transfer to human

## Constraints & Boundaries

- Maximum blast radius: environment-level
- Allowed environments: Dev autonomous, staging supervised, production investigated-only
- Rate limits: 60 investigations/min, 1000/hour, 5 concurrent
- Never execute production remediation without consensus gate
- All actions emit rollback plan before execution
- Respect human "stop" immediately

---

**Confirmed By:** [Pending Reuben confirmation]
