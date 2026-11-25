---
name: external-data-acquisition
description: Acquire, snapshot, document, and join external public data for mathematical-modeling projects. Use when a task needs API, portal, webpage, repository, or secondary-dataset evidence beyond supplied attachments; do not treat a live query or copied table as a reproducible input.
---

# Acquire External Data Reproducibly

External data is part of the model input, not background decoration. Preserve the exact response, query, version, coverage, licence, and transformation path needed to reproduce every field used by the model.

## Workflow

1. Write a minimum data contract before searching: decision or claim served, variables, units, population, geography, time range, frequency, acceptable latency, and required authority.
2. Prefer the strongest source that actually owns the fact: official organizer or agency release, official API or bulk download, maintained scholarly or institutional repository, then a documented aggregator. Use search results and unofficial mirrors only to discover a primary source.
3. Check access and use boundaries before acquisition. Record licence, attribution, redistribution limits, authentication needs, rate limits, robots or terms constraints, and whether automated retrieval is permitted. Never store credentials or session tokens in the project.
4. Save an immutable raw snapshot before cleaning. Record source URL or endpoint, method, query parameters, pagination, response format, retrieval time and timezone, release or vintage, HTTP status when applicable, file size, and SHA-256 hash.
5. Create a field dictionary covering original name, meaning, unit, type, code system, missing-value convention, time semantics, geography, and any revision policy. Distinguish event date, observation date, publication date, and retrieval date.
6. Validate completeness: page counts, record counts, date and geography coverage, duplicate keys, suppressed values, schema drift, revisions, and gaps. Compare a sample against the source interface or an independent official total.
7. Transform only from the preserved snapshot. Log parsing, filtering, resampling, unit conversion, deflation, geocoding, code mapping, and aggregation. Keep raw and derived data separate.
8. Audit every join with declared keys, expected cardinality, unmatched rows, duplicate expansion, temporal alignment, and leakage risk. Do not silently forward-fill revisions or combine incompatible vintages.
9. Freeze the accepted dataset version. Link every external variable used by the model to its source-manifest entry and transformation code.

## Source-specific cautions

- Economic and market series can be revised. Preserve the vintage available at the modeled decision date when historical realism matters.
- Cross-country or regional portals often change definitions across places and years. Verify concept, unit, population base, and boundary changes before comparing values.
- Scholarly indexes are discovery and metadata sources; they do not replace claim-level full-text verification.
- Domain databases may use identifiers, licences, access tiers, or update cycles that require specialist interpretation. Apply this Skill's provenance contract without pretending a generic adapter validates domain meaning.
- Scraping is a last resort. Prefer a documented export or API; if scraping is necessary and permitted, preserve the page snapshot, selector assumptions, and failure checks.

## Required outputs

Write under `求解/数据审计/外部数据/`:

- `source_contract.md`: required fields, source-selection rationale, authority and coverage;
- `acquisition_manifest.json`: query, version, retrieval, licence, hashes and file paths;
- immutable raw responses or files plus derived analysis data;
- `field_dictionary.csv` and `join_audit.csv` when applicable;
- acquisition code and a short verification report.

The gate passes only when each used external field traces to an immutable snapshot and reproducible query or download, coverage and joins are checked, licences and restrictions are visible, and no secret is embedded. If live retrieval cannot be repeated, preserve the strongest lawful snapshot and mark the limitation.

Read [external-data-acquisition.md](../../references/external-data-acquisition.md) for the manifest schema, source ladder, and acceptance checklist.
