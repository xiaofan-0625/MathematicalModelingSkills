---
name: data-analysis
description: Audit, clean, explore, and statistically analyze mathematical-modeling datasets. Use for CSV, Excel, tabular, time-series, multi-file, missing-data, outlier, distribution, correlation, hypothesis-test, regression-diagnostic, power-analysis, or pre-modeling data tasks.
---

# Analyze Modeling Data

Work from original attachments to an auditable analysis dataset and evidence-backed findings. Diagnose before selecting a statistical method.

When data must be acquired from an API, portal, webpage, or external repository, first use `external-data-acquisition` to freeze the source response and provenance. When the project controls treatment assignment or data collection, use `experimental-design-and-inference` before outcome inspection; this Skill analyzes the resulting data but does not repair a confounded design.

## Workflow

1. Inventory every file, sheet, table, encoding, shape, field, unit, key, and time range.
2. Preserve originals. Record every cleaning or transformation operation.
3. Classify variables by effective type: identifier, categorical, ordinal, continuous, count, datetime, text, target, or leakage risk.
4. Audit missingness, duplicates, invalid ranges, inconsistent units, impossible values, outliers, and cross-file key integrity.
5. Produce univariate summaries before relationship analysis.
6. Branch into group comparison, correlation, regression, classification, time-series, survival, reliability, ROC, or other justified analysis.
7. Check assumptions and effect sizes. Do not report only p-values.
8. Separate exploratory findings from confirmatory tests.
9. Save cleaned data, an audit log, summary tables, and machine-readable results.

## Cleaning rules

- Never modify source attachments in place.
- Do not impute, delete, winsorize, normalize, or encode without recording the rule and affected count.
- Fit learned preprocessing only on training data when prediction is involved.
- Treat extreme values as evidence to investigate before treating them as errors.
- Preserve identifiers for joining but exclude them from models unless substantively justified.
- Detect target leakage, future leakage, duplicated subjects, and post-outcome variables.

## Statistical rules

- Match the test or model to outcome type, dependence structure, distribution, sample size, and study design.
- Check independence, residual behavior, variance assumptions, multicollinearity, and influential observations where applicable.
- Report estimates, uncertainty intervals, effect sizes, sample sizes, and assumption limitations.
- Correct for multiple testing when the analysis creates a family of hypotheses.
- Use resampling, robust methods, or sensitivity analysis when classical assumptions are weak.
- Do not interpret association as causation without an identification strategy.

## Required outputs

Write under `求解/`:

- `data_audit.md`: inventory, quality issues, decisions, and limitations;
- `预处理数据.*`: cleaned analysis data when transformation is necessary;
- reproducible analysis code;
- machine-readable summary and test results;
- figures only when they help diagnose or communicate a finding.

Return a concise finding list distinguishing observation, interpretation, and unresolved question.
