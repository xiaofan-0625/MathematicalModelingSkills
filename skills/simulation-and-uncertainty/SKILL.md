---
name: simulation-and-uncertainty
description: Design Monte Carlo, scenario, and discrete-event simulation studies with explicit uncertainty sources, bounded execution, independent replications, convergence evidence, and tail-risk reporting. Use when random inputs, event-driven systems, queues, or uncertainty propagation materially affect a modeling conclusion.
---

# Simulate and Quantify Uncertainty

Simulation approximates consequences of an explicit model; it does not validate the model by itself. Separate variability inherent in the system from uncertainty caused by limited knowledge.

## Study contract

State the decision question, estimand, system boundary, time unit, state variables, stochastic inputs, output statistics, termination rule, and what the simulation cannot identify. Classify uncertainty as aleatory, parameter, structural, scenario, or numerical. Give each input a source, unit, distribution or admissible set, dependence structure, and justification.

Choose the smallest adequate mechanism:

- Monte Carlo propagation for uncertain inputs through a static or dynamic model;
- scenario analysis when probabilities are unavailable or contested;
- discrete-event simulation for queues, resources, routing, inventory, logistics, or other event-driven systems;
- resampling only when the empirical sampling assumption is defensible.

## Execution and validation

1. Verify deterministic limiting cases, conservation identities, boundary behavior, queue discipline, event ordering, and a small analytic or enumerated case before stochastic runs.
2. Use separate documented random streams for logically distinct sources. Record seed policy and environment; do not rely on one favorable seed.
3. Bound time, events, entities, memory, and replications. For steady-state studies justify initialization, warm-up removal, run length, and treatment of unfinished entities.
4. Estimate uncertainty from independent replication-level summaries. Observations within one run are generally correlated and are not independent replications.
5. Show convergence of the estimand and its interval against simulation effort. Increase effort until the predeclared precision target is met or report that it was not met.
6. Preserve input dependence. Independent marginal sampling is invalid when correlation, common causes, conservation, or ordering couples inputs.
7. Validate inputs and outputs against observed data, expert constraints, or accepted benchmarks for the stated purpose. Distinguish verification of code from validation of the conceptual model.
8. Report central tendency, dispersion, interval or quantiles, tail probability, and decision-relevant risk. Mean performance alone can hide unacceptable rare failures.
9. Challenge distribution families, parameters, dependence, scenarios, horizon, warm-up, and policy assumptions. Record reversal conditions and structurally unsupported claims.

Do not interpret Monte Carlo precision as real-world predictive accuracy, simulation association as causation, or repeated draws from one misspecified model as structural robustness. Avoid false precision when input evidence is weak.

## Outputs and gate

Maintain `simulation_contract.md`, `seed_manifest.json`, replication-level results, convergence evidence, input/source ledger, and validation report under the relevant `求解/问题X/` folders. Freeze only summaries that can be regenerated from those records.

G3.5 passes only when the model is verified on edge cases, independent replications support the reported precision, important dependence and tail behavior are addressed, and at least one plausible alternative assumption is tested. Use [robustness-guide.md](../../references/robustness-guide.md) for general sensitivity and reversal analysis.
