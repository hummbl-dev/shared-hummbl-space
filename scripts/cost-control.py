#!/usr/bin/env python3
"""Cost control enforcement for HUMMBL sessions.

Checks budget thresholds, emits warnings, and handles emergency overrides.
Exit codes: 0=ok, 1=warn, 2=halt
"""
import argparse
import json
import pathlib
import sys
import uuid
from datetime import datetime, timezone
from typing import Optional

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "configs" / "cost-control.json"
SESSION_PATH = ROOT.parent / "hummbl-integration" / "session-tracking.json"


def load_config() -> dict:
    """Load cost control configuration."""
    if not CONFIG_PATH.exists():
        print(f"ERROR: Config not found at {CONFIG_PATH}", file=sys.stderr)
        sys.exit(1)
    return json.loads(CONFIG_PATH.read_text())


def load_session() -> dict:
    """Load current session state."""
    if not SESSION_PATH.exists():
        print(f"ERROR: Session file not found at {SESSION_PATH}", file=sys.stderr)
        sys.exit(1)
    return json.loads(SESSION_PATH.read_text())


def save_session(session: dict) -> None:
    """Save session state."""
    SESSION_PATH.write_text(json.dumps(session, indent=2) + "\n")


def get_threshold_level(percent: float, config: dict) -> tuple[Optional[str], Optional[str]]:
    """Get the highest triggered threshold level and message."""
    triggered_level = None
    triggered_message = None

    for threshold in config["warning_thresholds"]:
        if percent >= threshold["percent"]:
            triggered_level = threshold["level"]
            triggered_message = threshold["message"]

    return triggered_level, triggered_message


def format_message(template: str, current: float, limit: float) -> str:
    """Replace ${current} and ${limit} placeholders in message."""
    return template.replace("${current}", f"${current:.2f}").replace("${limit}", f"${limit:.2f}")


def cmd_init(args) -> int:
    """Initialize a new session with budget tier."""
    config = load_config()

    if args.type not in config["budget_tiers"]:
        print(f"ERROR: Unknown tier '{args.type}'", file=sys.stderr)
        print(f"Valid tiers: {', '.join(config['budget_tiers'].keys())}", file=sys.stderr)
        return 1

    tier = config["budget_tiers"][args.type]

    session = {
        "session_id": str(uuid.uuid4()),
        "session_type": args.type,
        "started_at": datetime.now(timezone.utc).isoformat(),
        "budget": {
            "limit": tier["limit"],
            "warn_at": tier["warn_at"],
            "current": 0.00,
            "warnings_sent": [],
            "emergency_override": None
        },
        "metadata": {
            "runner": args.runner,
            "workspace": str(ROOT.parent),
            "notes": args.notes
        }
    }

    save_session(session)
    print(f"Session initialized: {args.type}")
    print(f"  Budget: ${tier['limit']:.2f} (warn at ${tier['warn_at']:.2f})")
    print(f"  Auto-approve: {tier['auto_approve']}")
    print(f"  Session ID: {session['session_id'][:8]}...")
    return 0


def cmd_add(args) -> int:
    """Add cost to current session."""
    config = load_config()
    session = load_session()

    if session["session_id"] is None:
        print("ERROR: No active session. Run --init first.", file=sys.stderr)
        return 1

    amount = args.add  # --add stores the value in args.add
    old_current = session["budget"]["current"]
    session["budget"]["current"] = round(old_current + amount, 2)

    save_session(session)
    print(f"Added ${amount:.2f} to session")
    print(f"  Previous: ${old_current:.2f}")
    print(f"  Current: ${session['budget']['current']:.2f}")
    print(f"  Limit: ${session['budget']['limit']:.2f}")

    # Check thresholds after adding
    return cmd_check_internal(config, session, emit_new_only=True)


def cmd_check(args) -> int:
    """Check current budget status and emit warnings if needed."""
    config = load_config()
    session = load_session()
    return cmd_check_internal(config, session, emit_new_only=not args.all)


def cmd_check_internal(config: dict, session: dict, emit_new_only: bool = True) -> int:
    """Internal check logic."""
    if session["session_id"] is None:
        print("ERROR: No active session. Run --init first.", file=sys.stderr)
        return 1

    budget = session["budget"]
    current = budget["current"]
    limit = budget["limit"]

    if limit <= 0:
        print("WARNING: Budget limit is zero", file=sys.stderr)
        return 1

    percent = (current / limit) * 100
    level, message = get_threshold_level(percent, config)

    # Check if emergency override is active
    if budget["emergency_override"]:
        print(f"[OVERRIDE ACTIVE] {budget['emergency_override']['reason']}")
        return 0

    exit_code = 0

    if level:
        threshold_key = f"{int(percent // 25) * 25}%"  # Normalize to threshold bucket

        # Find the exact threshold we crossed
        for t in config["warning_thresholds"]:
            if percent >= t["percent"]:
                threshold_key = f"{t['percent']}%"

        already_sent = threshold_key in budget["warnings_sent"]

        if not already_sent or not emit_new_only:
            formatted = format_message(message, current, limit)

            if level == "halt":
                print(f"[HALT] {formatted}")
                exit_code = 2
            elif level == "warn":
                print(f"[WARN] {formatted}")
                exit_code = 1
            else:
                print(f"[INFO] {formatted}")

            # Record warning as sent
            if not already_sent:
                budget["warnings_sent"].append(threshold_key)
                save_session(session)
        else:
            # Already sent this warning
            if level == "halt":
                exit_code = 2
            elif level == "warn":
                exit_code = 1

    return exit_code


