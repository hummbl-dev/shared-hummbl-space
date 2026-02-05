#!/usr/bin/env python3
"""Quick helper to display agent/team info from registries/agents.json."""
import argparse
import json
import pathlib
import sys
from typing import Dict, Any


ROOT = pathlib.Path(__file__).resolve().parent.parent
REGISTRY_PATH = ROOT / "registries" / "agents.json"


def load_agents() -> Dict[str, Dict[str, Any]]:
    data = json.loads(REGISTRY_PATH.read_text())
    return {entry["callsign"]: entry for entry in data.get("agents", [])}


def format_text(agent: Dict[str, Any]) -> str:
    artifacts = agent.get("artifacts", [])
    artifact_lines = "\n    - " + "\n    - ".join(artifacts) if artifacts else " none"
    return (
        f"Callsign : {agent['callsign']}\n"
        f"Name     : {agent['name']} {agent.get('emoji', '')}\n"
        f"Type     : {agent.get('type', 'agent')}\n"
        f"Status   : {agent.get('status', 'unknown')}\n"
        f"Home     : {agent.get('home')}\n"
        f"Summary  : {agent.get('summary')}\n"
        f"Artifacts:{artifact_lines}\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Lookup HUMMBL agents by callsign")
    parser.add_argument("callsign", nargs="?", help="Agent or team callsign (slug)")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON instead of human-readable text",
    )
    args = parser.parse_args()

    agents = load_agents()
    if not args.callsign:
        slugs = ", ".join(sorted(agents))
        print("Available callsigns:\n" + slugs)
        return 0

    agent = agents.get(args.callsign)
    if not agent:
        print(f"Unknown callsign: {args.callsign}", file=sys.stderr)
        return 1

    if args.json:
        json.dump(agent, sys.stdout, indent=2, ensure_ascii=False)
        print()
    else:
        print(format_text(agent))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
