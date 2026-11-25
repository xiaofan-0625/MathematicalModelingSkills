# External Data Acquisition Contract

Use this reference when a modeling project imports public data beyond the official competition attachments.

## Source ladder

1. Official competition correction, organizer, agency, standards body, or data owner.
2. Official API, bulk download, release archive, or repository record.
3. Maintained scholarly or institutional index with stable identifiers.
4. Documented aggregator that names its upstream source and transformation.
5. Permitted webpage extraction when no structured source exists.

Choose authority and semantic fit before convenience. A polished API is not stronger evidence than the official owner of the definition.

## Minimum acquisition manifest

```json
{
  "source_id": "stable-local-id",
  "title": "dataset or series title",
  "owner": "issuing organization",
  "landing_page": "https://...",
  "endpoint_or_file": "https://...",
  "method": "GET or manual official export",
  "query": {"series": "...", "start": "...", "end": "..."},
  "retrieved_at": "2026-11-25T16:00:00+08:00",
  "release_or_vintage": "as published by source",
  "coverage": {"time": "...", "geography": "...", "population": "..."},
  "format": "csv",
  "record_count": 0,
  "sha256": "...",
  "raw_path": "求解/数据审计/外部数据/source/raw/file.csv",
  "licence": "...",
  "restrictions": "...",
  "verification": ["record count", "official total spot-check"],
  "notes": "definitions, revisions, suppressed values, unresolved risks"
}
```

Omit secrets and volatile authorization headers. Record the credential requirement separately as an environment prerequisite.

## Acceptance checklist

- The source owns or faithfully transmits the intended fact.
- Definitions, units, population, geography, frequency, timezone and vintage match the model.
- Pagination and filters are complete; a zero-row response is distinguished from a failed request.
- Raw bytes are preserved and hashed before transformation.
- Schema and code mappings are documented; revisions and suppression are visible.
- Derived files can be rebuilt from raw snapshots with recorded code.
- Join keys and cardinality are declared; unmatched and duplicated rows are quantified.
- External data do not leak future information into prediction or backtesting.
- Licence, attribution, redistribution and access limitations are recorded.
- Every paper claim using the data points to the accepted snapshot and field definition.

## Failure states

- **Live-only source:** preserve a lawful response snapshot and exact query; label future availability as uncertain.
- **Revised series:** preserve vintage information or state that only the latest vintage was available.
- **No authoritative source:** use the best documented proxy, lower the claim strength, and test sensitivity to the proxy.
- **Blocked or licensed data:** do not bypass access controls. Record the minimum replacement data or user action required.
- **Schema drift:** stop automatic append, compare old and new dictionaries, and revalidate downstream transformations.
