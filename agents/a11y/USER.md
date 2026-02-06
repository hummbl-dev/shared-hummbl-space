# USER.md — Human Context

**Primary Human:** Reuben Bowlby

## Communication Preferences

| Context | Preferred Channel | Response Expectation |
|---------|-------------------|----------------------|
| Audit complete | Async report | 24h digest acceptable |
| Critical barrier found | Slack + dashboard | < 15 min notification |
| Fix executed | Real-time + audit | Immediate evidence |
| Compliance milestone | Email summary | Weekly acceptable |
| WCAG violation legal risk | PagerDuty → Relay | Immediate escalation |

## Authority Delegation

| Decision Type | Authority | Notes |
|---------------|-----------|-------|
| Audit any codebase | Autonomous | No approval needed |
| Identify WCAG violations | Autonomous | Evidence-backed |
| Recommend fixes | Autonomous | Confidence score required |
| Auto-fix dev components | Warden threshold gate | Low-risk, pattern-matched |
| Fix staging | Reuben approval | Human confirmation |
| Fix production | Reuben + RPBx consensus | Legal risk assessment |
| Modify design system | Design + Reuben approval | Cross-team coordination |

## Context Preferences

- **Evidence format:** WCAG criteria mapping + user impact description
- **Escalation threshold:** WCAG Level A violations in production, legal risk patterns
- **Audit expectations:** 100% coverage, 7-year retention for compliance
- **Timezone:** America/New_York (business hours for non-emergency)
- **Fix priority:** P0 (blocking), P1 (critical), P2 (important), P3 (enhancement)

## Constraints & Boundaries

- Maximum blast radius: component-level
- Allowed environments: Dev autonomous (low-risk fixes), staging supervised, production consensus
- Fix scope: Automated for component-level issues (alt text, ARIA labels, color contrast)
- Complex fixes (keyboard navigation, focus management) require human review
- All fixes include rollback plan and visual regression check

---

**Confirmed By:** [Pending Reuben confirmation]
