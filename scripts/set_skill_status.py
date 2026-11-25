#!/usr/bin/env python3
"""Set one canonical Skill applicability or completion record in the project ledger."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ALLOWED = {"active", "not_applicable", "blocked", "complete"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="mathskills project root")
    parser.add_argument("skill", help="canonical Skill name")
    parser.add_argument("status", choices=sorted(ALLOWED))
    parser.add_argument("--reason", required=True)
    parser.add_argument("--stage", action="append", dest="stages")
    parser.add_argument("--evidence", action="append", default=[])
    args = parser.parse_args()

    root = args.root.resolve()
    path = root / "求解" / "计划" / "skill_use_ledger.json"
    if not path.is_file():
        raise SystemExit(f"ERROR missing ledger: {path}")
    ledger = json.loads(path.read_text(encoding="utf-8"))
    matches = [record for record in ledger.get("records", []) if record.get("name") == args.skill]
    if len(matches) != 1:
        raise SystemExit(f"ERROR expected one canonical Skill record for {args.skill}")
    record = matches[0]
    checked_evidence = []
    for relative in args.evidence:
        candidate = (root / relative).resolve()
        try:
            candidate.relative_to(root)
        except ValueError:
            raise SystemExit(f"ERROR evidence escapes project root: {relative}")
        if not candidate.exists():
            raise SystemExit(f"ERROR evidence does not exist: {relative}")
        checked_evidence.append(relative.replace("\\", "/"))
    if args.status == "complete" and not checked_evidence:
        raise SystemExit("ERROR complete status requires at least one --evidence path")
    if args.status == "complete" and not args.stages:
        raise SystemExit("ERROR complete status requires at least one --stage")
    if args.status == "not_applicable" and not checked_evidence:
        raise SystemExit("ERROR not_applicable requires trigger-check evidence")

    record["status"] = args.status
    record["trigger_checked"] = True
    record["reason"] = args.reason
    if args.stages:
        if args.status == "active":
            record["planned_stages"] = args.stages
            current = record.setdefault("stage_status", {})
            record["stage_status"] = {
                stage: current.get(stage, "pending") for stage in args.stages
            }
    for item in checked_evidence:
        if item not in record.setdefault("evidence", []):
            record["evidence"].append(item)
    if args.status == "complete":
        planned = set(record.get("planned_stages", []))
        unknown = sorted(set(args.stages) - planned)
        if unknown:
            raise SystemExit(f"ERROR completion stage not planned for {args.skill}: {unknown}")
        stage_status = record.setdefault("stage_status", {})
        for stage in args.stages:
            stage_status[stage] = "complete"
        record.setdefault("invocations", []).append({
            "revision": ledger.get("revision", 0),
            "status": "passed",
            "stages": args.stages,
            "evidence": checked_evidence,
        })
        record["last_revision"] = ledger.get("revision", 0)
        record["status"] = (
            "complete"
            if all(stage_status.get(stage) == "complete" for stage in record.get("planned_stages", []))
            else "active"
        )
    elif args.status == "not_applicable":
        record["stage_status"] = {
            stage: "not_applicable" for stage in record.get("planned_stages", [])
        }
    path.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"UPDATED skill={args.skill} status={args.status} revision={ledger.get('revision', 0)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
