---
name: literature-evidence
description: Build a source-grounded evidence map for a mathematical-modeling project, including algorithm references, domain facts, assumptions, novelty positioning, and citation verification. Use before model selection or whenever a paper claim depends on external literature; do not use it to invent citations or replace the model decision.
---

# Build a Literature and Evidence Map

Connect each external claim to a source that actually supports it. Treat literature as part of the model specification: it can justify an algorithm, define an assumption, bound a parameter, or explain why a result matters.

## Workflow

1. State the question, subproblem, claim type, and the exact decision the source must inform.
2. Translate that need into searchable concepts: object or population, method, outcome, constraints, aliases, abbreviations, and Chinese/English variants. Record the exact query, channel, date, filters, and access status instead of remembering only the final paper.
3. Search through the strongest available source ladder: primary publisher, repository, DOI or official record for identity; an independent scholarly index or authoritative catalogue for discovery and cross-checking; ordinary web pages, snippets, and secondary summaries only as leads.
4. Merge and de-duplicate by DOI or other stable identifier, then by normalized title and author-year. Preserve version relationships among preprint, conference, accepted manuscript, and published article.
5. Assign an access level to every retained source: `metadata_only`, `snippet`, `abstract`, `partial_text`, or `full_text`. Read the section, table, figure, appendix, or code needed by the claim; access to a title or abstract is not access to implementation details.
6. Verify bibliographic identity against at least two independent channels when available. For a central, contested, numerical, or fast-moving claim, add a third check or leave the claim visibly unresolved.
7. Build `求解/证据/literature_map.md` with the smallest sufficient set of closest sources. For each source record the question, data or setting, method, headline result, limitation, transfer boundary, and relevance to this project.
8. For every external claim used in the report, add a source passport row to `求解/证据/citation_ledger.csv`: stable identity, version, access level, verification channels, supporting location, scope, use location, status, and check date.
9. Mark working papers, secondary summaries, inferred facts, inaccessible full text, and unresolved records explicitly. Do not present a source's suggestion as a proved result.

## Claim discipline

- Separate facts from the problem statement, assumptions introduced by the team, derived quantities, simulated values, and predictions.
- A citation supports only the claim and population it actually covers. Check sign, units, setting, and boundary conditions when quoting a result.
- Use a source for an algorithm only when it is relevant to the implemented variant; cite the primary method paper where practical.
- Use metadata or snippets only to locate and identify a source. An abstract can support a broad topic or headline conclusion, but method details, equations, sample construction, numerical values, limitations, and comparison claims normally require the relevant full-text location.
- Treat `retrieved`, `identified`, and `verified` as different states. A downloaded PDF is not verified until the claim-supporting passage is checked; a correct DOI does not prove the paper supports the sentence.
- If literature access is unavailable, create a clearly labelled placeholder and list the missing verification task. Never silently upgrade a placeholder to a real citation.

## Outputs and gate

Return the evidence map, citation ledger, unresolved-source list, and a short recommendation about how the literature changes the model choice or framing. The gate passes only when every external claim planned for the paper is verified at an access level sufficient for that claim or explicitly marked as unresolved, central identities are cross-checked, and no novelty claim depends on an unsearched or unrecorded premise.

Read [references/literature-evidence-protocol.md](../../references/literature-evidence-protocol.md) for the ledger schema and search stopping rules.
