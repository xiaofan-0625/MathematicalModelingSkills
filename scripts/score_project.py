#!/usr/bin/env python3
"""Validate an evidence-backed competition scorecard and calculate its range."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


WEIGHTS = {
    "problem_understanding": 10,
    "data_evidence": 12,
    "model_formulation": 18,
    "solving_correctness": 15,
    "validation_robustness": 15,
    "results_interpretation": 10,
    "paper_visuals": 12,
    "reproducibility_delivery": 8,
}
GATE_RULES = {
    "integrity": {"cap": 0, "invalid": True},
    "official_rule_compliance": {"cap": 0, "invalid": True},
    "core_task_completion": {"cap": 59, "invalid": False},
    "numerical_traceability": {"cap": 69, "invalid": False},
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="score evidence JSON")
    parser.add_argument("output", type=Path, help="calculated scorecard JSON")
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
    try:
        source = json.loads(args.input.read_text(encoding="utf-8"))
    except Exception as exc:
        raise SystemExit(f"ERROR cannot read input JSON: {exc}")
    if not isinstance(source, dict):
        raise SystemExit("ERROR score input must be a JSON object")

    criteria = source.get("criteria", {})
    gates = source.get("hard_gates", {})
    if not isinstance(criteria, dict) or not isinstance(gates, dict):
        raise SystemExit("ERROR criteria and hard_gates must be JSON objects")

    subtotal = 0.0
    unassessed_weight = 0
    assessed: dict[str, object] = {}
    for key, weight in WEIGHTS.items():
        item = criteria.get(key)
        if not isinstance(item, dict):
            unassessed_weight += weight
            warnings.append(f"unassessed criterion: {key}")
            continue
        score = item.get("score")
        evidence = item.get("evidence")
        if not isinstance(score, (int, float)) or isinstance(score, bool):
            errors.append(f"{key}: score must be numeric")
            unassessed_weight += weight
            continue
        if score < 0 or score > weight:
            errors.append(f"{key}: score {score} outside 0..{weight}")
            unassessed_weight += weight
            continue
        if not isinstance(evidence, list) or not evidence or not all(isinstance(value, str) and value.strip() for value in evidence):
            errors.append(f"{key}: assessed score requires non-empty evidence locations")
            unassessed_weight += weight
            continue
        confidence = item.get("confidence")
        if confidence not in {"high", "medium", "low"}:
            errors.append(f"{key}: confidence must be high, medium, or low")
        subtotal += float(score)
        assessed[key] = item

    cap = 100
    invalid = False
    gate_results: dict[str, object] = {}
    unknown_gates: list[str] = []
    for key, rule in GATE_RULES.items():
        item = gates.get(key)
        if not isinstance(item, dict):
            unknown_gates.append(key)
            gate_results[key] = {"status": "unknown", "evidence": []}
            continue
        status = item.get("status")
        evidence = item.get("evidence")
        if status not in {"pass", "fail", "unknown"}:
            errors.append(f"{key}: gate status must be pass, fail, or unknown")
            status = "unknown"
        if not isinstance(evidence, list):
            errors.append(f"{key}: gate evidence must be an array")
            evidence = []
        if status != "unknown" and not evidence:
            errors.append(f"{key}: pass/fail gate requires evidence")
        if status == "unknown":
            unknown_gates.append(key)
        if status == "fail":
            cap = min(cap, int(rule["cap"]))
            invalid = invalid or bool(rule["invalid"])
        gate_results[key] = {"status": status, "evidence": evidence}

    complete = not errors and unassessed_weight == 0 and not unknown_gates and not invalid
    capped_subtotal = min(subtotal, cap)
    result = {
        "schema_version": 1,
        "project": source.get("project", ""),
        "rubric_version": source.get("rubric_version", "mathskills-4.6"),
        "weights": WEIGHTS,
        "hard_gates": gate_results,
        "assessed_criteria": assessed,
        "verified_subtotal": round(subtotal, 2),
        "possible_score_range": [round(capped_subtotal, 2), round(min(subtotal + unassessed_weight, cap), 2)],
        "hard_gate_cap": cap,
        "invalid": invalid,
        "complete": complete,
        "final_diagnostic_score": round(capped_subtotal, 2) if complete else None,
        "unknown_gates": unknown_gates,
        "errors": errors,
        "warnings": warnings,
        "source": str(args.input),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"WROTE {args.output}")
    print(f"STATUS complete={complete} subtotal={subtotal:.2f} cap={cap} errors={len(errors)} warnings={len(warnings)}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
