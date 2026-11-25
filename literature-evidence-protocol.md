# Literature and Evidence Protocol

Use this protocol only for sources needed by the current modeling decision. It is adapted from the source-grounded literature and citation workflows in `skills大全`; it is not a license to ingest or execute third-party repositories.

## Evidence ledger schema

Store one row per externally checkable claim in `求解/证据/citation_ledger.csv`:

```text
claim_id,claim_text,claim_type,source_key,source_identifier,source_url,source_version,publication_status,access_level,verification_channels,location,scope,used_in,verification_status,checked_on,notes
```

Recommended `claim_type` values are `method`, `domain_fact`, `benchmark`, `assumption`, `limitation`, and `novelty`. Recommended `verification_status` values are `verified`, `partial`, `unverified`, and `not_applicable`.

Use DOI, arXiv ID, report number, dataset ID, or a stable official URL for `source_identifier`. Recommended `access_level` values are `metadata_only`, `snippet`, `abstract`, `partial_text`, and `full_text`. Store independent discovery or verification channels in `verification_channels` separated by semicolons. `location` must name the supporting page, section, table, figure, appendix, code file, or official field when the claim is verified. Together, the identity, version, access, verification channel, support location, scope, and use location form the source passport.

## Search and stopping rules

Search at least two independent source channels when external search is available: a primary publisher or repository record and a scholarly index, handbook, or official data documentation. Add a third channel when the claim is central to the model, contested, or likely to have a newer version.

Stop only when:

- the selected method has a primary or authoritative source;
- the main domain facts have a source and scope note;
- the closest 3-8 sources relevant to the contribution or model choice are mapped;
- each unresolved item is visible in the ledger; and
- a reasonable new search is no longer changing the model decision.

## Verification rules

- Match author, title, year, venue, DOI or stable URL, and version against the source record.
- Use one channel to discover a source and an independent channel to verify its identity when available. Central, contested, numerical, or fast-moving claims normally require a third check or an explicit unresolved status.
- Read the relevant full-text section before claiming method details, equations, data construction, limitations, or comparison results; read the table or figure when quoting a number. Abstract-only access permits only claims actually stated in the abstract.
- Prefer the published version over an older working paper when the two exist.
- Preserve uncertainty when only metadata, a snippet, an abstract, partial text, or a secondary source is available. Never label such a record `full_text` or imply that the unobserved body was checked.
- Never fabricate a DOI, page, quotation, dataset provenance, or benchmark.

## Model-facing use

The evidence map must change a decision or make the decision more defensible. If it does neither, keep the source in a background note rather than inflating the reference list. A literature map is not a substitute for a data audit, a validation run, or a proof of causality.
