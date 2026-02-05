# Tools Reference

This document catalogs all scripts and tooling available in the shared HUMMBL workspace.

---

## Validation Tools

### `scripts/lint_agents.py`

**Purpose:** Validate agent directory structure and file integrity.

**Usage:**
```bash
python3 scripts/lint_agents.py
```

**Checks:**
- Required files present: `IDENTITY.md`, `USER.md`, `SOUL.md`, `AGENT.md`, `MEMORY.md`
- Birth log exists at `memory/2026-02-05.md` and is non-empty
- `AGENT.md` contains correct `Home:` path reference
- Referenced folders in `AGENT.md` actually exist

**Output:** List of issues or "All agents passed lint checks."

---

### `scripts/check_avatars.py`

**Purpose:** Validate avatar assets referenced in `avatars/GALLERY.md`.

**Usage:**
```bash
python3 scripts/check_avatars.py
```

**Checks:**
- All files referenced in GALLERY.md exist
- PNG files have valid headers (`\x89PNG\r\n\x1a\n`)

**Output:** List of issues or "All avatars present with correct headers."

---

## Avatar Generation

### `avatars/generate_compass_avatar.py`

**Purpose:** Procedurally render compass-style avatar PNGs without external dependencies.

**Usage:**
```bash
# Color variant
python3 avatars/generate_compass_avatar.py --output avatars/my-avatar.png --mode color

# Monochrome variant
python3 avatars/generate_compass_avatar.py --output avatars/my-avatar-mono.png --mode mono
```

**Options:**
| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--output` | string | required | Output file path |
| `--size` | int | 512 | Image dimensions (square) |
| `--mode` | choice | color | `color` or `mono` |
| `--needle-angle` | float | 18 | Compass needle angle in degrees |
| `--needle-width` | float | 18 | Needle stroke width |
| `--tip-width` | float | 22 | Arrowhead width |
| `--tail-length` | float | 110 | Tail length |
| `--tail-width` | float | 28 | Tail width |
| `--grid-spacing` | int | 64 | Background grid spacing |
| `--bg-top` | hex | varies | Top gradient color |
| `--bg-bottom` | hex | varies | Bottom gradient color |
| `--grid` | hex | varies | Grid line color |
| `--outer-ring` | hex | varies | Outer circle color |
| `--inner-ring` | hex | varies | Inner circle color |
| `--needle-base` | hex | varies | Needle base color |
| `--needle-tip` | hex | varies | Needle tip color |
| `--tail-cutout` | hex | varies | Tail cutout color |
| `--highlight` | hex | varies | Center highlight color |
| `--grid-alpha` | float | varies | Grid opacity (0-1) |

**Example with custom colors:**
```bash
python3 avatars/generate_compass_avatar.py \
  --output avatars/custom-avatar.png \
  --mode color \
  --bg-top #1a2b3c \
  --bg-bottom #05080f \
  --needle-tip #f94c57 \
  --needle-angle 25
```

---

### `scripts/generate-avatar.sh`

**Purpose:** Convenience wrapper for the Python avatar generator.

**Usage:**
```bash
scripts/generate-avatar.sh --output avatars/<agent>-avatar.png --mode color
scripts/generate-avatar.sh --output avatars/<agent>-avatar-mono.png --mode mono
```

**Notes:** Passes all arguments directly to `generate_compass_avatar.py`.

---

## Workspace Management

### `scripts/link-shared-workspace.sh`

**Purpose:** Create symlinks from another project to this shared workspace.

**Usage:**
```bash
scripts/link-shared-workspace.sh ~/path/to/target/project
```

**Creates symlinks for:**
- `agents/`
- `avatars/`
- `scripts/`
- `memory/`
- `AGENT_BIRTH_PROCESS.md`
- `AGENT_BIRTH_LOG_TEMPLATE.md`
- `AGENT.md`
- `IDENTITY.md`
- `USER.md`
- `SOUL.md`

**Behavior:** Skips items that already exist in the target directory.

---

### `scripts/hummbl-inventory.sh`

**Purpose:** Generate a JSON inventory of HUMMBL projects.

**Usage:**
```bash
scripts/hummbl-inventory.sh > _state/inventory/projects.json
```

**Output format:**
```json
{
  "schema_version": "0.1",
  "host": "<hostname>",
  "generated_at": "<ISO timestamp>",
  "generated_from_cwd": "<current directory>",
  "artifact_suggested_path": "_state/inventory/projects.json",
  "projects": [
    {
      "id": "<project-id>",
      "path": "<absolute path>",
      "type": "repo",
      "role": "<role>",
      "status": "active",
      "exists": true/false,
      "mtime_epoch": <timestamp>,
      "size_bytes": <size>
    }
  ]
}
```

**Notes:**
- Uses a hardcoded allowlist of known HUMMBL projects
- Paths are specific to the original development environment
- Useful for project tracking and synchronization

---

### `scripts/hummbl-sync.sh`

**Purpose:** Sync a project to a remote device (Pixel) for local auditing.

**Usage:**
```bash
scripts/hummbl-sync.sh <project-id>
```

**Requirements:**
- `_state/inventory/projects.json` must exist (from `hummbl-inventory.sh`)
- SSH access configured for `pixel-ai` host
- rsync installed

**Behavior:**
1. Looks up project path from inventory JSON
2. Creates remote directory on Pixel
3. Syncs files (excluding `.git` and `node_modules`)

---

## Pre-Commit Checklist

Run these before committing changes:

```bash
# 1. Validate agent structure
python3 scripts/lint_agents.py

# 2. Validate avatar assets
python3 scripts/check_avatars.py

# 3. Check git status
git status

# 4. Review changes
git diff
```

---

## Adding New Tools

When adding new scripts:

1. **Location:** Place in `scripts/` directory
2. **Shebang:** Include appropriate shebang line
   - Python: `#!/usr/bin/env python3`
   - Bash: `#!/bin/bash` or `#!/usr/bin/env bash`
3. **Options:** Use `set -euo pipefail` for bash scripts
4. **Documentation:** Add usage comment/docstring
5. **Update TOOLS.md:** Document the new tool here

---

## Future Tools (Planned)

| Tool | Purpose | Status |
|------|---------|--------|
| `orchestrate.sh` | Session bootstrap + prompt generation | Referenced, not implemented |
| `run-cmd.sh` | Governed command execution | Referenced, not implemented |
| `generate-sitrep.sh` | SITREP scaffolding | Referenced, not implemented |
| `run-dialectic.sh` | Dialectical trio coordination | Mentioned as idea |
| `memory-archive.sh` | Memory promotion/archival | Not started |

---

## Dependencies

All scripts are designed to run with standard Python 3 and bash without external dependencies:

- **Python 3.8+** - Standard library only
- **Bash** - POSIX-compatible with common utilities (`rsync`, `ssh`, `stat`)
- **Git** - For version control operations

No pip packages or npm modules required.
