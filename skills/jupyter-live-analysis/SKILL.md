---
name: jupyter-live-analysis
description: Use a stateful Jupyter kernel for iterative mathematical-modeling data exploration, plotting, and small reproducible calculations when persistent variables and visible notebook state materially improve the analysis. Use terminal scripts for final batch runs.
---

# Jupyter Live Analysis

Use a live kernel as an exploratory workbench, not as the only source of final results.

## Workflow

1. Confirm the notebook path and project scope; never place a notebook inside protected raw-data
   directories.
2. Inspect schema, dimensions, missingness, units, and key integrity before modeling.
3. Execute small cells incrementally and record important transformations in the project code.
4. Save plots, tables, and a short narrative with the input paths and cell or script provenance.
5. Restart and run all cells when a clean verification is required; stale kernel state is not
   evidence of reproducibility.
6. Move accepted analysis into a deterministic script before freezing paper numbers.

## Safety and limits

- Do not put credentials, private endpoints, or private data in notebook outputs.
- Do not claim a result from a cell that was not re-run from a clean state when statefulness could
  affect it.
- If Jupyter is unavailable, use the documented Python-script fallback and record the limitation.
- Do not install kernels or packages without authorization.

## Outputs

Keep a notebook or session receipt under `求解/探索/`, and ensure the final `求解/` scripts,
machine-readable results, and figures can reproduce every value used in the paper.
