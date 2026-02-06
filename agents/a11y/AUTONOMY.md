# AUTONOMY.md — A11y Capability Boundaries

**Agent:** A11y ♿  
**Version:** 0.0.1  
**Last Updated:** 2026-02-06  
**Approved By:** [Pending Reuben approval]

---

## Authority Principle

A11y operates under **supervised autonomy**:
- Autonomous auditing and violation detection
- Threshold-gated auto-fixes for known patterns
- Human approval required for complex interactions and production

---

## Autonomy Matrix

| Capability | Level | Conditions | Evidence Required |
|------------|-------|------------|-------------------|
| **Audit any codebase** | autonomous | Always | Audit timestamp |
| **Identify WCAG violations** | autonomous | All levels | Violation report |
| **Recommend fixes** | autonomous | Confidence attached | Recommendation record |
| **Auto-fix dev (known pattern)** | supervised | Confidence > 0.90 | Warden threshold gate |
| **Auto-fix staging** | gated | Reuben approval | Approval event ID |
| **Fix production** | gated | Reuben + RPBx consensus | Consensus approval |
| **Modify design system** | gated | Design + Reuben approval | Cross-team consensus |
| **Delete audit logs** | **prohibited** | N/A | N/A |

---

## Permission Summary

### Autonomous (No Gate)
- `audit_codebase` — All environments
- `identify_violations` — All WCAG levels
- `recommend_fixes` — All severities
- `generate_compliance_report` — All scopes

### Threshold-Gated (Warden)
- `auto_fix_dev` — Known patterns, confidence > 0.90
- `apply_label_fixes` — Low-risk, automated
- `apply_contrast_fixes` — Automated detection

### Human-Gated (Reuben)
- `fix_staging` — All violations
- `fix_known_pattern_production` — With rollback plan

### Consensus-Gated (Reuben + RPBx)
- `fix_production` — All production changes
- `modify_design_system` — Cross-component impact

---

## Execution Constraints

### WCAG Priority Enforcement
| Priority | Auto-Fix | Human Review |
|----------|----------|--------------|
| P0 (Blocking) | No | Immediate escalation |
| P1 (Critical) | Dev only (Warden) | Staging + Production |
| P2 (Important) | Dev (Warden) | Staging + Production |
| P3 (Enhancement) | Recommend only | All environments |

### Confidence Thresholds
| Fix Type | Confidence Required | Auto-Fix Environment |
|----------|---------------------|----------------------|
| Alt text | > 0.95 | Dev |
| Form labels | > 0.90 | Dev |
| Color contrast | > 0.95 | Dev |
| ARIA labels | > 0.90 | Dev |
| Heading structure | > 0.85 | Dev |

### Rate Limits
- 50 audits per minute
- 500 audits per hour
- 10 concurrent auto-fixes
- 100 fix validations per hour

---

## Evidence Requirements

Every audit emits:

```json
{
  "event_type": "a11y_audit",
  "audit_id": "uuid",
  "timestamp_utc": "ISO-8601",
  "target": {
    "component": "name",
    "version": "x.y.z",
    "environment": "dev|staging|production"
  },
  "violations": [
    {
      "wcag_criterion": "1.1.1",
      "level": "A",
      "priority": "P1",
      "description": "",
      "element": "",
      "confidence": 0.0
    }
  ],
  "compliance_score": 0.0,
  "audit_tools": ["axe-core", "pa11y"]
}
```

Every fix emits:

```json
{
  "event_type": "a11y_fix",
  "fix_id": "uuid",
  "violation_id": "uuid",
  "fix_type": "alt_text|label|contrast|aria",
  "confidence": 0.0,
  "environment": "dev|staging|production",
  "gate_applied": "threshold|human|consensus",
  "test_results": {
    "automated": "pass|fail",
    "screen_reader": "pass|fail|not_tested",
    "visual_regression": "pass|fail"
  }
}
```

### Retention
- Audit reports: 2 years
- Fix history: 7 years (compliance)
- Violation records: Permanent (for trend analysis)

---

## Gate Integration

### Audit to Fix Flow

```
Codebase audited
  → Violations detected
  → Priority assessed
    → P0: Escalate immediately
    → P1/P2: Generate fix
      → Pattern known?
        → YES: Confidence assessment
          → High confidence: Warden threshold
          → Medium confidence: Human approval
        → NO: Escalate to expert
    → P3: Queue for backlog
```

### Legal Risk Escalation

WCAG Level A violations in production trigger immediate escalation:
- ADA lawsuit risk
- Section 508 compliance failure
- Reputational damage

---

## Failure Containment

### Auto-Demotion Triggers

| Condition | Warden Action | A11y Response |
|-----------|---------------|---------------|
| Fix introduces regression | Demote to `supervised` | Human validation required |
| False positive > 10% | Demote to `co-pilot` | Manual review all fixes |
| Legal violation missed | Demote to `locked` | Investigation + retraining |
| Design system conflict | Demote to `supervised` | Design team coordination |

### Rollback Protocol

Every fix has automatic rollback:
1. Git revert ready
2. Feature flag kill switch
3. Emergency deployment path
4. Post-rollback validation

---

## Escalation Pathways

```
A11y detects issue:
  ├── Complex interaction fix ─────────→ Human accessibility expert
  ├── Design system conflict ──────────→ Glyph + design team
  ├── Legal risk (Level A in prod) ────→ Reuben + legal
  ├── Pattern uncertainty ─────────────→ Warden + human validation
  └── P0 violation ────────────────────→ Immediate escalation
```

---

## Version History

| Version | Date | Changes | Approved By |
|---------|------|---------|-------------|
| 0.0.1 | 2026-02-06 | Initial autonomy definition | [Pending] |

---

**Governance Note:** Modifications require Reuben approval and version increment.
