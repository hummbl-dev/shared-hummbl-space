# Contributing to shared-hummbl-space

Welcome to the HUMMBL shared agent workspace! This document provides guidelines for contributing to this repository.

## Table of Contents

- [Getting Started](#getting-started)
- [Repository Structure](#repository-structure)
- [Development Workflow](#development-workflow)
- [Adding a New Agent](#adding-a-new-agent)
- [Working with Avatars](#working-with-avatars)
- [Memory Management](#memory-management)
- [Code Quality](#code-quality)
- [Pull Request Process](#pull-request-process)

---

## Getting Started

### Prerequisites

- Python 3.8+ (for lint scripts and avatar generation)
- Git
- Bash shell (for utility scripts)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/hummbl-dev/shared-hummbl-space.git
   cd shared-hummbl-space
   ```

2. Verify the setup by running health checks:
   ```bash
   python3 scripts/lint_agents.py
   python3 scripts/check_avatars.py
   ```

3. Link to another workspace (optional):
   ```bash
   scripts/link-shared-workspace.sh ~/your/project/path
   ```

---

## Repository Structure

```
shared-hummbl-space/
├── agents/                    # Individual agent directories
│   ├── <agent-name>/
│   │   ├── AGENT.md          # Agent operating orders
│   │   ├── IDENTITY.md       # Agent identity (name, emoji, vibe)
│   │   ├── USER.md           # Human operator profile
│   │   ├── SOUL.md           # Behavioral contract
│   │   ├── MEMORY.md         # Long-term memory
│   │   └── memory/           # Daily memory files
│   └── <team-name>/
│       └── PLAYBOOK.md       # Team coordination guide
├── avatars/                   # Visual assets
│   ├── <agent>-avatar.png    # Color avatar
│   ├── <agent>-avatar-mono.png # Monochrome variant
│   ├── <agent>-avatar-brief.md # Design brief
│   ├── GALLERY.md            # Avatar registry
│   └── generate_compass_avatar.py # Generator script
├── scripts/                   # Tooling
│   ├── lint_agents.py        # Agent validation
│   ├── check_avatars.py      # Avatar validation
│   ├── link-shared-workspace.sh # Workspace linker
│   ├── generate-avatar.sh    # Avatar generation wrapper
│   └── hummbl-*.sh           # Various utilities
├── memory/                    # Root memory files
│   └── YYYY-MM-DD.md         # Daily session logs
├── AGENT.md                   # Root agent orders
├── IDENTITY.md                # Root agent identity
├── USER.md                    # Human profile
├── SOUL.md                    # Root behavioral contract
└── README.md                  # Project overview
```

---

## Development Workflow

### Branch Naming

Use descriptive branch names:
- `feature/<description>` - New features
- `fix/<description>` - Bug fixes
- `docs/<description>` - Documentation updates
- `agent/<agent-name>` - Agent-specific changes

### Commit Messages

Follow conventional commit format:
```
<type>(<scope>): <description>

[optional body]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `refactor`: Code refactoring
- `chore`: Maintenance tasks

Examples:
```
feat(agents): add new Catalyst agent identity stack
docs(avatars): update gallery with new approvals
fix(scripts): resolve lint false positives
```

---

## Adding a New Agent

### 1. Follow the Birth Process

Refer to `AGENT_BIRTH_PROCESS.md` for the complete ritual. Key steps:

1. Create agent directory:
   ```bash
   mkdir -p agents/<agent-name>/memory
   ```

2. Create identity stack files:
   - `IDENTITY.md` - Name, creature, vibe, emoji, avatar reference
   - `USER.md` - Copy from root or customize
   - `SOUL.md` - Behavioral contract
   - `AGENT.md` - Operating orders with home path
   - `MEMORY.md` - Initialize empty or with seed knowledge

3. Generate avatar assets:
   ```bash
   scripts/generate-avatar.sh --output avatars/<agent>-avatar.png --mode color
   scripts/generate-avatar.sh --output avatars/<agent>-avatar-mono.png --mode mono
   ```

4. Update `avatars/GALLERY.md` with the new entry

5. Create birth log in `memory/YYYY-MM-DD.md`

### 2. Required Files

Every agent MUST have:
- [ ] `IDENTITY.md`
- [ ] `USER.md`
- [ ] `SOUL.md`
- [ ] `AGENT.md` with correct home path
- [ ] `MEMORY.md`
- [ ] `memory/YYYY-MM-DD.md` birth log
- [ ] Avatar assets (color + mono PNGs)
- [ ] GALLERY.md entry

### 3. Validation

Run lint to verify:
```bash
python3 scripts/lint_agents.py
```

---

## Working with Avatars

### Generating New Avatars

Use the procedural generator:
```bash
# Color variant
python3 avatars/generate_compass_avatar.py \
  --output avatars/<agent>-avatar.png \
  --mode color

# Monochrome variant
python3 avatars/generate_compass_avatar.py \
  --output avatars/<agent>-avatar-mono.png \
  --mode mono
```

### Customizing Appearance

Override colors and geometry:
```bash
python3 avatars/generate_compass_avatar.py \
  --output avatars/my-agent-avatar.png \
  --bg-top #1a2b3c \
  --bg-bottom #05080f \
  --needle-tip #f94c57 \
  --needle-angle 25
```

### Avatar Requirements

1. **Format:** PNG, 512×512 default size
2. **Variants:** Both color and mono required
3. **Naming:** `<agent>-avatar.png`, `<agent>-avatar-mono.png`
4. **Brief:** Create `<agent>-avatar-brief.md` with design rationale
5. **Approval:** Human approval required before service

### Gallery Updates

Update `avatars/GALLERY.md` with:
```markdown
| Agent | Emoji | Primary Asset | Mono Asset | Status | Notes |
| NewAgent | 🔮 | `avatars/newagent-avatar.png` | `avatars/newagent-avatar-mono.png` | Pending approval | Description |
```

---

## Memory Management

### Daily Memory Files

Create/update `memory/YYYY-MM-DD.md`:
- Decisions made
- Blockers encountered
- Follow-ups needed
- Session highlights

### Long-Term Memory

Promote durable facts to `MEMORY.md`:
- Stable configurations
- Learned patterns
- Historical context

### Memory Guidelines

1. Keep daily logs concise and scannable
2. Use bullets over prose
3. Reference file paths and line numbers
4. Tag important decisions with `[DECISION]`
5. Note escalations with `[ESCALATION]`

---

## Code Quality

### Running Checks

Before committing:
```bash
# Validate agent structure
python3 scripts/lint_agents.py

# Validate avatar assets
python3 scripts/check_avatars.py
```

### Script Standards

When adding scripts:
1. Add shebang (`#!/usr/bin/env python3` or `#!/bin/bash`)
2. Include docstring/header comment with usage
3. Use `set -euo pipefail` for bash scripts
4. Handle errors gracefully
5. Document in `TOOLS.md`

---

## Pull Request Process

### Before Submitting

1. [ ] Run `lint_agents.py` - no new issues
2. [ ] Run `check_avatars.py` - all assets valid
3. [ ] Update relevant documentation
4. [ ] Add memory entry if significant change
5. [ ] Update GALLERY.md for avatar changes

### PR Template

```markdown
## Summary
Brief description of changes

## Type
- [ ] Agent addition
- [ ] Avatar update
- [ ] Script/tooling
- [ ] Documentation
- [ ] Bug fix

## Checklist
- [ ] Lint passes
- [ ] Avatar check passes
- [ ] Documentation updated
- [ ] Memory entry added (if applicable)

## Related Issues
Closes #X
```

### Review Process

1. Automated checks run on PR
2. Human review for:
   - Identity stack completeness
   - Avatar approval status
   - Documentation accuracy
   - Governance compliance

---

## Questions?

- Check `AGENT.md` for operating guidelines
- Review `SOUL.md` for behavioral expectations
- Consult `AGENT_BIRTH_PROCESS.md` for onboarding

For workspace-specific questions, reference the relevant SITREP or memory files.
