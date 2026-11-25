---
name: scientific-tables
description: Turn frozen modeling results into compact, auditable scientific tables with correct units, precision, uncertainty, comparison direction, notes, and machine-readable provenance. Use for descriptive, comparison, ablation, sensitivity, optimization, or final-answer tables in a modeling paper.
---

# Build Scientific Tables

A table is a result interface, not a place to retype numbers. Every displayed cell must trace to a frozen machine-readable source and retain enough context to be interpreted correctly.

## Table contract

Before formatting, define the question answered, row entity, column metric, unit, favorable direction, aggregation, uncertainty statistic, comparison set, missing-value meaning, and source artifact. Decide whether the table belongs in the main text or appendix based on decision value, not on available space alone.

## Construction rules

1. Generate cells from CSV, JSON, database output, or another machine-readable result. Do not manually transcribe headline numbers.
2. Keep units in headers and use consistent scaling. Separate raw values from percentages, rates, indices, and normalized scores.
3. Choose precision from measurement and decision resolution. Round for display only; compare and rank using unrounded values. Align decimal places within a metric.
4. Name uncertainty precisely: standard deviation, standard error, confidence interval, prediction interval, quantiles, or across-seed variation. `±` without a definition is incomplete.
5. Bold or underline results only within a genuinely comparable set and only after declaring whether higher or lower is better. Do not mark tiny numerical differences as meaningful when uncertainty or tolerance makes them ties.
6. Treat zero, missing, not applicable, not observed, infeasible, timeout, and failed run as distinct states. Explain symbols and exclusions in table notes.
7. For ablations and sensitivity tables, hold evaluation conditions fixed and expose the baseline. For optimization tables, report feasibility and constraint violation alongside objective values when relevant.
8. Keep tables scan-friendly: descriptive title, stable ordering, concise headers, grouped columns only when hierarchy is real, and notes for abbreviations or exceptions. Split a wide table rather than shrinking it below readable size.
9. Reconcile every table with prose, figures, abstract, and `frozen_numbers.json`; regenerate downstream artifacts after any upstream change.

Use publication conventions such as restrained rules and aligned numeric columns when the template supports them, but current competition rules and the supplied template take precedence over a preferred LaTeX package.

## Outputs and gate

Preserve the source data, generation code or deterministic transformation, editable table source, rendered PDF result, and a short provenance record. The G4 gate passes only when cells match frozen data, units and uncertainty are explicit, highlighting is defensible, and the final PDF is readable at normal zoom.

Use [paper-writing-rules.md](../../references/paper-writing-rules.md) for narrative placement and [visual-evidence-design.md](../../references/visual-evidence-design.md) for cross-figure consistency.
