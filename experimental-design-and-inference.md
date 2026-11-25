# Experimental Design and Inference Checklist

Use this reference before collecting controlled observations or launching algorithmic or simulation experiments.

## Design selection

| Question structure | Preferred starting design | Main risk to audit |
|---|---|---|
| Compare a few conditions on independent units | completely randomized or randomized block | imbalance, confounding, wrong independent unit |
| Known prognostic groups | stratified block randomization | too many sparse strata, predictable allocation |
| Several factors and interactions | full or fractional factorial | aliasing, inadequate resolution, unmodeled interaction |
| Optimize continuous settings | central composite, Box-Behnken, or justified space-filling design | curvature, boundary extrapolation, run-order drift |
| Same unit receives several conditions | crossover or repeated measures | carry-over, period effects, dependence |
| Treatment assigned to groups | cluster-randomized or hierarchical design | too few clusters, individual-level pseudoreplication |
| Hard-to-change and easy-to-change factors | split-plot design | wrong error term and randomization level |
| Algorithms across datasets/scenarios | paired blocked comparison | folds/seeds treated as independent populations |
| Observational causal contrast | explicit identification design | confounding, positivity, interference, post-treatment control |

## Power and sample-size record

Record the primary estimand, effect scale, smallest practically important effect or effect range, alpha or decision threshold, target power, sidedness, allocation, variance or event-rate assumption, intracluster correlation, repeated-measure correlation, multiplicity, attrition, and software/version. Show required sample size or minimum detectable effect across plausible assumptions.

Do not calculate observed post-hoc power from the estimated effect. For completed studies, report effect estimates and uncertainty, or the detectable-effect range at the achieved design.

## Pre-execution audit

- Treatment, outcome, estimand and time ordering are explicit.
- Experimental, assignment and analysis units are distinguished.
- Independent replication count is correct.
- Randomization, blocking, stratification and run order are reproducible.
- Controls and nuisance factors are sufficient for the intended contrast.
- Factorial aliases, cluster structure, nesting and repeated measures are estimable.
- Primary and exploratory outcomes are separated.
- Exclusion, missing-data, multiplicity and stopping rules are fixed.
- The analysis model contains the design structure.
- Synthetic or pilot-shaped data execute through the planned analysis.

## Computational experiment translation

For algorithm or simulation comparisons, map laboratory terms explicitly:

- treatment: algorithm, policy, feature set, or model component;
- experimental unit: independent dataset, problem instance, scenario, or generated world;
- block: the same instance evaluated across treatments;
- repeated measurement: seeds, folds, horizons, or timepoints within an instance;
- nuisance factor: hardware, software version, initialization, budget, or preprocessing;
- outcome: predeclared metric with direction, unit and aggregation rule.

Use paired comparisons when treatments share the same instances. Report both across-instance variation and within-instance algorithmic variation when both matter.
