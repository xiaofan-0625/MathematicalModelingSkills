# Reproducibility Package

Use this checklist before calling G5 or G7 complete. It combines the evidence-ledger, replication-package, and consistency-audit patterns with the existing mathskills frozen-results rules.

## Artifact manifest

Create `求解/artifact_manifest.json` with entries like:

```json
{
  "artifact_id": "figure_1",
  "kind": "figure",
  "path": "求解/问题一/图片/figure_1.svg",
  "source_result": "求解/问题一/结果/frozen_numbers.json",
  "code": "求解/问题一/code/plot.py",
  "command": "python code/plot.py",
  "input_hashes": {"数据/附件1.xlsx": "..."},
  "status": "verified"
}
```

Every reported number, table, and figure needs an entry or a traceable parent artifact. Use relative paths so the project remains movable.

## Clean-rerun checklist

- original inputs are present and unchanged;
- external data raw responses, exact queries, release/vintage metadata, licences and hashes are preserved when used;
- raw-input directories contain no generated files;
- environment and dependency versions are recorded;
- seeds, solver settings, fonts, and randomization rules are recorded;
- the main entry command is documented;
- generated data can be rebuilt from code;
- external joins can be reproduced with declared keys, cardinality and unmatched-row reports;
- frozen values match the regenerated values within declared tolerances;
- every figure and table can be regenerated from results, not hand-edited;
- the manuscript compiles from the documented source tree;
- unresolved proprietary, network, or unavailable-runtime blockers are explicit.

## Delivery layout

```text
求解/
  project_state.yaml
  artifact_manifest.json
  reproducibility_report.md
  citation_ledger.csv
  问题X/结果/frozen_numbers.json
  问题X/code/
论文/
  论文.tex or main.typ
  论文.pdf
```

The audit report must separate `blocking`, `evidence-dependent`, and `presentation-only` findings. A successful compile without a clean rerun is not a reproducibility pass.
