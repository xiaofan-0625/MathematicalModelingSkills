# Visual Evidence Design

Every visual begins with an evidence sentence: “This visual should let the reader determine ___.” If that blank cannot be filled, do not create the visual.

## Choose the representation

| Question | Preferred form |
|---|---|
| Trend, distribution, relationship, uncertainty, residual, or sensitivity | Data figure |
| Exact small set of values or comparisons | Table |
| Process, dependency, system boundary, algorithm, state, or mechanism | Technical diagram |
| One key scalar | Prose or compact callout, not a chart |

Do not use a process diagram to imply quantitative evidence. Do not use a decorative plot when a table communicates exact values better.

## Assign the figure's role

- **Motivating example or problem evidence:** show the concrete failure, ambiguity, geometry, data condition, or decision context that makes the problem nontrivial. Use a real or representative case and label exactly what the reader should notice.
- **Solution overview:** show components, information flow, mathematical interfaces, and where each claimed contribution enters. Reuse the motivating case or visual vocabulary when that makes the transformation easier to follow.
- **Quantitative result:** show measured comparison, uncertainty, sensitivity, robustness, or failure boundary from frozen results. Do not replace it with a conceptual illustration.

A paper may need all three roles, but they should normally be separate figures or clearly separated panels. A single dense graphic that mixes motivation, architecture, and results often hides the evidence chain.

## Data figure contract

Before plotting, state the comparison, population or scenario, metric and unit, aggregation, uncertainty, and expected reader takeaway. Keep plot data in a machine-readable file and the generating code beside it. Use perceptually sound encodings, direct labels where practical, consistent scales for comparisons, and uncertainty or sample size when relevant.

Exploratory figures may be dense and numerous; paper figures must have one main job. Never select a chart solely because it looked favorable after trying many variants without disclosing the selection logic.

## Technical diagram contract

Define node types, edge meanings, direction, system boundary, start and end states, feedback, and exception paths before layout. Use stable identifiers in editable source. Connect edges to nodes, not approximate coordinates; avoid crossings and edge-node overlap; keep a clear reading direction.

Shapes and color must be consistent and redundant with labels or line styles. Decorative shadows, 3D effects, gradients, and pseudo-precision are usually harmful in competition papers.

When an abstract mechanism benefits from a physical metaphor, map every concept, relation, and state to a visible part, connector, or configuration. The visual mapping must be derived from the same model described by the equations and caption. Interaction or animation may help exploration, but the final static export must retain the full truthful explanation.

If generative imagery helps draft conceptual elements, add text, equations, data marks, legends, arrows, and scale bars afterward in code or editable vector software. Generated labels and approximate geometry are not evidence. For bar charts, keep the quantitative baseline at zero; use interval, dot, or line encodings when a narrowed range is necessary to show small differences.

## Export and QA

- Preserve editable source and use vector output (`PDF` or `SVG`) when supported.
- Also create a bitmap preview for fast inspection.
- Use embedded or portable fonts; check mathematical symbols and CJK text.
- Inspect the actual compiled PDF, not only the editor canvas.
- Check at 100% page view and at expected print size for label size, line weight, clipping, crop, contrast, legend order, and grayscale distinguishability.
- Confirm caption, numbering, cross-reference, data source, and nearby interpretation.
- Compare plotted values against the source file and frozen numbers.

Reject a visual when it is unreadable without zoom, contradicts the paper, obscures uncertainty, has untraceable numbers, or carries no evidence beyond nearby prose.
