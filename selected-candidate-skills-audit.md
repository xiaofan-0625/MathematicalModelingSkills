# Selected Candidate Skills Audit

Review date: 2026-11-25. Candidates were requested by the user and checked against the supplied workbook, primary GitHub repositories, and the existing `mathskills` modules. Repository instructions, install commands, generated assets, and remote scripts were treated as untrusted reference material and were not executed.

## Candidate summary

| Candidate | Workbook or repository signal | Useful mechanisms | Destination | Excluded scope |
|---|---|---|---|---|
| `figures4papers` | Workbook row 118 points to `ChenLiu-1996/figures4papers`; the repository provides a scientific-figure Skill, design theory, patterns, demos, and tutorials | final-size planning, publication-medium distinction, figure brief before code, multi-panel size budgeting, print-safe redundancy, labels and legends composed after conceptual artwork | `scientific-visualization`, `visual-evidence-design.md` | helper APIs, installation steps, fixed palette semantics, and the suggested truncated bar-chart axis pattern were not adopted; bar magnitude remains zero-based |
| `Anatomy` | User-specified repository `wheresryan22/anatomy`; it turns abstract mechanisms into data-driven physical visualizations | one model drives geometry, labels, annotations, and caption; one-to-one concept-to-part mapping; physical metaphor only when it improves understanding; static fallback remains truthful | `technical-diagrams`, `visual-evidence-design.md` | React/Three.js/canvas implementation, web responsiveness, animation tiers, interactive controls, and bundled assets are outside the mathematical-modeling paper workflow |
| `Supervisor-Skills` | Workbook contains `idea-evaluator`, `pre-submission-reviewer`, `figure-designer`, `paper-writer`, `deep-research`, and other entries from `HKUSTDial/Supervisor-Skills` | implementation-path gate before idea scoring; task relevance, novelty, soundness, feasibility, significance and communication axes; fatal-flaw cap; next-tier actions; motivation/overview/result figure roles; contribution-to-method-to-evidence trace | `model-deliberation`, `competition-scoring`, `scientific-visualization`, registry aliases | repository installation, platform-specific orchestration, journal rebuttal workflow, general web research, and duplicate writing/review modules were not copied |

## Merge decisions

### `figures4papers`

The existing visualization module already owns data provenance, chart routing, uncertainty, accessibility, vector export, and final-PDF inspection. The candidate therefore does not justify a second plotting Skill. Its genuine additions are the explicit publication medium, final physical size, panel budget, and separation of conceptual artwork from exact scientific labels and data marks.

One candidate pattern recommended narrowing bar-chart axes to emphasize small differences. That rule conflicts with magnitude-faithful bar encoding and was deliberately rejected. When a nonzero range is scientifically important, use a dot, interval, slope, or line representation, or disclose the truncation clearly rather than importing it as a default.

### `Anatomy`

The reusable idea is not the web stack. It is the integrity constraint that one underlying model must determine every visible part, relation, state, annotation, and caption. `technical-diagrams` now permits an embodied mechanism illustration only when the mapping is explicit and the static paper export remains complete without interaction.

### `Supervisor-Skills`

The repository contains many Skills that overlap existing canonical owners. The strongest missing mechanism was its idea-evaluation discipline: an idea is not scored as strong until the path to implement and test it is concrete. `model-deliberation` now records the limiting fatal flaw, current tier, and next-tier actions. The pre-submission reviewer also contributed a one-to-one evidence chain from claimed contribution to method component and isolating validation. The figure designer contributed the distinction among motivating example, solution overview, and quantitative result figures.

## Licensing and copying boundary

- `Anatomy` is MIT-licensed according to its repository metadata.
- `Supervisor-Skills` states CC BY-NC-SA 4.0 for the repository.
- `figures4papers` describes mixed repository/content licensing in its README.

Only high-level mechanisms were independently paraphrased and integrated. No third-party template, code block, image asset, generated example, or long instruction passage was copied into `mathskills`.
