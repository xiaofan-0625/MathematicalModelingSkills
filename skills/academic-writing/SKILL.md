---
name: academic-writing
description: Plan, draft, revise, translate, and verify mathematical-modeling and academic manuscripts with evidence-grounded claims, consistent equations and results, traceable citations, and submission-ready structure. Use after model results are stable or when reviewing an existing paper.
---

# Write an Evidence-Grounded Paper

Write from verified evidence and frozen results. Never invent citations, values, experiments, or successful validation.

## Workflow

1. Inventory problem requirements, frozen results, figures, tables, equations, references, and format constraints.
2. Build an argument map linking each claim to evidence and each section to a required deliverable.
3. Select the operation: outline, draft, revise, translate, compress, expand, verify, or respond to review.
4. Draft in logical order: methods and results before abstract and conclusion when practical.
5. Keep symbols, units, names, sample counts, metrics, rounding, and conclusions consistent.
6. Verify every citation and every externally checkable claim.
7. Run numerical, citation, structural, and format gates before delivery.

## Mathematical-modeling paper structure

- Abstract: problem, methods by subproblem, key quantitative results, validation, and conclusion.
- Problem restatement: preserve the task without copying unnecessary background.
- Problem analysis: explain dependencies and modeling logic for each subproblem.
- Assumptions: state necessity, scope, and likely consequence of violation.
- Symbols: define every important symbol and unit once.
- Model sections: idea, formulation, solution method, result, interpretation, and validation.
- Sensitivity/robustness: test claims under plausible perturbations.
- Evaluation and extension: give concrete strengths, limitations, and applicable scope.
- References: include only verified and used sources.

## Claim discipline

- Distinguish observed, estimated, simulated, and assumed quantities.
- Match claim strength to design and uncertainty.
- Report limitations where they affect interpretation.
- Avoid citation dumping; explain why each cited source supports the statement.
- Preserve equations, reference identifiers, and frozen numbers during language revision.
- Record the exact evidence path, metric, aggregation, scope and uncertainty behind each headline claim. If evidence supports only a narrower population, regime, dataset or comparison, weaken the sentence instead of rounding the verdict upward.

Before final drafting, apply [claim-evidence-integrity.md](../../references/claim-evidence-integrity.md). Only `supported` or accurately rewritten `qualified` claims may enter the abstract and conclusion; `unsupported` claims must be removed and `unresolved` claims must remain visibly provisional.

When a paper revision changes an equation, number, table, figure, caption, scope statement, or
claim strength, record the change as a rework event. Trace it back to the earliest responsible
stage, regenerate the affected evidence and frozen values when needed, and rerun cross-file
consistency before accepting the prose. Language-only edits may stay at G4/G5 only when protected
technical meaning is unchanged.

## Completion gates

Verify that all required questions are answered, all paper values match machine-readable results, all figures and tables are cited, all references resolve, the source compiles when a renderer is available, and uncertainty is visible rather than hidden.
