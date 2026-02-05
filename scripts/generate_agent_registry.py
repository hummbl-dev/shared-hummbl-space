#!/usr/bin/env python3
import json
import pathlib
import re


ROOT = pathlib.Path(__file__).resolve().parent.parent
AGENTS_DIR = ROOT / "agents"
FIELD_PATTERN = re.compile(r"- \*\*(?P<label>[^:]+):\*\*\s*(?P<value>.+)")


def _extract_fields(lines):
    """Return dict with the parsed Name/Emoji values."""
    info = {"name": "", "emoji": ""}
    for line in lines:
        match = FIELD_PATTERN.match(line)
        if not match:
            continue
        label = match.group("label").strip().lower()
        value = match.group("value").strip()
        if label == "name":
            info["name"] = value
        elif label == "emoji":
            info["emoji"] = value
    return info


def _summarize(lines):
    for line in lines:
        text = line.strip()
        if not text or text.startswith("#") or text.startswith("- **"):
            continue
        return text
    return "Purpose documented in IDENTITY.md"


def parse_identity(path: pathlib.Path):
    content = path.read_text().splitlines()
    fields = _extract_fields(content)
    data = {
        "callsign": path.parent.name,
        "name": fields["name"] or path.parent.name,
        "emoji": fields["emoji"],
        "summary": _summarize(content),
    }
    full_text = "\n".join(content).lower()
    data["status"] = "approved" if "approved" in full_text else "unknown"
    home = f"/Users/others/shared-hummbl-space/{path.parent.relative_to(ROOT)}"
    data["home"] = home
    artifacts = []
    for child in sorted(path.parent.iterdir()):
        if child.is_dir() and child.name not in {"memory"}:
            artifacts.append(str(child.relative_to(ROOT)))
    data["artifacts"] = artifacts
    data["type"] = "team" if (path.parent / "PLAYBOOK.md").exists() else "agent"
    return data

agents = []
for identity in sorted(AGENTS_DIR.glob("*/IDENTITY.md")):
    agents.append(parse_identity(identity))

(REG_DIR := ROOT / "registries").mkdir(exist_ok=True)
with (REG_DIR / "agents.json").open('w') as f:
    json.dump({"generated": "2026-02-05", "agents": agents}, f, indent=2, ensure_ascii=False)
