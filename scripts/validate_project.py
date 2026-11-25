#!/usr/bin/env python3
"""Run deterministic, non-destructive structural checks on a mathskills project."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


CANONICAL_SKILLS = {
    "problem-forensics",
    "data-analysis",
    "external-data-acquisition",
    "experimental-design-and-inference",
    "model-deliberation",
    "model-formulation-and-solving",
    "mathematical-derivation-and-proof",
    "forecasting-and-backtesting",
    "simulation-and-uncertainty",
    "geospatial-modeling",
    "network-modeling",
    "scientific-visualization",
    "technical-diagrams",
    "scientific-tables",
    "academic-writing",
    "academic-humanization",
    "workflow-orchestration",
    "literature-evidence",
    "systematic-evidence-review",
    "exemplar-distillation",
    "validation-and-robustness",
    "reproducibility-audit",
    "national-award-paper-style",
    "measured-experiment-loop",
    "jupyter-live-analysis",
    "sql-data-analysis",
    "academic-translation",
    "research-presentation",
    "plan-and-execution",
    "competition-scoring",
    "submission-packaging",
    "ai-use-disclosure",
}
SKILL_STATUSES = {"pending", "active", "not_applicable", "blocked", "complete", "superseded"}
STAGE_STATUSES = {"pending", "complete", "not_applicable", "superseded"}
REWORK_EVENT_TYPES = {"log_init", "rework", "rework_close"}


STAGES = ("G0", "G1", "G1.5", "G2", "G3", "G3.5", "G4", "G5", "G6", "G7")
REQUIRED_DIRS = (
    "题目",
    "数据",
    "求解",
    "求解/计划",
    "求解/数据审计",
    "求解/证据",
    "求解/实验",
    "论文",
    "提交",
)
REQUIRED_STATE_KEYS = (
    "project_id:",
    "revision:",
    "current_stage:",
    "protected_paths:",
    "open_gates:",
    "next_action:",
    "last_rework_event:",
)
LEDGER_FIELDS = {
    "claim_id",
    "claim_text",
    "claim_type",
    "source_key",
    "source_identifier",
    "access_level",
    "verification_channels",
    "location",
    "scope",
    "verification_status",
    "checked_on",
}


def expected_canonical_skills(root: Path) -> set[str]:
    registry = root / "skills" / "registry.yaml"
    if not registry.is_file():
        return set(CANONICAL_SKILLS)
    names: set[str] = set()
    in_canonical = False
    for line in registry.read_text(encoding="utf-8").splitlines():
        if line == "canonical_skills:":
            in_canonical = True
            continue
        if in_canonical and line and not line.startswith(" "):
            break
        if in_canonical and line.startswith("  ") and not line.startswith("    ") and line.rstrip().endswith(":"):
            names.add(line.strip()[:-1])
    return names or set(CANONICAL_SKILLS)


def check_json(path: Path, label: str, errors: list[str]) -> object | None:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{label}: invalid JSON ({exc})")
        return None
    if not isinstance(value, (dict, list)):
        errors.append(f"{label}: top-level value must be an object or array")
    return value


def validate_skill_ledger(
    root: Path,
    errors: list[str],
    warnings: list[str],
    require_decisions: bool = False,
    target_stage: str | None = None,
) -> None:
    path = root / "求解" / "计划" / "skill_use_ledger.json"
    if not path.is_file():
        errors.append("G0: missing 求解/计划/skill_use_ledger.json")
        return
    value = check_json(path, "求解/计划/skill_use_ledger.json", errors)
    if not isinstance(value, dict):
        return
    records = value.get("records")
    if not isinstance(records, list):
        errors.append("skill ledger: records must be an array")
        return
    expected = expected_canonical_skills(root)
    by_name = {}
    for record in records:
        if not isinstance(record, dict):
            errors.append("skill ledger: every record must be an object")
            continue
        name = record.get("name")
        status = record.get("status")
        if not isinstance(name, str) or name not in expected:
            errors.append(f"skill ledger: unknown or missing Skill name: {name!r}")
        if name in by_name:
            errors.append(f"skill ledger: duplicate Skill: {name}")
        by_name[name] = record
        if status not in SKILL_STATUSES:
            errors.append(f"skill ledger: {name}: invalid status {status!r}")
        if record.get("trigger_checked") is not True:
            message = f"skill ledger: {name}: trigger_checked must be true"
            if require_decisions:
                errors.append(message)
            else:
                warnings.append(message)
        if status in {"active", "complete", "not_applicable", "blocked"}:
            if not isinstance(record.get("reason"), str) or not record.get("reason", "").strip():
                errors.append(f"skill ledger: {name}: status {status} requires a reason")
        if status == "active" and not isinstance(record.get("planned_stages"), list):
            errors.append(f"skill ledger: {name}: active record requires planned_stages")
        if status == "not_applicable" and record.get("trigger_checked") is not True:
            errors.append(f"skill ledger: {name}: not_applicable requires a completed trigger check")
        planned_stages = record.get("planned_stages", [])
        stage_status = record.get("stage_status")
        if not isinstance(stage_status, dict):
            errors.append(f"skill ledger: {name}: stage_status must be an object")
            stage_status = {}
        for planned_stage in planned_stages if isinstance(planned_stages, list) else []:
            if planned_stage not in STAGES:
                errors.append(f"skill ledger: {name}: unknown planned stage {planned_stage!r}")
                continue
            if stage_status.get(planned_stage) not in STAGE_STATUSES:
                errors.append(
                    f"skill ledger: {name}: invalid stage status for {planned_stage}: "
                    f"{stage_status.get(planned_stage)!r}"
                )
        if target_stage in STAGES and status in {"active", "complete", "superseded"}:
            target_index = STAGES.index(target_stage)
            for planned_stage in planned_stages if isinstance(planned_stages, list) else []:
                if STAGES.index(planned_stage) <= target_index and stage_status.get(planned_stage) != "complete":
                    errors.append(
                        f"skill ledger: {name}: {planned_stage} is not complete for --through {target_stage}"
                    )
        if target_stage == "G7" and status == "complete":
            if not isinstance(record.get("invocations"), list) or not record.get("invocations"):
                errors.append(f"skill ledger: {name}: complete Skill requires invocations")
            if not isinstance(record.get("evidence"), list) or not record.get("evidence"):
                errors.append(f"skill ledger: {name}: complete Skill requires evidence")
        if target_stage == "G7" and status == "not_applicable":
            if not isinstance(record.get("evidence"), list) or not record.get("evidence"):
                errors.append(f"skill ledger: {name}: not_applicable requires trigger evidence")
    missing = expected - set(by_name)
    for name in sorted(missing):
        errors.append(f"skill ledger: missing canonical Skill: {name}")
    if value.get("revision") is None:
        errors.append("skill ledger: missing revision")
    statuses = [record.get("status") for record in by_name.values()]
    if any(status in {"pending", "blocked", "superseded"} for status in statuses):
        message = "skill ledger still has pending, blocked, or superseded records"
        if require_decisions:
            errors.append(message)
        else:
            warnings.append(message)


def validate_revision_alignment(root: Path, errors: list[str], warnings: list[str]) -> None:
    state = root / "求解" / "project_state.yaml"
    ledger = root / "求解" / "计划" / "skill_use_ledger.json"
    if not state.is_file() or not ledger.is_file():
        return
    state_text = state.read_text(encoding="utf-8")
    state_revision = None
    for line in state_text.splitlines():
        if line.startswith("revision:"):
            try:
                state_revision = int(line.split(":", 1)[1].strip())
            except ValueError:
                errors.append("project state revision must be an integer")
            break
    try:
        ledger_revision = json.loads(ledger.read_text(encoding="utf-8")).get("revision")
    except Exception:
        return
    if state_revision is not None and ledger_revision != state_revision:
        errors.append(f"revision mismatch: project_state={state_revision} skill_ledger={ledger_revision}")


def validate_rework_log(root: Path, errors: list[str], warnings: list[str]) -> None:
    path = root / "求解" / "计划" / "rework_log.jsonl"
    if not path.is_file():
        errors.append("G0: missing 求解/计划/rework_log.jsonl")
        return
    try:
        lines = [line for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
        if not lines:
            errors.append("rework log: file is empty")
            return
        revisions = []
        open_revisions = set()
        for index, line in enumerate(lines, start=1):
            event = json.loads(line)
            if not isinstance(event, dict):
                errors.append(f"rework log line {index}: event must be an object")
                continue
            event_type = event.get("event_type")
            if event_type not in REWORK_EVENT_TYPES:
                errors.append(f"rework log line {index}: invalid event_type {event_type!r}")
            revision = event.get("revision")
            if not isinstance(revision, int) or revision < 0:
                errors.append(f"rework log line {index}: revision must be a non-negative integer")
            else:
                revisions.append(revision)
            if event_type == "rework":
                required = ("timestamp", "trigger", "changed_paths", "earliest_affected_gate", "invalidated_gates", "replay_skills", "status")
                for key in required:
                    if key not in event:
                        errors.append(f"rework log line {index}: missing {key}")
                if event.get("status") == "open":
                    open_revisions.add(revision)
            if event_type == "rework_close":
                required = ("timestamp", "status", "evidence", "result")
                for key in required:
                    if key not in event:
                        errors.append(f"rework log line {index}: missing {key}")
                open_revisions.discard(revision)
        if revisions != sorted(revisions):
            errors.append("rework log: revisions are not monotonic")
        if open_revisions:
            warnings.append(f"rework log has {len(open_revisions)} open event(s)")
    except Exception as exc:
        errors.append(f"rework log unreadable: {exc}")


def need_file(root: Path, relative: str, stage: str, errors: list[str]) -> None:
    if not (root / relative).is_file():
        errors.append(f"{stage}: missing required artifact: {relative}")


def need_glob(
    root: Path, pattern: str, label: str, stage: str, errors: list[str]
) -> list[Path]:
    matches = [path for path in root.glob(pattern) if path.is_file()]
    if not matches:
        errors.append(f"{stage}: missing {label} (expected {pattern})")
    return matches


def validate_through(root: Path, through: str, errors: list[str]) -> None:
    target = STAGES.index(through)
    if target >= STAGES.index("G1"):
        need_file(root, "求解/计划/problem_contract.md", "G1", errors)
        need_file(root, "求解/数据审计/data_audit.md", "G1", errors)
    if target >= STAGES.index("G1.5"):
        need_file(root, "求解/证据/literature_map.md", "G1.5", errors)
        need_file(root, "求解/证据/citation_ledger.csv", "G1.5", errors)
    if target >= STAGES.index("G2"):
        need_file(root, "求解/计划/modeling_blueprint.md", "G2", errors)
    if target >= STAGES.index("G3"):
        need_glob(root, "求解/问题*/code/*", "subproblem code", "G3", errors)
        need_glob(root, "求解/问题*/结果/*", "raw or machine-readable result", "G3", errors)
    if target >= STAGES.index("G3.5"):
        need_glob(root, "求解/问题*/结果/validation_report.md", "validation report", "G3.5", errors)
        need_glob(root, "求解/问题*/结果/frozen_numbers.json", "frozen numbers", "G3.5", errors)
    if target >= STAGES.index("G4"):
        need_glob(root, "论文/*.tex", "paper source", "G4", errors)
    if target >= STAGES.index("G5"):
        need_glob(root, "论文/*.pdf", "compiled paper", "G5", errors)
        need_file(root, "求解/artifact_manifest.json", "G5", errors)
        need_file(root, "求解/reproducibility_report.md", "G5", errors)
    if target >= STAGES.index("G6"):
        need_file(root, "求解/scorecard.json", "G6", errors)
    if target >= STAGES.index("G7"):
        need_file(root, "提交/manifest.json", "G7", errors)
        if not any(path.is_file() and path.name != "manifest.json" for path in (root / "提交").rglob("*")):
            errors.append("G7: submission directory contains no deliverable")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="mathskills project root")
    parser.add_argument("--through", choices=STAGES, help="validate artifacts through this gate")
    parser.add_argument("--strict", action="store_true", help="treat warnings as errors")
    args = parser.parse_args()
    root = args.root.resolve()
    errors: list[str] = []
    warnings: list[str] = []

    for name in REQUIRED_DIRS:
        if not (root / name).is_dir():
            errors.append(f"missing required directory: {name}/")

    state = root / "求解" / "project_state.yaml"
    if not state.is_file():
        errors.append("missing 求解/project_state.yaml (run scripts/init_project.py first)")
    else:
        state_text = state.read_text(encoding="utf-8")
        for key in REQUIRED_STATE_KEYS:
            if key not in state_text:
                errors.append(f"project state missing key: {key}")

    validate_skill_ledger(
        root,
        errors,
        warnings,
        require_decisions=args.through is not None,
        target_stage=args.through,
    )
    validate_rework_log(root, errors, warnings)
    validate_revision_alignment(root, errors, warnings)

    ledgers = [
        path
        for path in (root / "求解" / "证据" / "citation_ledger.csv", root / "求解" / "citation_ledger.csv")
        if path.exists()
    ]
    if ledgers:
        ledger = ledgers[0]
        try:
            with ledger.open(newline="", encoding="utf-8-sig") as handle:
                fields = set(next(csv.reader(handle), []))
            missing = LEDGER_FIELDS - fields
            if missing:
                errors.append(f"citation ledger missing fields: {sorted(missing)}")
        except Exception as exc:
            errors.append(f"citation ledger unreadable: {exc}")
    else:
        warnings.append("citation ledger not created yet")

    json_files = [root / "求解" / "artifact_manifest.json", root / "求解" / "scorecard.json", root / "提交" / "manifest.json"]
    json_files.extend((root / "求解").glob("问题*/结果/frozen_numbers.json"))
    for path in json_files:
        if path.exists():
            check_json(path, str(path.relative_to(root)), errors)

    if not list((root / "求解").glob("问题*/结果/frozen_numbers.json")):
        warnings.append("no frozen_numbers.json found yet")

    protected_control_names = {
        "project_state.yaml",
        "artifact_manifest.json",
        "scorecard.json",
        "frozen_numbers.json",
    }
    for path in (root / "题目", root / "数据"):
        if path.is_dir():
            generated = [
                item for item in path.rglob("*")
                if item.is_file() and item.name in protected_control_names
            ]
            if generated:
                errors.append(f"generated control files found under protected input: {path}")

    if args.through:
        validate_through(root, args.through, errors)

    if args.strict and warnings:
        errors.extend(f"strict warning: {warning}" for warning in warnings)
    if args.through == "G7":
        delivery_warnings = [
            warning
            for warning in warnings
            if "skill ledger" in warning or "rework log" in warning
        ]
        errors.extend(f"G7 control warning: {warning}" for warning in delivery_warnings)

    for warning in warnings:
        print(f"WARN {warning}")
    for error in errors:
        print(f"ERROR {error}")
    if errors:
        print(f"FAIL errors={len(errors)} warnings={len(warnings)}")
        return 1
    print(f"PASS errors=0 warnings={len(warnings)} through={args.through or 'structure'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
