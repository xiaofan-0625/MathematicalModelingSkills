---
name: experimental-design-and-inference
description: Design prospective, controlled, computational, or simulation experiments and their statistical inference before results are observed. Use for randomization, blocking, factorial designs, sample size, power, causal estimands, repeated measures, or pre-specified analysis; use validation-and-robustness for post-model stress testing.
---

# Design Experiments and Inference

No downstream test can repair a confounded design, pseudoreplication, an undefined estimand, or a stopping rule chosen after the result is known. Design the comparison and its analysis before observing the outcome whenever the project controls data collection, interventions, simulation runs, or algorithm evaluations.

## Design contract

State the decision question, hypothesis, estimand, treatment or controlled factor, outcome, experimental unit, unit of assignment, unit of analysis, measurement schedule, target population, and conditions under which the conclusion may be transported. Distinguish independent units from repeated measurements, subsamples, seeds, epochs, folds, or time points.

Choose the smallest design that identifies the requested effect:

- randomized or blocked comparison for a few treatments;
- stratification when a small number of prognostic factors must be balanced;
- factorial or fractional-factorial design for main effects and interactions, with aliasing and resolution stated;
- response-surface or space-filling design when curvature or an optimum over continuous factors matters;
- crossover, repeated-measures, split-plot, cluster, or nested design when assignment and measurement occur at different levels;
- paired instance/seed comparisons for algorithms and simulations, treating the independent dataset, scenario, or replication as the unit;
- observational causal design only with an explicit identification strategy and challenged assumptions.

## Workflow

1. List nuisance factors such as site, batch, day, operator, plate position, dataset difficulty, scenario, or hardware. Decide which are blocked, stratified, randomized across, modeled, or held fixed.
2. Define controls, comparator, run order, allocation ratio, blinding or masking where relevant, washout and carry-over handling, and contamination risks.
3. Generate and archive a seeded allocation or run schedule. Keep treatment assignment concealed when the design requires it; record deviations without rewriting the original schedule.
4. Plan sample size from a smallest effect of practical interest or a justified range. Report alpha, target power, sidedness, allocation, attrition, clustering, multiple comparisons, assumptions, and sensitivity of required sample size. Do not use observed post-hoc power as evidence.
5. Pre-specify the analysis that matches the design: contrasts, model terms, blocks, strata, clusters, repeated measures, covariates, missing-data handling, exclusions, multiplicity control, uncertainty intervals, and effect-size reporting.
6. Separate confirmatory outcomes and analyses from exploratory ones. Predeclare interim looks, stopping rules, adaptive changes, and how type-I error or decision risk is controlled.
7. For observational inference, state the causal contrast, timing, confounder set, positivity and consistency assumptions, interference boundary, and negative-control or sensitivity plan. Do not convert association into causation through wording.
8. Before execution, test the schedule and analysis on synthetic or pilot-shaped data. Confirm that all planned effects are estimable and that the independent-replication count is correct.
9. After execution, preserve deviations, exclusions, failed runs, and the realized sample structure. Hand the results to `validation-and-robustness` without changing the design to favor the observed outcome.

## Anti-pseudoreplication rules

- The independent sample size is determined by the level of assignment or independent generation, not by the number of cells, images, repeated readings, folds, timesteps, or logged events.
- Repeated seeds from one fixed dataset quantify algorithmic variability, not population generalization by themselves.
- Cross-validation folds are dependent reuse of the same observations; they are not independent studies.
- Cluster assignment, nested measurements, and repeated measures must appear in both the power calculation and the analysis.

## Required outputs

Write under `求解/实验/`:

- `experiment_contract.md` with estimand, units, factors, outcomes, nuisance structure and inference boundary;
- `allocation_schedule.csv` or `run_schedule.csv` plus seed and generator version;
- `power_analysis.json` or a documented minimum-detectable-effect analysis;
- `analysis_plan.md` with contrasts, models, multiplicity, missingness and stopping rules;
- `deviations.md` after execution.

The design gate passes only when the intended effect is estimable, assignment and analysis units agree, nuisance structure is addressed, the sample-size rationale is sensitivity-tested, and the analysis and stopping rules were fixed before outcome inspection or clearly labelled exploratory.

Read [experimental-design-and-inference.md](../../references/experimental-design-and-inference.md) for the design-selection matrix and audit checklist.
