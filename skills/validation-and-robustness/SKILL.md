---
name: validation-and-robustness
description: Design and run evidence-backed validation, sensitivity, ablation, uncertainty, and stress tests for mathematical-modeling solutions. Use after a candidate model exists and before results are frozen; do not add tests merely to select a favorable result.
---

# Validate and Stress-Test a Model

Validation is a decision gate, not a collection of impressive metrics. Match tests to the model's purpose, data structure, constraints, and claimed use.

This Skill starts after a candidate model or executed study exists. For prospective randomization, blocking, factorial layout, sample-size/power planning, estimands, and pre-specified inference, use `experimental-design-and-inference`; do not redesign an experiment after seeing results and call the change validation.

## Workflow

1. Define the target of validation: prediction, ranking, optimization feasibility, explanation, simulation behavior, or decision quality.
2. Establish a simple baseline and a fixed evaluation protocol before comparing complex candidates. Use the same split, units, and scoring rules when comparison is intended.
3. Select tests appropriate to the problem: holdout or time-block validation, cross-validation, bootstrap uncertainty, residual and calibration checks, conservation or bound checks, perturbation sensitivity, ablation, placebo, or alternative parameterization.
4. Run at least one failure-oriented test that could change the recommendation. Record every attempted test, including null or failed checks.
5. Compare performance, uncertainty, stability, interpretability, computational cost, and physical or domain feasibility. Do not rank methods by one metric alone.
6. Freeze the accepted outputs only after the validation record is complete. Save machine-readable values and the code or command that produced each table and figure.

If a validation, baseline, stress test, or ablation invalidates the selected model, do not merely
edit the conclusion. Open a rework event, route to the earliest affected G2 or G3 decision, mark
the old frozen values and downstream prose as superseded, and rerun validation after the repair.
If a test is added after seeing results, record it as exploratory unless the experiment contract is
reopened and the change is explicitly marked.

## Evaluation-integrity checks

When results will support a paper claim, also verify ground-truth provenance, metric definitions and denominators, result-file existence, executed metric paths, aggregation across seeds/folds/instances, configuration comparability, failed-run handling, and whether scope language matches the evaluated datasets or scenarios. A candidate's own extrema or output statistics must not be used to manufacture a favorable normalized score unless the task externally defines that metric.

For learned models, inspect training and validation curves, leakage boundaries, convergence or divergence, gradient or parameter pathologies when observable, checkpoint selection, early stopping, class imbalance, calibration, and sensitivity to seed and preprocessing. Training loss alone is not evidence of generalization.

## Anti-cherry-picking rules

- Do not change the split, metric, preprocessing, seed, sample, or constraints after seeing a result without logging the change and labelling the analysis exploratory.
- Do not discard an inconvenient seed, ablation, or sensitivity result. Explain why a run failed or why a method was rejected.
- Thresholds must be justified by the task, a domain constraint, a pre-specified plan, or a clearly labelled exploratory convention.
- Statistical significance is not a substitute for practical effect size, uncertainty, or feasibility.

## Required outputs

For each subproblem write `求解/问题X/结果/validation_report.md` and `robustness_results.csv` (or an equivalent machine-readable file). Include the baseline, evaluation protocol, metrics and units, uncertainty or repeated-run summary, sensitivity range, failed checks, accepted model, and reversal conditions. Update `求解/问题X/结果/frozen_numbers.json` only after the gate passes.

Read [references/validation-matrix.md](../../references/validation-matrix.md) for test selection and the minimum report schema.

Before promoting headline claims, read [claim-evidence-integrity.md](../../references/claim-evidence-integrity.md) and classify each as supported, qualified, unsupported, or unresolved.
