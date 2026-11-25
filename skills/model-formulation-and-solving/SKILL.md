---
name: model-formulation-and-solving
description: Turn an approved mathematical-modeling blueprint into explicit variables, equations, algorithms, solver settings, executable interfaces, and feasibility checks. Use after model candidates are selected and during implementation or solver repair.
---

# Formulate and Solve the Model

Make the mathematical object and the implemented object agree. A solver status is evidence about a run, not proof that the model is correct.

## Workflow

1. Define sets, indices, parameters, decision variables, units, domains, time order, and information available at each decision.
2. State objective functions, constraints, initial or boundary conditions, stochastic assumptions, and the link from each equation to the problem contract.
3. Check dimensional consistency, identifiability, feasibility, boundedness, symmetry, degeneracy, and expected limiting behavior before coding.
4. Implement a legal baseline and small verifiable instance. Then choose an exact, numerical, simulation, statistical, or heuristic solver based on structure and evidence, not popularity.
5. Specify initialization, scaling, tolerances, random seeds, stopping rule, resource budget, infeasibility handling, and what guarantee the method does and does not provide. When runtime or memory affects feasibility, profile representative runs and separate measured bottlenecks from guesses; record any temporary instrumentation.
6. Separate model construction, solving, evaluation, and export. Save raw solver diagnostics and machine-readable outputs; do not transcribe headline numbers manually.
7. Verify constraints independently of solver-reported success. Where possible compare with an analytic case, enumeration, bound, alternate implementation, or conservation law.

## Multi-objective and heuristic optimization

When objectives conflict, preserve them separately until a preference rule is justified. Define dominance, objective direction, scaling, constraints, reference point or decision preference, and the admissible decision set before choosing an algorithm. Report the nondominated feasible set or an auditable approximation, then explain why any final compromise is selected; a weighted sum with unexplained weights is not a neutral answer.

For stochastic or population-based solvers, compare against a legal simple baseline, repeat independent seeds, save convergence histories, and assess feasibility, spread, and stability of the obtained trade-off set. Hypervolume or another quality indicator is meaningful only with a declared reference and comparable scaling. A finite search, evolutionary run, or sampled Pareto front is evidence about explored candidates, not proof of continuous global optimality.

## Outputs and gate

Maintain `求解/计划/modeling_blueprint.md`, code under `求解/问题X/code/`, raw outputs and logs under `求解/问题X/结果/`, and explicit interfaces between subproblems.

G3 passes only when the implementation answers the approved formulation, produces legal repeatable outputs, records diagnostics, and states the strength of its guarantee. Route comparative model choice to `model-deliberation` and empirical stress testing to `validation-and-robustness`.

If a claimed formula, bound, convergence statement, approximation, or algorithm guarantee requires a nontrivial derivation, route it to `mathematical-derivation-and-proof`. Solver output, symbolic simplification, and numerical agreement are checks, not substitutes for the required proof obligations.

Read [modeling-solver-playbook.md](../../references/modeling-solver-playbook.md) when choosing algorithms or checking solver claims.
