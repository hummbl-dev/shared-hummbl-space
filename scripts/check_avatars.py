#!/usr/bin/env python3
"""Validate avatar entries in avatars/GALLERY.md."""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
GALLERY = ROOT / "avatars" / "GALLERY.md"
PNG_HDR = b"\x89PNG\r\n\x1a\n"

issues = []
for line in GALLERY.read_text().splitlines():
    line = line.strip()
    if not line.startswith("|"):
        continue
    parts = [p.strip() for p in line.strip('|').split('|')]
    if len(parts) < 6 or parts[0] == 'Agent':
        continue
    agent, emoji, primary, mono = parts[0], parts[1], parts[2], parts[3]
    for path in (primary, mono):
        path = path.strip('` ')
        if not path or path.startswith('---'):
            continue
        avatar_path = ROOT / path
        if not avatar_path.exists():
            issues.append(f"{agent}: missing {path}")
            continue
        with avatar_path.open('rb') as fh:
            if fh.read(8) != PNG_HDR:
                issues.append(f"{agent}: {path} header invalid")

if issues:
    print("Avatar issues:")
    for item in issues:
        print(f"- {item}")
else:
    print("All avatars present with correct headers.")
