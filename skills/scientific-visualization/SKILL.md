---
name: scientific-visualization
description: Explore data visually and create, review, repair, and export publication-quality scientific figures for mathematical modeling and academic papers. Use for chart selection, plotting code, multi-panel layouts, statistical graphics, figure storytelling, style consistency, accessibility, vector export, and visual QA.
---

# Create Scientific Visualizations

Design each figure around a question or claim. Use exploration graphics to learn and publication graphics to communicate; do not confuse the two.

## Workflow

1. Inspect the data schema, units, missingness, grouping, uncertainty, and sample sizes.
2. State the intended message, audience, publication medium, and final physical size. Assign the figure a role: motivating example or problem evidence, solution overview, or quantitative result. Do not ask one figure to perform all three jobs.
3. Choose the simplest chart that exposes the relevant comparison, distribution, relationship, sequence, network, or spatial structure. When a motivating example is useful, keep the same case or visual vocabulary through the solution overview so the reader can follow the transformation.
4. Define a figure contract: inputs, mappings, panels, annotations, uncertainty, dimensions, output formats, and a size budget for each panel, legend, label, and margin.
5. Generate reproducible plotting code from frozen results. If a generative image tool is used for conceptual artwork, compose exact labels, legends, arrows, scale bars, and data-bearing geometry afterward in code or editable vector software; never trust generated text or approximate geometry as scientific evidence.
6. Run technical checks and visually inspect the rendered artifact.
7. Repair overlap, clipping, misleading scales, unreadable text, poor contrast, and inconsistent styling. Bar charts start at zero unless a different encoding is used and the truncation is explicitly justified; do not import a visually dramatic axis convention that changes perceived magnitude.
8. Export source code, vector output when feasible, and a high-resolution raster copy.

## Chart routing

- Distribution: histogram, ECDF, density, box, violin, or point distribution.
- Relationship: scatter with justified fit and uncertainty; avoid hiding density.
- Group comparison: dot/interval, box/violin, dumbbell, or ranked bars.
- Time or sequence: line with uncertainty; use small multiples when series crowd.
- Composition: stacked bars only when part-to-whole comparison is genuinely needed.
- Matrix: heatmap with meaningful ordering and a labeled color scale.
- Network or flow: node-link or flow diagram only when topology is the message.
- Model evaluation: residual, calibration, ROC/PR, confusion matrix, feature effect, or sensitivity plot.

Do not use 3D, dual axes, decorative gradients, or pie charts unless the data and audience clearly justify them.

## Publication rules

- Size the figure for its final placement; do not rely on later scaling.
- Design paper figures for print and page composition rather than reusing slide, poster, or website dimensions unchanged.
- Keep fonts, weights, line widths, marker sizes, and colors consistent across the paper.
- Use accessible palettes and do not encode meaning by color alone.
- Label axes with quantity and unit. Explain error bars, intervals, and sample sizes.
- Use direct labels when they reduce lookup burden; keep legends concise otherwise.
- Highlight selectively and keep context visible in restrained neutral colors.
- Titles and captions should state the finding without overstating evidence.
- Prefer SVG/PDF with editable text; also export PNG/TIFF when required.

## QA gate

Check data-to-mark correctness, axis limits, ordering, aggregation, uncertainty, visual hierarchy, clipping, overlap, contrast, color-blind accessibility, final-size readability, and agreement with frozen numerical results.

Deliver the figure, plotting code, caption, source data or result path, and a brief QA report.
