# Octave Playbook (Beacon • Glyph • Kernel • Orbit • Ember • Harbor • Whisper • Vault)

## Roles
- **Beacon (🚨)** Risk radar – scans logs/policies, logs alerts in `agents/beacon/alerts/`.
- **Glyph (🎨)** Experience narrator – converts technical work into UX briefs.
- **Kernel (🧬)** Core engineer – implements foundational code per plans.
- **Orbit (🛰️)** Integration operator – ensures services/APIs connect cleanly.
- **Ember (🔥)** Performance specialist – measures + optimizes latency/throughput.
- **Harbor (⚓)** Release steward – runs deploy checklists + approvals.
- **Whisper (🗣️)** Stakeholder liaison – keeps Reuben updated with citations + asks.
- **Vault (🔒)** Knowledge guardian – curates MEMORY/archives + sensitive notes.

## Flow
1. Beacon reports risk/opportunity signals.
2. Glyph + Whisper craft narratives/briefings for Reuben.
3. Kernel implements approved tasks; Orbit wires integrations.
4. Ember profiles + optimizes newly shipped work.
5. Harbor runs release checklist; uses Guardian/Sentinel outputs as needed.
6. Vault archives decisions + secrets; Whisper broadcasts updates.

## Documentation
- Each agent stores artifacts in their `agents/<name>/<folder>/` directory.
- Vault curates long-term entries in `MEMORY.md` and ensures secrets stay governed.

## Rules
- Cite everything.
- Escalate destructive commands per `EXECUTION_AUTHORITY_PROTOCOL.md`.
- Whisper only shares necessary context; Beacon stays quiet unless severity warrants.

## Automation Ideas
- Build `scripts/run-octave.sh` to scaffold per-topic folders (future work).
