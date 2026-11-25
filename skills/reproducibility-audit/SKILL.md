---
name: reproducibility-audit
description: Audit whether a mathematical-modeling project can regenerate its data products, numerical results, figures, and paper from protected inputs and recorded code. Use before final delivery, after major revisions, or when a result cannot be traced; do not modify raw inputs to make a rerun pass.
---

# Audit Reproducibility and Cross-Artifact Consistency

Treat the project as an artifact graph: original inputs feed transformations, models produce frozen results, and frozen results feed figures, tables, and prose. A project is not reproducible when only the final PDF exists.

## Workflow

1. Inventory protected inputs, external data snapshots and queries, scripts, environments, seeds, generated data, model reports, frozen results, figures, tables, and manuscript files.
2. Check that every generated artifact has a source path and a producing command or script. Record hashes or version identifiers; for external data also verify endpoint or file identity, query, retrieval time, release/vintage, licence, raw snapshot, and transformation path.
3. Perform a clean or isolated rerun from the original inputs. If a runtime, package, font, or proprietary file prevents the rerun, record the exact blocker and the strongest verified fallback.
4. Compare regenerated results with `frozen_numbers.json` using stated tolerances. Then compare paper text, tables, captions, and figures against the frozen values and labels.
5. For each quantitative or scope claim, verify the evidence file and metric key, exact value and rounding, aggregation rule, seed/run count, configuration, comparator, denominator, uncertainty, and claimed population or scenario. Detect best-run cherry-picking, phantom results, incompatible comparisons, and paper-to-result drift.
6. Check path portability, random seeds, dependency versions, missing files, hidden manual edits, and accidental writes under raw-input directories.
7. Produce a prioritized report: blocking, evidence-dependent, and presentation-only findings. Repair only verified issues, rerun the affected checks, and preserve the original audit report.

After any material repair, compare the project revision recorded in `project_state.yaml`, the
skill-use ledger, frozen results, paper, manifest, and scorecard. A clean rerun for an old revision
does not pass the current gate. If a source, code path, environment, or transformation changed,
write the rework event before rerunning and verify that no stale artifact remains in the delivery
graph.

## Required outputs

Write `求解/reproducibility_report.md` and `求解/artifact_manifest.json`. The manifest must map each reported number, table, and figure to its source result and producing code. The report must state the rerun scope, pass/fail status, tolerances, environment, unresolved blockers, and the exact next action.

Read [references/reproducibility-package.md](../../references/reproducibility-package.md) for the artifact manifest, clean-rerun checklist, and delivery package layout.

Use [claim-evidence-integrity.md](../../references/claim-evidence-integrity.md) for the paper-to-evidence audit and claim-strength routing.
