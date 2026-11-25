# Claim-to-Evidence Integrity

Use this gate after results exist and before drafting or accepting a quantitative claim.

## Claim record

For each headline claim record:

- exact wording and intended scope;
- claim type: observed, estimated, simulated, causal, comparative, generalization, novelty, or guarantee;
- raw evidence paths and producing code;
- metric key, unit, direction, denominator and aggregation rule;
- dataset, split, horizon, scenario, seed policy, sample count and configuration;
- point estimate, uncertainty and comparison baseline;
- status: `supported`, `qualified`, `unsupported`, or `unresolved`;
- reversal condition and missing evidence.

## Deterministic integrity checks

- Every reported file and metric key exists and is produced by executed code.
- Paper values match raw evidence under declared rounding.
- Means, medians, best runs, folds, seeds and repeated measures are not interchanged.
- Relative and absolute improvements use the stated denominator and correct arithmetic.
- Compared methods use compatible data, preprocessing, budgets, constraints and metrics.
- Ground truth originates from the declared dataset or is visibly labelled as a proxy; model output is not recycled as hidden reference truth.
- Normalization does not use the candidate's own extrema or statistics to manufacture a favorable score unless that definition is externally justified.
- Defined metric functions are actually called and their outputs appear in retained results.
- Evaluation scope supports words such as “consistent”, “robust”, “general”, or “comprehensive”.
- Failed, missing and excluded runs are visible; the paper does not silently select a favorable seed or scenario.

## Claim-strength routing

- `supported`: evidence directly matches the claim, scope and aggregation.
- `qualified`: evidence supports a narrower population, regime, metric, or comparison; rewrite the claim to that boundary.
- `unsupported`: evidence contradicts the claim, uses an invalid comparison, or is missing; remove it from the paper.
- `unresolved`: evidence exists but integrity, uncertainty, mapping or reviewer questions remain open; do not promote it to a headline conclusion.

A file-existence check proves only that a value is present. It does not establish causal identification, generalization, novelty, practical importance, or mathematical correctness.
