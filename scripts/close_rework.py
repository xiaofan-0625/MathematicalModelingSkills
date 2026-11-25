#!/usr/bin/env python3
"""Close a rework revision after replayed Skills and evidence pass."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="mathskills project root")
    parser.add_argument("--revision", type=int, required=True)
    parser.add_argument("--evidence", action="append", required=True, help="project-relative evidence path")
    parser.add_argument("--result", default="replay and affected gates passed")
    args = parser.parse_args()

    root = args.root.resolve()
    ledger_path = root / "求解" / "计划" / "skill_use_ledger.json"
    log_path = root / "求解" / "计划" / "rework_log.jsonl"
    if not ledger_path.is_file() or not log_path.is_file():
        raise SystemExit("ERROR run init_project.py before closing rework")

    evidence = []
    for relative in args.evidence:
        path = (root / relative).resolve()
        try:
            path.relative_to(root)
        except ValueError:
            raise SystemExit(f"ERROR evidence escapes project root: {relative}")
        if not path.exists():
            raise SystemExit(f"ERROR evidence does not exist: {relative}")
        evidence.append(relative.replace("\\", "/"))

    events = [json.loads(line) for line in log_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    opens = [event for event in events if event.get("event_type") == "rework" and event.get("revision") == args.revision]
    closes = [event for event in events if event.get("event_type") == "rework_close" and event.get("revision") == args.revision]
    if len(opens) != 1:
        raise SystemExit(f"ERROR expected one open event for revision {args.revision}")
    if closes:
        raise SystemExit(f"ERROR revision {args.revision} is already closed")

    replay_skills = opens[0].get("replay_skills", [])
    affected_stages = {
        opens[0].get("earliest_affected_gate"),
        *opens[0].get("invalidated_gates", []),
    }
    ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    if ledger.get("revision") != args.revision:
        raise SystemExit(f"ERROR ledger revision {ledger.get('revision')} does not match {args.revision}")
    by_name = {record.get("name"): record for record in ledger.get("records", [])}
    missing = sorted(set(replay_skills) - set(by_name))
    if missing:
        raise SystemExit(f"ERROR unknown replay Skills in event: {missing}")
    for name in replay_skills:
        record = by_name[name]
        stage_status = record.setdefault("stage_status", {})
        completed_stages = []
        for stage in record.get("planned_stages", []):
            if stage in affected_stages:
                stage_status[stage] = "complete"
                completed_stages.append(stage)
        record["status"] = (
            "complete"
            if all(stage_status.get(stage) == "complete" for stage in record.get("planned_stages", []))
            else "active"
        )
        record["last_revision"] = args.revision
        record.setdefault("evidence", []).extend(item for item in evidence if item not in record.get("evidence", []))
        record.setdefault("invocations", []).append({
            "revision": args.revision,
            "status": "passed",
            "stages": completed_stages,
            "evidence": evidence,
        })
    ledger_path.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    close_event = {
        "event_type": "rework_close",
        "revision": args.revision,
        "timestamp": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "status": "closed",
        "evidence": evidence,
        "result": args.result,
    }
    with log_path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(close_event, ensure_ascii=False) + "\n")
    print(f"CLOSED revision={args.revision} replay_skills={len(replay_skills)} evidence={len(evidence)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
