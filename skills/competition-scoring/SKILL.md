---
name: competition-scoring
description: Score a mathematical-modeling project with an evidence-linked 100-point rubric, hard gates, confidence levels, and prioritized repairs. Use for judge-style review, pre-submission triage, or rescoring after revisions; it does not predict an official award.
---

# Score Like a Competition Judge

Score observable evidence, not effort, fluency, or model complexity. Keep official rules above the generic rubric and label the result as an internal diagnostic rather than an award prediction.

## Workflow

1. Establish review scope, competition rules, available artifacts, and missing material. Record whether code was run, PDF pages were visually inspected, and citations were verified.
2. Evaluate hard gates first: integrity, official-rule compliance, core task completion, and numerical traceability. A failure can invalidate or cap the diagnostic score.
3. Trace every claimed contribution through a complete chain: 题目要求或研究缺口 → contribution claim → method component → isolating validation, ablation, proof, or failure test → frozen result → paper statement. If a claimed innovation has no isolating evidence, score the observable method and result without crediting the unsupported attribution.
4. Audit claim integrity before awarding credit: evidence-file existence, metric and aggregation match, seed/run count, comparison fairness, uncertainty, scope language, and any mathematical proof obligation. A present number is not automatically a supported interpretation.
5. Score each rubric dimension with evidence locations, deductions, confidence, and the change needed to earn the next point. Anchor findings to a page, section, formula, figure, table, code path, or exact phrase when useful. Missing evidence remains unassessed; do not infer a favorable score.
6. Separate correctness risk from presentation polish. Rank issues by severity, probability, score impact, repair cost, and dependency. Do not inflate issue counts by splitting one root cause into many minor findings.
7. Produce `求解/scorecard.json` and `求解/scorecard.md`. Use `scripts/score_project.py` to validate arithmetic and completeness.
8. After revision, retest hard gates and rescore only affected dimensions while preserving the before/after evidence trail.

Every deduction must point to an owning stage and repair Skill. A scorecard issue that implies a
model, data, validation, claim, or delivery defect opens a rework event rather than being fixed only
inside the scorecard. Close the issue only after the owner reruns its gate and the score is recomputed
against the new revision.

Read [judge-scorecard.md](../../references/judge-scorecard.md) for weights, evidence standards, caps, and the machine-readable input schema.

Use [claim-evidence-integrity.md](../../references/claim-evidence-integrity.md) when a claimed result, comparison or scope cannot be accepted from the paper wording alone.
