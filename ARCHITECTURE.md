# Architecture Overview

This document describes the architecture of the shared HUMMBL agent workspace.

## System Purpose

The `shared-hummbl-space` repository serves as a **centralized identity and governance hub** for HUMMBL's multi-agent AI system. It provides:

1. **Shared Identity** - Common agent identity stacks, user profiles, and behavioral contracts
2. **Avatar Assets** - Visual representations and branding for agents
3. **Memory Persistence** - Session logs and long-term knowledge storage
4. **Tooling** - Scripts for workspace management, validation, and automation
5. **Governance** - Operating orders, authority boundaries, and escalation protocols

---

## Core Concepts

### Identity Stack

Every agent (root or individual) has a **5-file identity stack**:

```
┌─────────────────────────────────────────────────────────────┐
│                       IDENTITY STACK                        │
├─────────────────────────────────────────────────────────────┤
│  IDENTITY.md  │  Who the agent is (name, emoji, vibe)       │
│  USER.md      │  Who the human operator is                   │
│  SOUL.md      │  Behavioral contract and boundaries          │
│  AGENT.md     │  Operating orders and workspace facts        │
│  MEMORY.md    │  Long-term persistent knowledge              │
└─────────────────────────────────────────────────────────────┘
```

This stack ensures every agent:
- Knows their identity and role
- Understands the human they serve
- Follows consistent behavioral guidelines
- Has documented operating procedures
- Maintains contextual memory

### Agent Hierarchy

```
                    ┌─────────────────┐
                    │   Codex 🧭      │
                    │  (Root Agent)   │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
   ┌────┴────┐         ┌────┴────┐         ┌────┴────┐
   │Individual│         │  Team   │         │Individual│
   │  Agents  │         │Playbooks│         │  Agents  │
   └────┬────┘         └────┬────┘         └────┬────┘
        │                   │                   │
   Scout, Pulse,      Dialectic,           Halo, Quill,
   Echo, etc.        Pentad, etc.         Matrix, etc.
```

### Team Playbooks

Agents can be organized into teams with shared coordination:

| Team | Purpose | Members |
|------|---------|---------|
| **Dialectic** | Thesis-antithesis-synthesis reasoning | Thesis, Antithesis, Synthesis |
| **Red-Blue-Purple** | Security testing & mediation | Redline, Bluewall, Purplebridge |
| **Pentad** | 5-agent operational core | Atlas, Forge, Vigil, Quorum, Flux |
| **HexaOps** | 6-agent operations team | Prism, Vector, Circuit, Sentinel, Chronos, Nexus |
| **Septet** | 7-agent documentation/governance | Halo, Quill, Matrix, Guardian, Tempo, Relay, Loom |
| **Octave** | 8-agent full-stack ensemble | Beacon, Glyph, Kernel, Orbit, Ember, Harbor, Whisper, Vault |

---

## Directory Architecture

```
shared-hummbl-space/
│
├── Root Identity Stack
│   ├── AGENT.md              # Root operating orders
│   ├── IDENTITY.md           # Codex identity
│   ├── USER.md               # Reuben Bowlby profile
│   ├── SOUL.md               # Root behavioral contract
│   └── README.md             # Project overview
│
├── Agent Onboarding
│   ├── AGENT_BIRTH_PROCESS.md    # Onboarding ritual
│   └── AGENT_BIRTH_LOG_TEMPLATE.md # Birth log format
│
├── agents/                   # Agent directories
│   ├── <agent-name>/
│   │   ├── AGENT.md         # Agent-specific orders
│   │   ├── IDENTITY.md      # Agent identity
│   │   ├── USER.md          # Human profile (may link root)
│   │   ├── SOUL.md          # Agent behavioral contract
│   │   ├── MEMORY.md        # Long-term memory
│   │   ├── memory/          # Daily logs
│   │   │   └── YYYY-MM-DD.md
│   │   └── [work folders]   # Agent-specific work areas
│   │
│   └── <team-name>/
│       ├── PLAYBOOK.md      # Team coordination guide
│       └── [identity files] # Shared team identity
│
├── avatars/                  # Visual assets
│   ├── *-avatar.png         # Color avatars
│   ├── *-avatar-mono.png    # Monochrome variants
│   ├── *-avatar-brief.md    # Design briefs
│   ├── GALLERY.md           # Avatar registry
│   ├── README.md            # Avatar documentation
│   └── generate_compass_avatar.py # Avatar generator
│
├── scripts/                  # Tooling
│   ├── lint_agents.py       # Agent validation
│   ├── check_avatars.py     # Avatar validation
│   ├── link-shared-workspace.sh # Symlink utility
│   ├── generate-avatar.sh   # Generator wrapper
│   ├── hummbl-inventory.sh  # Project inventory
│   └── hummbl-sync.sh       # Cross-device sync
│
└── memory/                   # Root memory store
    └── YYYY-MM-DD.md        # Daily session logs
```

---

## Data Flow

### Session Boot Sequence

