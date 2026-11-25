---
name: problem-forensics
description: Convert a mathematical-modeling competition statement and official rules into a traceable task contract, ambiguity register, deliverable matrix, and data requirements. Use before modeling or when a solution may have misread the problem.
---

# Forensically Interpret the Problem

Treat the original statement and current competition rules as evidence. Do not infer the intended task from a familiar problem type, prior paper, translation, or forum solution.

## Workflow

1. Inventory every official file, attachment, correction, deadline, format rule, and stated evaluation target. Record versions and unresolved access failures.
2. Read twice: first for structure, then adversarially for quantifiers, scope, units, time order, exceptions, and required outputs.
3. For each subproblem, extract inputs, decisions, targets, hard constraints, uncertainties, output granularity, evaluation basis, and dependencies on earlier answers.
4. Build an ambiguity register. For each ambiguity list plausible readings, evidence, downstream effect, a discriminating test, and the adopted reading. Escalate only when the choice materially changes the answer.
5. Cross-check attachments against the statement: schema, units, keys, date ranges, coverage, missing tables, duplicated entities, and information that would not have been available at decision time.
6. Write `求解/计划/problem_contract.md` and `求解/数据审计/data_audit.md`. Keep assumptions introduced by the team separate from facts stated by the organizer.

## Gate

G1 passes only when every requested output maps to a model result, table, figure, or explanation; all hard constraints have planned checks; cross-question dependencies are explicit; and high-impact ambiguities are resolved or visibly blocked.

Read [problem-forensics.md](../../references/problem-forensics.md) for the extraction schema and adversarial checks. Route file-specific data inspection to `data-analysis`; this Skill owns interpretation, not statistical exploration.