def cmd_status(args) -> int:
    """Print current session status."""
    config = load_config()
    session = load_session()

    if session["session_id"] is None:
        print("No active session")
        return 0

    budget = session["budget"]
    current = budget["current"]
    limit = budget["limit"]
    percent = (current / limit) * 100 if limit > 0 else 0

    print(f"Session: {session['session_type']} ({session['session_id'][:8]}...)")
    print(f"Started: {session['started_at']}")
    print(f"Budget: ${current:.2f} / ${limit:.2f} ({percent:.1f}%)")
    print(f"Warnings sent: {', '.join(budget['warnings_sent']) or 'none'}")

    if budget["emergency_override"]:
        override = budget["emergency_override"]
        print(f"OVERRIDE ACTIVE: {override['reason']} at {override['timestamp']}")

    # Show progress bar
    bar_width = 30
    filled = int(bar_width * percent / 100)
    bar = "=" * filled + "-" * (bar_width - filled)
    print(f"[{bar}]")

    return 0


def cmd_override(args) -> int:
    """Log emergency override."""
    config = load_config()
    session = load_session()

    if session["session_id"] is None:
        print("ERROR: No active session. Run --init first.", file=sys.stderr)
        return 1

    valid_reasons = config["emergency_override"]["conditions"]
    if args.reason not in valid_reasons:
        print(f"ERROR: Invalid override reason '{args.reason}'", file=sys.stderr)
        print(f"Valid reasons: {', '.join(valid_reasons)}", file=sys.stderr)
        return 1

    session["budget"]["emergency_override"] = {
        "reason": args.reason,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "notes": args.notes
    }

    save_session(session)
    print(f"Emergency override logged: {args.reason}")
    print("Budget limits suspended for this session")
    return 0


def cmd_reset(args) -> int:
    """Reset session to initial state."""
    session = {
        "session_id": None,
        "session_type": None,
        "started_at": None,
        "budget": {
            "limit": 0.00,
            "warn_at": 0.00,
            "current": 0.00,
            "warnings_sent": [],
            "emergency_override": None
        },
        "metadata": {
            "runner": None,
            "workspace": str(ROOT.parent),
            "notes": None
        }
    }
    save_session(session)
    print("Session reset")
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Cost control enforcement for HUMMBL sessions",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exit codes:
  0 - OK (under budget or info threshold)
  1 - WARN (75 percent threshold crossed)
  2 - HALT (90 percent threshold crossed)

Examples:
  cost-control.py --init routine           # Start routine session ($5 limit)
  cost-control.py --add 0.50               # Add $0.50 to current session
  cost-control.py --check                  # Check budget, emit new warnings
  cost-control.py --status                 # Show session status
  cost-control.py --override production_down  # Emergency override
"""
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--init", dest="type", metavar="TYPE",
                       help="Initialize session (routine|analysis|research|architecture)")
    group.add_argument("--add", type=float, metavar="AMOUNT",
                       help="Add cost to current session")
    group.add_argument("--check", action="store_true",
                       help="Check budget and emit warnings")
    group.add_argument("--status", action="store_true",
                       help="Print session status")
    group.add_argument("--override", dest="override_reason", metavar="REASON",
                       help="Log emergency override")
    group.add_argument("--reset", action="store_true",
                       help="Reset session to initial state")

    # Optional arguments
    parser.add_argument("--runner", help="Runner name for metadata (with --init)")
    parser.add_argument("--notes", help="Notes for session or override")
    parser.add_argument("--all", action="store_true",
                        help="Show all warnings, not just new ones (with --check)")

    args = parser.parse_args()

    if args.type:
        sys.exit(cmd_init(args))
    elif args.add is not None:
        sys.exit(cmd_add(args))
    elif args.check:
        sys.exit(cmd_check(args))
    elif args.status:
        sys.exit(cmd_status(args))
    elif args.override_reason:
        args.reason = args.override_reason
        sys.exit(cmd_override(args))
    elif args.reset:
        sys.exit(cmd_reset(args))


if __name__ == "__main__":
    main()
