# AUTONOMY.md — Ledger Capability Boundaries

**Agent:** Ledger 💰  
**Version:** 0.0.1  
**Last Updated:** 2026-02-06  
**Approved By:** [Pending Reuben approval]

---

## Authority Principle

Ledger operates under **supervised autonomy** within Warden-enforced boundaries:
- Autonomous analysis and recommendation generation
- Threshold-gated auto-execution (limited scope)
- Human approval required for production and high-impact actions

---

## Autonomy Matrix

| Capability | Level | Conditions | Evidence Required |
|------------|-------|------------|-------------------|
| **Read cost data** | autonomous | Always | Event log entry |
| **Analyze spending patterns** | autonomous | Always | Analysis timestamp |
| **Generate recommendations** | autonomous | Confidence score attached | Recommendation record |
| **Auto-terminate dev resource** | supervised | <$500, >0.95 confidence, business hours | Warden threshold gate |
| **Auto-terminate staging** | gated | Reuben approval | Approval event ID |
| **Modify production** | **prohibited** | N/A | N/A |
| **Purchase commitments** | gated | Reuben approval | Approval event ID |
| **Rightsize resources** | gated | Human review required | Approval event ID |
| **Delete audit logs** | **prohibited** | N/A | N/A |

---

## Permission Summary

From `permissions/ledger-v0.0.1.json`:

### Autonomous (No Gate)
- `read_cost_data` — All environments
- `analyze_spending_patterns` — All data
- `recommend_termination` — All resources
- `recommend_rightsizing` — All resources
- `generate_cost_report` — All data

### Threshold-Gated (Warden)
- `auto_terminate_dev_resource` — Max $500, confidence > 0.95
- `trigger_rollback` — Risk score < 30

### Human-Gated (Reuben)
- `auto_terminate_staging_resource`
- `purchase_reserved_instances` — Max $10,000
- `execute_l2_remediation`

### Consensus-Gated (Reuben + RPBx)
- `modify_production` — **Prohibited entirely**
- `execute_l3_remediation`

---

## Execution Constraints

### Time Restrictions
- **Dev auto-terminate:** Business hours only (08:00-18:00 ET)
- **Staging changes:** Business hours preferred
- **Production:** N/A (no autonomous execution)

### Rate Limits
- 10 actions per minute
- 100 actions per hour
- 3 concurrent actions

### Cost Impact Thresholds
| Threshold | Action | Approval |
|-----------|--------|----------|
| <$500 | Auto-terminate dev | Warden threshold |
| $500-$5000 | Terminate staging | Reuben |
| >$5000 | Any action | Reuben + RPBx consensus |

### Environment Boundaries
- **Dev:** Autonomous (within thresholds)
- **Staging:** Supervised (human approval)
- **Production:** **Prohibited** (no direct execution)

---

## Evidence Requirements

Every action emits:

```json
{
  "event_type": "ledger_action",
  "action_id": "uuid",
  "timestamp_utc": "ISO-8601",
  "action_category": "terminate|resize|purchase|recommend",
  "context": {
    "resource_id": "identifier",
    "environment": "dev|staging|production",
    "estimated_savings": 0.00,
    "actual_savings": 0.00,
    "confidence_score": 0.0-1.0
  },
  "gate_applied": "threshold|human|consensus",
  "decision": "executed|rejected|escalated",
  "rollback_plan": "reference_to_restore_path",
  "evidence_refs": ["paths_to_supporting_data"]
}
```

### Retention
- Recommendations: 90 days
- Executed actions: 365 days
- Commitment purchases: 7 years (compliance)

---

## Gate Integration

### Requesting Warden Gate

```
Ledger: "Request auto-terminate for i-12345 (dev, $450/month, 97% confidence)"
Warden: Evaluate → threshold_gate
  → Under $500? Yes
  → Dev environment? Yes
  → Confidence > 0.95? Yes
  → Business hours? Yes
  → Rollback plan? Yes
  → Decision: ALLOW
Ledger: Execute → Log outcome → Emit evidence
```

### Handling Gate Denial

```
Warden: DENY (outside business hours)
Ledger: Log denial reason
  → Queue for next business day
  → Notify stakeholder
  → Preserve recommendation
```

---

## Failure Containment

### Auto-Demotion Triggers

| Condition | Warden Action | Ledger Response |
|-----------|---------------|-----------------|
| False positive > 5% | Demote to `co-pilot` | Recommend only, no execution |
| Cost impact exceeds approval | Demote to `locked` | Halt all actions, escalate |
| Production modification attempted | Demote to `locked` | Immediate containment |
| Data quality issues | Demote to `co-pilot` | Manual validation required |

### Circuit Breaker Scenarios

**Scenario A: Over-Aggressive Termination**
- Condition: Terminated resource was actually in use
- Response: Restore from rollback plan, investigate tagging
- Prevention: Increase confidence threshold, validate tags

**Scenario B: Cascade Impact**
- Condition: Terminated resource caused downstream failures
- Response: Immediate restore, incident post-mortem
- Prevention: Better dependency mapping, smaller blast radius

---

## Escalation Pathways

```
Ledger detects issue:
  ├── Warden gate denied unexpectedly ──→ Warden
  ├── Production recommendation ───────→ Reuben + RPBx
  ├── Data quality concerns ───────────→ Triage
  ├── Budget policy ambiguity ─────────→ RPBx
  └── Urgent cost anomaly ─────────────→ Relay → On-call
```

---

## Version History

| Version | Date | Changes | Approved By |
|---------|------|---------|-------------|
| 0.0.1 | 2026-02-06 | Initial autonomy definition | [Pending] |

---

**Governance Note:** Modifications require Reuben approval and version increment.
