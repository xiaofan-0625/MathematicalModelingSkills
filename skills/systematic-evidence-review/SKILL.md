---
name: systematic-evidence-review
description: Run a scoped, auditable literature or evidence review for a mathematical-modeling project, from question and search protocol through source screening, deep reading, evidence matrices, bias checks, synthesis, and gap analysis. Use when the user requests deep research, a systematic review, a formal literature review, or an evidence map; use literature-evidence alone for a small method lookup.
---

# Systematic Evidence Review

Use this module when a modeling decision genuinely depends on a structured body of literature. It is a controlled research workflow, not a requirement to collect many citations for every competition problem. The official problem statement and current competition rules remain higher authority than any paper.

## Choose the lightest review mode

Select the smallest mode that answers the request and record the choice:

- **fact-check**: verify a few claims against authoritative sources;
- **three-way scan**: compare a small candidate set using WHY / HOW / WHAT;
- **rapid brief**: bounded search for a decision memo;
- **narrative review**: thematic map and synthesis without claiming exhaustive coverage;
- **systematic review**: pre-specified question, search, screening, extraction, quality appraisal, and transparent flow;
- **evidence map**: organize methods, assumptions, data settings, and gaps when quantitative pooling is not appropriate.

Do not call a review “systematic,” “comprehensive,” or “state of the art” unless the protocol, search coverage, screening decisions, and stopping rule support that claim.

## Protocol before search

Write `求解/证据/review_protocol.md` before broad searching. Include:

- the decision or modeling question, population/system/context, intervention or method, comparator/baseline, outcomes, and eligible study designs;
- in-scope and out-of-scope boundaries, language/date limits, databases or repositories, search strings, and access constraints;
- inclusion and exclusion criteria that can be applied consistently;
- primary extraction fields: problem, data, variables, assumptions, equations/algorithm, evaluation, result, limitations, code/data availability, and relevance to this project;
- planned quality or risk-of-bias checks, synthesis type, subgroup or sensitivity analyses, and how deviations will be recorded;
- a stopping rule: stop only when the method decision is stable, closest relevant sources are mapped, and unresolved gaps are visible.

For confirmatory experiments, multiple testing, secondary analysis, or a formal systematic review, consider preregistration. A plan or template is not proof that registration occurred; record `not_registered`, `registered`, or `unknown` with evidence.

## Search and source control

1. Search at least two independent channels when available: a primary publisher/repository record plus a scholarly index, official documentation, or authoritative handbook. Add a third channel for central, contested, or fast-moving claims.
2. Keep a search log with query, channel, date, filters, result count if observable, access status, and changes to the query. Do not silently discard inconvenient results.
3. De-duplicate by DOI, stable identifier, title, and author-year fallback. Mark preprints, conference papers, reports, tutorials, search snippets, and secondary summaries distinctly.
4. Add a source passport for every retained item: stable identity, version or publication status, access level, discovery and verification channels, exact support location, eligible scope, and planned use. Distinguish `metadata_only`, `snippet`, `abstract`, `partial_text`, and `full_text`.
5. Verify bibliographic identity and read the relevant section, table, or figure before using a source to support a method, number, assumption, or novelty claim. A title or abstract alone cannot establish implementation details.
6. Grade source fitness on separate axes: study/design quality, peer review, methodology, data/sample, currency relative to the claim, conflicts, and domain fit. A high-prestige venue does not rescue a mismatched or flawed method; a qualitative or domain-specific source is not automatically weak merely because it is not an experiment.

## Screening, extraction, and deep reading

Maintain `求解/证据/search_log.csv`, `求解/证据/source_screening.csv`, and `求解/证据/literature_matrix.csv` or an equivalent machine-readable table. Every excluded candidate gets a reason when systematic coverage is claimed.

For each retained source, record the exact passage or location supporting the claim, not only a summary. Read full text for the sources that determine the model choice or contribution. For each deep-read source capture:

- question and setting;
- data-generating process, sample, units, and information available at decision time;
- model/algorithm and assumptions;
- baseline, metrics, validation, uncertainty, and failure cases;
- code/data availability and reproducibility risks;
- what transfers to this problem, what does not, and the proposed adaptation test.

Build a source-by-theme matrix that distinguishes support, contradiction, partial evidence, and not addressed. Summarize convergence, disagreement, methodological and geographic gaps, stale evidence, and missing code/data. Seek disconfirming evidence deliberately to reduce cherry-picking and confirmation bias.

## Synthesis and handoff

Choose the synthesis that matches the evidence:

- direct method comparison when tasks and metrics are comparable;
- structured narrative synthesis when settings or outcomes differ;
- quantitative pooling only when estimands, scales, dependence, and uncertainty are compatible;
- gap map when the goal is to decide what is unknown rather than to rank methods.

Never pool incompatible metrics or treat independent papers as independent experimental replicates without checking overlap and design. Do not infer causality from correlation, post hoc ordering, group-level association, or a method's popularity. Run a final argument audit for cherry-picking, hasty generalization, survivorship bias, Simpson's paradox, Goodhart effects, and appeal to novelty.

Hand off only verified claims and clearly labeled limitations to `literature-evidence`, `model-deliberation`, and the modeling blueprint. The review may inform a candidate, assumption, baseline, parameter range, or validation test; it cannot replace the data audit, executable experiment, proof, or solver check.

## Outputs and gate

Minimum outputs for a formal review:

- `review_protocol.md`;
- `search_log.csv` and `source_screening.csv`;
- `literature_matrix.csv` or equivalent;
- `source_quality_report.md`;
- `synthesis_and_gaps.md`;
- updated `citation_ledger.csv` with claim-level locations and verification status.

G1.5 passes only when the review mode is appropriate, the search and screening process is auditable, central sources were read deeply enough, contradictory evidence was considered, and every adopted claim has a bounded scope. If external access fails, downgrade the evidence and leave the unresolved source visible.
