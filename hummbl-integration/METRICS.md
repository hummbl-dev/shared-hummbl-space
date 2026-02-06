# HUMMBL Phase0 Metrics

**Version:** 1.0
**Created:** 2026-02-06
**Status:** Active
**Baseline Reference:** Feb 5, 2026 16:39 UTC

---

## Weekly Active Users (WAU)

### Definition

**WAU (Weekly Active Users)** measures the count of distinct entities that performed at least one qualifying activity within a 7-day rolling window.

### What is a "User"?

For HUMMBL Phase0, a "user" is defined as a **distinct authenticated entity** that interacts with HUMMBL infrastructure. This includes:

| Entity Type | Identification Method | Example |
|-------------|----------------------|---------|
| Human Operator | Unique IP + session pattern | Reuben, Dan |
| AI Agent (Managed) | Agent ID in heartbeat/session | Soma, Echo, Claude Code |
| AI Agent (External) | API key or MCP client ID | Third-party integrations |
| CI/CD System | Service account identifier | GitHub Actions runner |

**Exclusions:**
- Health check probes (automated `/health` requests without session context)
- Internal monitoring (Cloudflare Analytics collection)
- Bot traffic without valid session/API credentials
- Test runs explicitly marked `test: true` or from `localhost`
- Duplicate IPs within same 5-minute window (debounced)

### What is "Active"?

An entity is considered **active** when it performs at least ONE of the following qualifying activities:

| Activity Type | Weight | Data Source | Example |
|---------------|--------|-------------|---------|
| API Request (authenticated) | 1.0 | API KV counters | `POST /v1/tasks/poll` |
| MCP Server Interaction | 1.0 | npm API + session logs | Package download + tool call |
| Agent Heartbeat | 0.5 | `/v1/agents/heartbeat` endpoint | Soma sending heartbeat |
| Transformation Chain Execution | 2.0 | Session tracking JSON | P1-CO5-SY4 chain run |
| Git Commit to HUMMBL Repos | 1.0 | GitHub API | Commit to hummbl-agent |
| SITREP Generation | 1.5 | `_state/runs/` artifacts | Daily SITREP created |

**Minimum Threshold:** Weight >= 0.5 to count as active

**Rationale:** Weights reflect engagement depth. Passive downloads count less than active transformation chain executions.

### Measurement Window

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Window Type | 7-day rolling | Industry standard, smooths daily variance |
| Calculation | `T-7d 00:00 UTC` to `T-1d 23:59 UTC` | Full completed days only |
| Update Frequency | Daily at 00:15 UTC | After day boundary, with buffer for late logs |
| Timezone | UTC | Consistent across global operations |

**Calendar Week Option:** For reporting, may also calculate Monday-Sunday totals (ISO 8601 week).

### Data Sources

```
Primary Sources (validated):
├── API KV Counters          → Request counts by endpoint + IP
├── npm API                  → @hummbl/mcp-server download stats
├── Cloudflare Analytics     → Unique IP counts (web dashboard)
└── Session Logs             → _state/runs/YYYY-MM-DD/ artifacts

Secondary Sources (cross-validation):
├── GitHub API               → Commit activity on HUMMBL repos
├── Agent Heartbeat Logs     → /v1/agents/heartbeat responses
└── Transformation Tracking  → hcc-chain-tracking.json records
```

### Calculation Formula

```
WAU = COUNT(DISTINCT user_id WHERE
  SUM(activity_weight) >= 0.5
  AND activity_timestamp BETWEEN (now - 7d) AND now
  AND user_type NOT IN ('health_probe', 'internal_monitor', 'test')
)
```

**Deduplication Rules:**
1. Same IP + User-Agent within 5 minutes = 1 activity
2. Agent heartbeats capped at 1 per hour per agent
3. npm downloads counted once per package version per IP per day

---

## Baseline Snapshot (Feb 5, 2026)

**Captured:** Feb 5, 2026 16:39 UTC
**Purpose:** Phase0 launch readiness validation

| Metric | Value | Source |
|--------|-------|--------|
| MCP Weekly Downloads | 9 | npm API |
| API Daily Requests | 8 | API KV |
| Unique IPs (trailing 24h) | 0* | CF Analytics |
| Agent Heartbeats | N/A | Endpoint not yet active |

*Note: uniqueIPs tracking returned 0 due to bug in initial implementation (flagged for investigation).

---

## Current Snapshot (Feb 6, 2026)

**Captured:** Feb 6, 2026 15:08 UTC
**Status:** Validated

| Metric | Value | Delta from Baseline | Source |
|--------|-------|---------------------|--------|
| MCP Weekly Downloads | 91 | +82 (+911%) | npm API |
| API Total Requests | 337 | +329 | API KV |
| Unique IPs | 5 | +5 | CF Analytics |
| Active Agent Endpoints | 2 | New | Heartbeat + Poll |

**New Endpoints Active:**
- `/v1/tasks/poll` - Agent task polling
- `/v1/agents/heartbeat` - Agent liveness

