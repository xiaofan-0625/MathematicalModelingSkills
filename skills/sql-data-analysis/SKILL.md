---
name: sql-data-analysis
description: Turn a natural-language modeling-data question plus a DDL or database schema into verified SQL and auditable summaries. Use for SQLite or relational attachments, joins, grouped statistics, and query-plan checks; do not use when the task is purely CSV analysis without a database schema.
---

# SQL Data Analysis

Treat schema linking and query verification as part of data auditing.

## Workflow

1. Read the DDL or inspect the database metadata without changing the database.
2. Identify tables, keys, units, time fields, missingness, and possible join fan-out.
3. Translate the question into an explicit target, population, grouping, filter, and ordering.
4. Generate a small number of candidate queries; quote identifiers and make joins explicit.
5. Run `EXPLAIN` or an equivalent plan check and execute against a read-only copy or in-memory
   SQLite when possible.
6. Check row counts, uniqueness, duplicate amplification, null behavior, and aggregate additivity.
7. Save the SQL, schema snapshot, verification output, and limitations under `求解/数据审计/`.

## Integrity rules

- Never update, delete, or migrate a user database as part of analysis.
- Never hide a join that changes the unit of observation.
- A syntactically valid query is not necessarily semantically valid; report unresolved schema
  ambiguity instead of guessing.
- Feed derived tables into the normal data-analysis and reproducibility stages.
