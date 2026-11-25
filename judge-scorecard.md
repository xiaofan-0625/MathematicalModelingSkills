# Judge-Style Scorecard

This is an internal 100-point diagnostic for prioritizing repairs. Official criteria and disqualifying rules always override it. It does not predict an award or replace an actual judge.

## Hard gates

Evaluate before adding scores:

| Gate | Default consequence | Examples |
|---|---:|---|
| Integrity | invalid diagnostic result | fabricated data/citation/run, plagiarism, concealed manipulation |
| Official-rule compliance | invalid until fixed | identity leakage, prohibited format, missing required declaration |
| Core task completion | cap 59 | a required subproblem or mandated output is not answered |
| Numerical traceability | cap 69 | headline results cannot be traced to data and code |

Use `pass`, `fail`, or `unknown`. `unknown` does not trigger a favorable assumption; it keeps the score provisional. Change default caps only when competition-specific evidence justifies it, and record the change.

## Dimensions

| Key | Weight | What earns credit |
|---|---:|---|
| `problem_understanding` | 10 | correct decomposition, constraints, deliverables, ambiguity handling |
| `data_evidence` | 12 | data contract, cleaning trace, source quality, verified citations |
| `model_formulation` | 18 | justified assumptions, coherent equations, units, interfaces, appropriate complexity |
| `solving_correctness` | 15 | implementation fidelity, feasibility, diagnostics, solver-claim discipline |
| `validation_robustness` | 15 | legal baselines, uncertainty, sensitivity, failure tests, reversal conditions |
| `results_interpretation` | 10 | direct answers, quantitative insight, boundaries, practical meaning |
| `paper_visuals` | 12 | clear structure, readable evidence figures, consistent notation and references |
| `reproducibility_delivery` | 8 | frozen results, clean rerun, manifest, compliant package |

The weights total 100. Award partial points only for observable evidence. For every dimension record score, at least one evidence location or a reason it is unassessed, deductions, confidence (`high`, `medium`, `low`), and next-point action.

## Specialized failure checks

Apply only when the corresponding structure is present:

- external data: unofficial source used when an authoritative source exists, missing raw snapshot or query, unrecorded vintage/revision, incomplete pagination, silent schema drift, licence conflict, join multiplication, or future leakage;
- experimental design: undefined estimand or experimental unit, pseudoreplication, confounded assignment/run order, ignored blocking or clustering, power based on an unjustified effect, observed post-hoc power, unplanned stopping, or analysis that omits the design structure;
- claim integrity: phantom result files, metric-key mismatch, best-seed cherry-picking, aggregation or denominator errors, incompatible configurations, self-normalized scores, hidden failed runs, or scope language broader than evaluated evidence;
- derivation and proof: undefined symbols or quantifiers, hidden assumptions, invalid theorem conditions, unbounded constant dependence, unsupported limit/integral interchange, numerical checks presented as proof, or paper claims stronger than discharged obligations;
- forecasting: random temporal splits, future-feature leakage, missing legal baseline, or untested interval coverage;
- simulation: one-run inference, correlated entities treated as replications, no convergence evidence, or unsupported input distributions;
- spatial: missing or guessed CRS, angular distance/area arithmetic, uncontrolled join multiplication, or random validation with spatial leakage;
- network: undefined node/edge semantics, cost-strength confusion, unstable community claims, or centrality interpreted causally;
- tables: manually transcribed numbers, hidden units, undefined `±`, false best-result highlighting, or mismatch with frozen results;
- claimed contribution: no one-to-one mapping from the stated innovation to a method component and an isolating experiment, proof, ablation, or failure test;
- AI use: missing required declaration, a disclosure inconsistent with the work ledger, or an unverified AI-generated claim retained as evidence.

Treat an issue as a blocker when it violates an official rule or invalidates a central result; otherwise score it in the most directly affected dimension without double-counting the same defect.

## Severity and repair priority

- **Blocker:** integrity, official-rule, missing-task, or invalid-result failure.
- **Major:** likely changes a central conclusion or loses substantial points.
- **Moderate:** weakens trust, clarity, or completeness but does not overturn the core result.
- **Minor:** local presentation or polish issue.

Order repairs by dependency first, then expected score recovery divided by credible repair effort. Fix upstream correctness before style. Keep an issue open until evidence verifies the repair; do not close it because prose was rewritten.

## Scoring input

Save a JSON input for `scripts/score_project.py`:

```json
{
  "project": "example",
  "rubric_version": "mathskills-4.6",
  "hard_gates": {
    "integrity": {"status": "pass", "evidence": ["求解/reproducibility_report.md"]},
    "official_rule_compliance": {"status": "unknown", "evidence": []},
    "core_task_completion": {"status": "pass", "evidence": ["论文/论文.pdf#p2"]},
    "numerical_traceability": {"status": "pass", "evidence": ["求解/artifact_manifest.json"]}
  },
  "criteria": {
    "problem_understanding": {
      "score": 8,
      "evidence": ["求解/计划/problem_contract.md"],
      "deductions": ["one medium-risk ambiguity remains"],
      "confidence": "high",
      "next_action": "resolve A-03"
    }
  }
}
```

Include all eight criteria for a complete score. Missing or evidence-free criteria remain unassessed. The helper returns verified subtotal, possible range, hard-gate cap, final diagnostic score only when complete, and validation errors; it does not generate evidence.
