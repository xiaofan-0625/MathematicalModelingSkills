#!/usr/bin/env python3
"""Record a material change and mark its downstream Skill work as stale."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def update_scalar(text: str, key: str, value: str) -> str:
    lines = text.splitlines()
    replacement = f"{key}: {value}"
    for index, line in enumerate(lines):
        if line.startswith(f"{key}:"):
            lines[index] = replacement
            return "\n".join(lines) + "\n"
    lines.append(replacement)
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="mathskills project root")
    parser.add_argument("--trigger", required=True, help="short reason for the material change")
    parser.add_argument("--changed-path", action="append", required=True, dest="changed_paths")
    parser.add_argument("--earliest-gate", required=True, choices=("G0", "G1", "G1.5", "G2", "G3", "G3.5", "G4", "G5", "G6", "G7"))
    parser.add_argument("--invalidated-gate", action="append", required=True, dest="invalidated_gates")
    parser.add_argument("--replay-skill", action="append", required=True, dest="replay_skills")
    parser.add_argument("--root-cause", default="")
    parser.add_argument("--decision", default="")
    parser.add_argument("--approval-required", action="store_true")
    args = parser.parse_args()

    root = args.root.resolve()
    state_path = root / "求解" / "project_state.yaml"
    ledger_path = root / "求解" / "计划" / "skill_use_ledger.json"
    log_path = root / "求解" / "计划" / "rework_log.jsonl"
    for path in (state_path, ledger_path, log_path):
        if not path.is_file():
            raise SystemExit(f"ERROR missing required control file: {path}")

    ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    current_revision = int(ledger.get("revision", 0))
    revision = current_revision + 1
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    event = {
        "event_type": "rework",
        "revision": revision,
        "timestamp": now,
        "trigger": args.trigger,
        "changed_paths": args.changed_paths,
        "root_cause": args.root_cause,
        "earliest_affected_gate": args.earliest_gate,
        "invalidated_gates": args.invalidated_gates,
        "invalidated_artifacts": [],
        "replay_skills": args.replay_skills,
        "decision": args.decision,
        "approval_required": bool(args.approval_required),
        "status": "open",
    }

    with log_path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(event, ensure_ascii=False) + "\n")

    for record in ledger.get("records", []):
        if record.get("name") in set(args.replay_skills):
            record["status"] = "superseded"
            record["last_revision"] = revision
            affected = {args.earliest_gate, *args.invalidated_gates}
            stage_status = record.setdefault("stage_status", {})
            for stage in record.get("planned_stages", []):
                if stage in affected:
                    stage_status[stage] = "superseded"
            record.setdefault("invocations", []).append({"revision": revision, "status": "required"})
    ledger["revision"] = revision
    ledger_path.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    state_text = state_path.read_text(encoding="utf-8")
    state_text = update_scalar(state_text, "revision", str(revision))
    state_text = update_scalar(state_text, "last_rework_event", json.dumps(str(revision), ensure_ascii=False))
    state_path.write_text(state_text, encoding="utf-8", newline="\n")
    print(f"RECORDED revision={revision} earliest_gate={args.earliest_gate} status=open")
    print(f"NEXT close the event only after replaying: {', '.join(args.replay_skills)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
