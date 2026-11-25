# Modeling and Solver Playbook

Use this reference after the problem contract is stable. It is a decision aid, not an algorithm catalog.

## Formulation record

For each subproblem define:

1. decision or estimand;
2. sets, indices, variables, parameters, units, and domains;
3. data availability at decision time;
4. assumptions with purpose and likely bias;
5. objective, loss, likelihood, or governing equations;
6. hard constraints, soft penalties, initial and boundary conditions;
7. interface to earlier and later subproblems;
8. baseline, verification oracle, validation protocol, and failure criteria.

Run dimensional, sign, limiting-case, feasibility, boundedness, identifiability, and data-sufficiency checks before selecting a solver.

## Choose by mathematical structure

| Structure | Candidate method families | Claims that require care |
|---|---|---|
| Linear continuous or mixed-integer | LP/MILP, decomposition, valid bounds | Optimality requires a valid gap or proof, not merely a feasible status |
| Smooth nonlinear | constrained NLP, automatic differentiation, multistart | Local convergence is not global optimality |
| Nonsmooth or combinatorial | dynamic programming, CP-SAT, branch-and-bound, heuristics | Heuristics need feasibility checks, baselines, and gap language |
| Sequential uncertainty | stochastic/robust optimization, MDP, simulation | Distribution and information assumptions must be explicit |
| Prediction | interpretable baseline, regularized/statistical/ML models | Split protocol, leakage, calibration, and uncertainty matter more than novelty |
| Causal or policy effect | design-based or identified causal model | Prediction accuracy does not establish causal effect |
| Dynamical mechanism | ODE/PDE, difference equations, state-space models | Parameter identifiability and numerical stability must be tested |
| Network or spatial | graph algorithms, flow, spatial statistics | Connectivity, boundary and aggregation effects must match the setting |
| Multi-criteria decision | Pareto analysis, outranking, constrained utility | Weight sensitivity and normalization can reverse rankings |

Use specialized methods only when they fit the structure and can be validated within the competition budget. A popular or recent method is not automatically suitable.

## Baseline ladder

Start with the simplest legal comparator:

- constant, historical, random, greedy, or rule-based baseline;
- classical model with transparent assumptions;
- stronger domain baseline;
- proposed enhancement.

All models must share data splits, scenarios, constraints, metrics, and compute accounting. Do not compare a constrained method with an unconstrained score without explaining the difference.

## Implementation contract

Separate these layers:

```text
load/version inputs → transform/validate → build model
→ solve/simulate → verify feasibility → evaluate
→ export machine-readable results and diagnostics
```

Record solver and library versions, seed, initialization, scaling, tolerances, timeout, stopping reason, incumbent and bound when available, infeasibility diagnostics, and hardware-sensitive settings.

## Verification hierarchy

Prefer the strongest affordable check:

1. analytic solution or theorem under a special case;
2. exhaustive enumeration on a small instance;
3. valid upper/lower bound or conservation law;
4. independent implementation or solver;
5. perturbation, multistart, and residual checks;
6. domain plausibility only when stronger checks are unavailable.

If the optimizer returns success but independent constraint residuals fail, the run fails. If only a local or sampled result is available, state exactly that scope.

## When to simplify or stop

Reduce model complexity when the added component has no measurable benefit, cannot be identified from available data, breaks the compute budget, or makes the core conclusion unauditable. Stop experimentation when the registered budget is exhausted, the improvement is within noise, or a gate failure requires returning to formulation rather than trying more hyperparameters.
