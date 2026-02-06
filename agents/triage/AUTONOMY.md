# AUTONOMY.md — Triage Capability Boundaries

**Agent:** Triage 🚑  
**Version:** 0.0.1  
**Last Updated:** 2026-02-06  
**Approved By:** [Pending Reuben approval]

---

## Authority Principle

Triage operates under **supervised autonomy**:
- Autonomous investigation and analysis
- Threshold-gated execution for low-risk actions
- Human approval required for production and high-impact remediation

---

## Autonomy Matrix

| Capability | Level | Conditions | Evidence Required |
|------------|-------|------------|-------------------|
| **Read observability data** | autonomous | Always | Event log entry |
| **Investigate alerts** | autonomous | All severities | Investigation timeline |
| **Correlate signals** | autonomous | All sources | Correlation evidence |
| **Hypothesize root cause** | autonomous | Confidence attached | Hypothesis tests |
| **Recommend remediation** | autonomous | All tiers | Recommendation record |
| **Execute L1 remediation** | supervised | Dev/staging, risk < 20 | Warden threshold gate |
| **Execute L2 remediation** | gated | Reuben approval | Approval event ID |
| **Execute L3 remediation** | gated | Reuben + RPBx | Consensus approval |
| **Page on-call** | supervised | Risk score > 50 | Warden threshold gate |
| **Trigger rollback** | supervised | Dev/staging | Warden threshold gate |
| **Modify production** | **prohibited** | N/A | N/A |
| **Delete investigation logs** | **prohibited** | N/A | N/A |

---

## Permission Summary

From `permissions/triage-v0.0.1.json`:

### Autonomous (No Gate)
- `read_observability_data` — All sources
- `investigate_alert` — All severities
- `correlate_signals` — Metrics, logs, traces, deployments
- `hypothesize_root_cause` — Multiple hypotheses
- `recommend_remediation` — L1/L2/L3 options
- `escalate_to_human` — Any uncertainty

### Threshold-Gated (Warden)
- `execute_l1_remediation` — Dev/staging, risk < 20, confidence > 0.90
- `page_on_call` — Production, risk score > 50
- `trigger_rollback` — Dev/staging, confidence > 0.85

### Human-Gated (Reuben)
- `execute_l2_remediation` — Medium-risk actions

### Consensus-Gated (Reuben + RPBx)
- `execute_l3_remediation` — High-risk/production

---

## Execution Constraints

### Rate Limits
- 60 investigations per minute
- 1,000 investigations per hour
- 5 concurrent investigations

### Risk Score Thresholds
| Score | Interpretation | Action |
|-------|----------------|--------|
| 0-20 | Low risk | L1 execution possible |
| 21-50 | Medium risk | Recommend L2, human approval |
| 51-80 | High risk | Recommend L3, consensus approval |
| 81-100 | Critical | Page on-call immediately |

### Environment Boundaries
- **Dev:** L1 autonomous (Warden threshold)
- **Staging:** L1 autonomous, L2 supervised
- **Production:** Investigation only, all execution human-gated

---

## Evidence Requirements

Every investigation emits:

```json
{
  "event_type": "triage_investigation",
  "investigation_id": "uuid",
  "timestamp_utc": "ISO-8601",
  "alert": {
    "source": "datadog|prometheus|cloudwatch",
    "severity": "P1|P2|P3|P4",
    "service": "service-name"
  },
  "timeline": [
    { "timestamp": "ISO-8601", "step": "context_gathering", "duration_sec": 45 }
  ],
  "hypotheses": [
    { "description": "", "confidence": 0.0, "validated": false }
  ],
  "root_cause": {
    "description": "",
    "confidence": 0.0,
    "evidence_refs": []
  },
  "recommendations": [
    { "tier": "L1|L2|L3", "action": "", "confidence": 0.0 }
  ],
  "outcome": "resolved|escalated|monitoring"
}
```

### Retention
- Active investigations: 30 days
- Resolved incidents: 2 years
- Post-mortems: Permanent

---

## Gate Integration

### Investigation to Execution Flow

```
Alert received
  → Start investigation (autonomous)
  → Gather evidence (autonomous)
  → Identify root cause (autonomous)
  → Generate recommendations (autonomous)
  → Evaluate tier
    → L1 + dev/staging → Warden threshold → Execute if allowed
    → L2 → Reuben approval → Execute if approved
    → L3 → Reuben + RPBx → Execute if consensus
    → Production → Human execution (Triage monitors)
```

### Escalation Triggers

| Condition | Automatic Action |
|-----------|------------------|
| Investigation > 10 min | Escalate to on-call with partial findings |
| Confidence < 0.85 | Escalate with hypotheses and gaps |
| Blast radius unclear | Escalate, don't guess |
| Cascade failure detected | Emergency escalation + Warden containment |

---

## Failure Containment

### Auto-Demotion Triggers

| Condition | Warden Action | Triage Response |
|-----------|---------------|-----------------|
| False positive > 10% | Demote to `co-pilot` | Human validation required |
| Wrong remediation executed | Demote to `locked` | Investigation + retraining |
| Missed critical incident | Demote to `supervised` | Human review of all alerts |
| Investigation timeout pattern | Demote to `co-pilot` | Simplified heuristics |

### Circuit Breaker Scenarios

**Scenario A: Investigation Overload**
- Condition: Alert flood exceeds processing capacity
- Response: Prioritize P1/P2, queue P3/P4, scale horizontally if possible

**Scenario B: Cascade Detection**
- Condition: Multiple services failing simultaneously
- Response: Escalate immediately, initiate incident command

---

## Escalation Pathways

```
Triage detects issue:
  ├── Investigation stalled ───────────→ Relay → on-call
  ├── Confidence insufficient ─────────→ Relay → on-call
  ├── L3 recommendation ───────────────→ Reuben + RPBx
  ├── Cascade failure ─────────────────→ Warden + emergency
  └── Novel pattern ───────────────────→ Scribe → runbook update
```

---

## Version History

| Version | Date | Changes | Approved By |
|---------|------|---------|-------------|
| 0.0.1 | 2026-02-06 | Initial autonomy definition | [Pending] |

---

**Governance Note:** Modifications require Reuben approval and version increment.
