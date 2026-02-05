#!/usr/bin/env python3
"""Lint agent directories for required files and AGENT.md path references."""
import argparse
import pathlib
import re
from typing import List

ROOT = pathlib.Path(__file__).resolve().parent.parent
AGENTS_DIR = ROOT / "agents"
REQUIRED = ["IDENTITY.md", "USER.md", "SOUL.md", "AGENT.md", "MEMORY.md"]

parser = argparse.ArgumentParser()
parser.add_argument("--date", help="Override birth log date (YYYY-MM-DD)")
args = parser.parse_args()

if args.date:
    birth_log_name = f"memory/{args.date}.md"
else:
    memory_dir = ROOT / "memory"
    candidates = sorted(memory_dir.glob("20*-*-*.md"))
    birth_log_name = pathlib.Path("memory") / candidates[-1].name if candidates else pathlib.Path("memory/2026-02-05.md")

BIRTH_LOG = pathlib.Path(birth_log_name)
pattern = re.compile(r"agents/(?P<name>[\w\-]+)/(?P<folder>[\w\-]+)/")

issues: List[str] = []

for agent_dir in sorted(p for p in AGENTS_DIR.iterdir() if p.is_dir()):
    name = agent_dir.name
    for file_name in REQUIRED:
        path = agent_dir / file_name
        if not path.exists():
            issues.append(f"{name}: missing {file_name}")
    birth = agent_dir / BIRTH_LOG
    if not birth.exists():
        issues.append(f"{name}: missing {BIRTH_LOG}")
    elif birth.stat().st_size == 0:
        issues.append(f"{name}: birth log empty")

    agent_file = agent_dir / "AGENT.md"
    if agent_file.exists():
        home_line = None
        for line in agent_file.read_text().splitlines():
            if "Home:" in line:
                home_line = line.strip()
                break
        expected = f"/Users/others/agents/{name}"
        if home_line and expected not in home_line:
            issues.append(f"{name}: AGENT.md home mismatch ('{home_line}')")
        elif not home_line:
            issues.append(f"{name}: AGENT.md missing Home line")

        text = agent_file.read_text()
        for match in pattern.finditer(text):
            folder = AGENTS_DIR / match.group("name") / match.group("folder")
            if not folder.exists():
                issues.append(f"{name}: referenced folder {folder} missing")

if issues:
    print("Agent lint issues:")
    for item in issues:
        print(f"- {item}")
else:
    print("All agents passed lint checks.")
