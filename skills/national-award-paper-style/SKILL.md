---
name: national-award-paper-style
description: Learn from and apply evidence-backed writing, structure, figure, table, appendix, and LaTeX layout patterns observed in national mathematical-modeling award papers. Use during CUMCM paper planning, drafting, figure/table QA, appendix assembly, and final review; do not copy distinctive wording or treat an individual paper as a mandatory template.
---

# National Award Paper Style

Use the local corpus as a style and quality reference, not as a source of reusable text,
data, claims, figures, or solutions. The goal is a clear, auditable CUMCM paper whose
structure matches the problem and whose visual decisions help a reviewer verify the work.

## Load progressively

- Read `references/national-award-paper-style.md` for the learned writing and structure rules.
- Read `references/national-award-layout-contract.md` before compiling or repairing a paper.
- Read `references/national-award-figure-appendix.md` when planning figures, tables, source code,
  supplementary calculations, or appendices.
- Read `references/national-award-corpus-inventory.json` only when choosing a benchmark by year,
  problem letter, or artifact type.

## Route by deliverable

1. **Outline**: map every original subproblem to a paper section and show the dependency chain.
2. **Draft**: write from frozen results and the evidence ledger; use the corpus patterns for
   information order, not for sentence copying.
3. **Figures and tables**: assign one claim to each figure/table, place it immediately after the
   supporting paragraph, and preserve source-data lineage.
4. **Appendix**: include a concise algorithm/code index and reproducible output map; move only
   bulky details out of the main argument.
5. **QA**: run the layout contract, then inspect the rendered PDF at final size.

## Hard constraints

- Never copy an award paper's distinctive prose, title, diagram, data, code, or numerical result.
- Do not add a section merely because it occurs in a sample. If the problem does not support a
  sensitivity analysis, prove why it is unavailable and label the limitation.
- Every headline number must trace to `frozen_numbers.json` or a documented analytical output.
- Every figure/table/equation must have a purpose, a source path, a caption or explanation, and a
  cross-reference in the surrounding text.
- Prefer the official competition template and current competition rules over historical samples.
- Treat scanned PDFs, journal reprints, solution collections, and advertisements as context only;
  do not use them as clean layout measurements without identifying their source class.

## Completion gate

The style pass is complete only when the paper has a problem-matched outline, evidence-bound
abstract, explicit model-to-result chain, readable figures/tables, a controlled appendix, a clean
compile or an explicit compiler blocker, and a report separating mandatory fixes from stylistic
options.
