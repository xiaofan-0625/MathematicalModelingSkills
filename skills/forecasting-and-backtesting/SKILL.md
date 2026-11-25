---
name: forecasting-and-backtesting
description: Design and validate time-ordered forecasting models with leakage-safe rolling backtests, legal baselines, multi-step protocols, and calibrated prediction intervals. Use when a mathematical-modeling task predicts future values or evaluates a policy using temporal data; do not use for unordered regression.
---

# Forecast and Backtest Time Series

Treat forecasting as a decision made at a historical information boundary, not as ordinary random-split regression. A sophisticated model is unacceptable if it sees data unavailable at the forecast origin.

## Forecast contract

Before fitting, record:

- target, unit, cadence, forecast horizon, forecast origin, and required output granularity;
- the decision time and which variables are actually known then;
- whether future covariates are known, scheduled, separately forecast, or unavailable;
- the operational loss: point error, interval miss, asymmetric cost, peak error, or threshold failure;
- training window, update frequency, latency gap, and any regime boundary.

Audit timestamp parsing, timezone, duplicate times, missing periods, irregular sampling, censoring, revisions, aggregation, and transformations. Fit imputation, scaling, feature engineering, seasonal decomposition, and hyperparameter selection inside each training window.

## Evaluation workflow

1. Build legal baselines: last value, seasonal naive, historical mean or drift as appropriate. A candidate must beat the relevant baseline under the same origins and horizon.
2. Use rolling-origin or expanding/sliding-window backtesting. Add a gap when labels or covariates arrive late. Random train/test splits are not valid evidence for temporal forecasting.
3. Match the production strategy: recursive, direct, multiple-output, or hybrid. Report error by horizon, not only one pooled mean.
4. Choose metrics before seeing final results. Pair at least one scale-dependent metric with a scale-free or decision-specific metric; do not use MAPE when zeros or near-zeros make it unstable.
5. Produce prediction intervals when uncertainty matters. Evaluate empirical coverage, average width, calibration by horizon, and interval failure during peaks or regime shifts.
6. Compare models across identical forecast origins. Preserve per-origin predictions so aggregate scores can be audited and paired differences can be inspected.
7. Stress test window length, origin selection, seasonality assumptions, missingness, transformation, and structural breaks. A foundation model or deep learner remains a candidate, not an automatic winner.

Never tune on the final holdout, use future aggregates as features, interpolate across the split with future observations, or call an in-sample fit a forecast. If only one historical trajectory exists, state the limited effective sample size and avoid treating overlapping forecast errors as independent replicates.

## Outputs and gate

Save the forecast contract and split diagram under `求解/计划/`, per-origin predictions and metrics under `求解/问题X/结果/`, and a machine-readable table containing origin, horizon, actual, point forecast, interval bounds, model, and data version.

G3.5 passes only when temporal leakage checks pass, legal baselines use the same information set, conclusions are stable across credible origins, and interval claims are supported by observed coverage. Route generic data cleaning to `data-analysis`, result freezing to `validation-and-robustness`, and final charts to `scientific-visualization`.