**Calculated WAU (Feb 6):** 5-7 (estimate pending full activity log correlation)

---

## Validation Approach

### Infrastructure Validation

| Component | Status | Evidence |
|-----------|--------|----------|
| API KV Counters | Validated | Incrementing correctly (Feb 4-6 snapshots) |
| npm API | Validated | Consistent returns, matches dashboard |
| CF Analytics | Validated | Unique IPs now tracking (bug fixed) |
| Session Logging | Validated | Artifacts in `_state/runs/` |

### Methodology Validation

1. **Cross-Source Reconciliation**
   - Compare npm downloads vs MCP tool invocations
   - Match API requests to session logs
   - Correlate unique IPs with known operator locations

2. **Sanity Checks**
   - WAU should be <= Total Unique IPs
   - API requests should show daily patterns (lower on weekends)
   - MCP downloads should spike around releases

3. **Anomaly Detection**
   - Flag WAU changes > 50% week-over-week for review
   - Identify IPs with > 1000 requests/day (potential bot)
   - Alert on zero-activity days for known active agents

### Validation Frequency

| Check | Frequency | Automated |
|-------|-----------|-----------|
| Snapshot capture | Daily 00:15 UTC | Yes |
| Cross-source reconciliation | Weekly | Manual |
| Methodology review | Monthly | Manual |
| Definition review | Quarterly | Manual |

---

## Related Metrics

### Daily Active Users (DAU)

**Definition:** Distinct entities with qualifying activity in trailing 24 hours.

**Formula:** Same as WAU but with 24-hour window.

**Use Case:** Operational health monitoring, incident detection.

### Session Duration

**Definition:** Time between first and last activity in a session.

**Measurement:**
- Agent sessions: First heartbeat to last activity
- Human sessions: First API request to 30-min inactivity

**Current Baseline:** Not yet tracked (Phase1 target)

### Artifacts Produced Per Session

**Definition:** Count of artifacts written to `_state/runs/YYYY-MM-DD/artifacts/` per session.

**Current Baseline (Feb 6):**
- Transformation chain artifacts: 4-6 per session
- SITREP files: 1 per day
- Evidence imports: Variable

### Transformation Chain Completion Rate

**Definition:** Percentage of initiated transformation chains that complete all steps.

**Current Baseline (Feb 6):** 75% (3/4 steps completed in routing test, 1 skipped due to agent timeout)

### MCP Adoption Rate

**Definition:** Weekly downloads / Total potential users (org size estimate)

**Current:** 91 downloads (potential users unknown for Phase0)

---

## Reporting

### Weekly Report Template

```markdown
# HUMMBL WAU Report - Week of YYYY-MM-DD

## Summary
- WAU: [N]
- Delta: [+/-N] ([%] week-over-week)
- Trend: [Increasing/Stable/Declining]

## Breakdown by Entity Type
| Type | Count | % of Total |
|------|-------|------------|
| Human Operators | X | X% |
| AI Agents (Managed) | X | X% |
| AI Agents (External) | X | X% |
| CI/CD Systems | X | X% |

## Notable Events
- [Events affecting metrics]

## Data Quality
- [ ] All sources reporting
- [ ] Cross-validation passed
- [ ] No anomalies detected
```

### Dashboard Location

Primary: Cloudflare Analytics dashboard (hummbl-api worker)
Secondary: `_state/metrics/` local snapshots
Planned: Grafana dashboard (Phase1)

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-02-06 | Initial definition created | Claude Code |
| 2026-02-05 | Baseline snapshot captured | kimi-code |
| 2026-02-04 | WAU infrastructure validated | kimi-code |

---

## Appendix: Decision Rationale

### Why 7-Day Rolling Window?

- **Industry standard:** Aligns with how most SaaS metrics are reported
- **Smoothing:** Reduces impact of daily variance and weekends
- **Actionable:** Long enough to show trends, short enough to react

### Why Include AI Agents as "Users"?

HUMMBL is fundamentally a multi-agent coordination system. Excluding AI agents would:
1. Miss 60-80% of actual system activity
2. Fail to measure agent adoption and health
3. Ignore the core value proposition (agents helping agents)

**Agent activity is first-class usage**, not noise.

### Why Weight Activities Differently?

Not all activities indicate equal engagement:
- A health check is minimal signal
- A transformation chain execution shows deep usage
- Weights allow nuanced understanding of engagement depth

### Why Exclude Test Runs?

Test traffic inflates metrics artificially. Clear separation ensures:
- Production WAU reflects real usage
- Testing can be aggressive without metric pollution
- Anomalies are real signals, not test artifacts

---

## Future Considerations (Phase1+)

1. **Cohort Analysis:** Track WAU by first-active-week to measure retention
2. **Feature-Level DAU:** Which transformations are most used?
3. **Agent Health Score:** Composite of heartbeats, completion rate, artifact quality
4. **Cost Per Active User:** Infrastructure cost / WAU
5. **Network Effects:** Does WAU growth correlate with artifact sharing?