```
┌─────────────┐
│ Agent Start │
└──────┬──────┘
       │
       ▼
┌──────────────────────────────────────┐
│ 1. Read IDENTITY.md                  │
│    → Load name, emoji, vibe          │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│ 2. Read USER.md                      │
│    → Load human preferences          │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│ 3. Read SOUL.md                      │
│    → Load behavioral contract        │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│ 4. Read AGENT.md                     │
│    → Load operating orders           │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│ 5. Read MEMORY.md + recent daily     │
│    → Restore context continuity      │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│ 6. Check for SITREPs, TODOs          │
│    → Establish task plan             │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌─────────────┐
│ Ready State │
└─────────────┘
```

### Memory Update Flow

```
┌─────────────────┐     ┌─────────────────────┐
│  Session Work   │────▶│ memory/YYYY-MM-DD.md│
└─────────────────┘     │   (Daily notes)     │
                        └──────────┬──────────┘
                                   │
                                   │ Periodic promotion
                                   ▼
                        ┌─────────────────────┐
                        │     MEMORY.md       │
                        │ (Durable knowledge) │
                        └─────────────────────┘
```

---

## Workspace Linking

The workspace can be linked into other projects using symlinks:

```
Target Project/
├── [project files]
├── agents → shared-hummbl-space/agents
├── avatars → shared-hummbl-space/avatars
├── scripts → shared-hummbl-space/scripts
├── memory → shared-hummbl-space/memory
├── AGENT.md → shared-hummbl-space/AGENT.md
├── IDENTITY.md → shared-hummbl-space/IDENTITY.md
├── USER.md → shared-hummbl-space/USER.md
└── SOUL.md → shared-hummbl-space/SOUL.md
```

This ensures:
- Consistent agent identity across all HUMMBL projects
- Shared memory and context
- Centralized tooling
- Single source of truth for governance

---

## Validation Layer

### Agent Lint (`lint_agents.py`)

Validates:
- Required files present (IDENTITY, USER, SOUL, AGENT, MEMORY)
- Birth log exists and non-empty
- AGENT.md home path correctness
- Referenced folders exist

### Avatar Check (`check_avatars.py`)

Validates:
- All GALLERY.md entries have corresponding files
- PNG headers are valid
- Color and mono variants exist

---

## Governance Model

### Authority Boundaries

```
┌─────────────────────────────────────────────────────────────┐
│                    AUTHORITY LEVELS                         │
├─────────────────────────────────────────────────────────────┤
│  AUTONOMOUS    │  File edits, staging commits, memory       │
│  (Agent can    │  updates, running lint/tests, research     │
│   proceed)     │                                             │
├─────────────────────────────────────────────────────────────┤
│  ESCALATE      │  Git push, publish, destructive commands,  │
│  (Human        │  network calls, cross-repo operations,     │
│   approval)    │  scope changes, credential edits           │
└─────────────────────────────────────────────────────────────┘
```

### Escalation Protocol

1. **Document** - Log the escalation in memory
2. **Evidence** - Provide supporting data
3. **Threshold** - Explain why escalation is needed
4. **Recommendation** - Offer ranked options
5. **Wait** - Do not proceed until human approves

---

## Integration Points

### External References (from AGENT.md)

| Reference | Purpose |
|-----------|---------|
| SITREPs | Situation reports with recommendations |
| Base120 docs | Canonical data framework |
| EXECUTION_AUTHORITY_PROTOCOL | Governance boundaries |
| MACHINE_SCAFFOLDING | Infrastructure documentation |

### Script Toolbelt

| Script | Purpose |
|--------|---------|
| `lint_agents.py` | Validate agent structure |
| `check_avatars.py` | Validate avatar assets |
| `link-shared-workspace.sh` | Create workspace symlinks |
| `generate-avatar.sh` | Generate avatar PNGs |
| `hummbl-inventory.sh` | Generate project inventory |
| `hummbl-sync.sh` | Sync projects across devices |

---

## Future Architecture Considerations

### Proposed Additions

1. **CI/CD Pipeline** - GitHub Actions for automated validation
2. **SITREP Automation** - Script-generated situation reports
3. **Agent Dashboard** - Web interface for status/gallery
4. **Memory Search** - Indexed search across memory files
5. **Event Bus** - Inter-agent communication layer
6. **Metrics Collection** - Track agent activity and outcomes

### Scaling Considerations

- Agent count: Currently 49 agents across 6 teams
- Avatar storage: ~2.5MB per agent (color + mono + SVG)
- Memory growth: Managed via daily files + periodic archival
- Cross-workspace sync: Manual via `hummbl-sync.sh`

---

## Summary

The shared-hummbl-space provides a robust foundation for multi-agent AI operations with:

- **Consistent Identity** via the 5-file identity stack
- **Visual Branding** through procedurally generated avatars
- **Memory Continuity** with daily logs and long-term storage
- **Quality Assurance** via lint and validation scripts
- **Governance Compliance** through documented authority boundaries

This architecture enables HUMMBL agents to operate with shared context, consistent behavior, and traceable decision-making across all projects and workspaces.
