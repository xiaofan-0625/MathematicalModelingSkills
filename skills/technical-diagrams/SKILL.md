---
name: technical-diagrams
description: Design editable technical-route, system, algorithm, causal, and mechanism diagrams for mathematical-modeling papers, with semantic and visual integrity checks. Use for diagrams that explain structure rather than plot numerical data.
---

# Build Technical Diagrams

Start with the claim the diagram must make. Use data plotting for quantitative comparisons; use a technical diagram for relationships, sequence, ownership, or mechanism.

## Workflow

1. Write a one-sentence evidence purpose and choose the diagram grammar: flow, dependency graph, architecture, causal graph, state machine, timeline, mechanism, or an embodied mechanism illustration when boxes and arrows would hide the interaction.
2. Define nodes and typed edges before styling. Distinguish data, process, decision, model, result, and feedback consistently.
3. Keep reading order explicit, labels short, and crossings minimal. Do not encode essential meaning by color alone.
4. For a physical or embodied metaphor, require a one-to-one mapping from model concepts to visible parts, relations to connectors or contact, and state changes to position, shape, or clearly labeled stages. Every visible part must be driven by the same model and claim as the caption; reject decorative motion or geometry that has no mathematical meaning.
5. Preserve an editable source such as Draw.io, Mermaid, Graphviz, or native vector format. Use unique identifiers and valid directed connections; do not fake connectors with loose lines. Keep text and exact annotations editable rather than baking unreliable generated lettering into a bitmap.
6. Export vector first when the submission format permits, plus a preview image. Embed fonts or use portable fonts where necessary.
7. Inspect the rendered paper at final size for clipped text, overlap, edge-node collisions, illegible labels, false visual hierarchy, and inconsistency with the equations or code. A static export must remain truthful even when the source concept was first explored interactively or with animation.

## Gate

The diagram is complete only when a reader can follow it without body-text rescue, every element has a role, the editable source is preserved, and the final PDF rendering is legible. Store source and exports under `求解/问题X/图片/` or the paper's figure directory.

Read [visual-evidence-design.md](../../references/visual-evidence-design.md) for the figure-versus-diagram decision and QA checklist.
