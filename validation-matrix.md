# Validation Matrix

Choose the smallest set of tests that can falsify the intended use of the model. Record the reason each test is included and the decision it can change.

| Model purpose | Minimum baseline | Core validation | Failure-oriented check |
|---|---|---|---|
| Prediction | naive or mean/seasonal baseline | holdout, time-block, or cross-validation with MAE/RMSE and uncertainty | leakage check, subgroup or temporal shift |
| Ranking/classification | majority or simple score baseline | calibration, confusion matrix, ROC/PR where appropriate | threshold sensitivity and class-imbalance check |
| Optimization | feasible heuristic or relaxation | objective, constraint satisfaction, stability across starts | perturbation, infeasibility, and boundary stress test |
| Simulation | analytical or limiting-case benchmark | repeated seeds, coverage, convergence, and distributional checks | parameter and initial-condition sensitivity |
| Evaluation/index construction | transparent equal-weight or domain baseline | alternative weights, normalization, ranking stability | leave-one-variable-out and missingness stress test |
| Time series | seasonal or last-value baseline | rolling-origin or blocked evaluation | regime shift and horizon sensitivity |

## Minimum report fields

```yaml
validation_id: model_1_v1
target: prediction | ranking | optimization | simulation | evaluation
baseline: name and configuration
protocol: split, folds, time window, or repeated seeds
metrics: [{name, value, unit, uncertainty, direction}]
stress_tests: [{name, perturbation, result, decision_impact}]
failed_or_null_checks: []
accepted_model: name and version
reversal_conditions: []
```

Do not treat a single pass as proof. Explain what remains untested and whether the claim is descriptive, predictive, normative, or causal.
