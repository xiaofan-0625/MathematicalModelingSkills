# Problem Forensics Protocol

Use this protocol for G1 and whenever downstream work suggests the task was misread.

## Two-pass reading

### Pass A: structural extraction

Create a row for every subproblem with:

| Field | Required content |
|---|---|
| `question_id` | Stable identifier matching the statement |
| `action` | Estimate, predict, optimize, rank, explain, design, simulate, or prove |
| `decision_or_quantity` | Exact output to determine |
| `inputs` | Official data and results inherited from earlier questions |
| `hard_constraints` | Conditions whose violation makes an answer invalid |
| `evaluation` | Metric or qualitative criterion stated or safely inferred |
| `granularity` | Entity, location, time step, scenario, and precision |
| `deliverables` | Number, table, figure, plan, formula, code, or discussion |
| `downstream` | Later questions that consume this output |

Also inventory global rules: page and file limits, anonymity, required declarations, accepted formats, naming rules, and submission deadline. Attach a source location to each.

### Pass B: adversarial reading

Search specifically for:

- `all`, `at least`, `at most`, `only`, `except`, `respectively`, and negation;
- whether a quantity is a stock, flow, rate, probability, count, or cumulative total;
- calendar time versus elapsed time, and what information existed at the decision point;
- hard constraints disguised as prose examples;
- local versus global, discrete versus continuous, expected versus worst-case claims;
- required comparison groups, units, uncertainty, or rounding rules;
- whether a later question requires preserving intermediate outputs from an earlier one.

## Ambiguity register

Use one entry per ambiguity:

```yaml
id: A-01
statement_location: "page/paragraph/table"
text: "verbatim fragment"
interpretations:
  - reading: "..."
    consequences: "variables, constraints, data, or conclusion affected"
evidence: ["official wording or correction"]
discriminating_test: "small example or contradiction that separates readings"
adopted: "... or unresolved"
rationale: "..."
risk_if_wrong: low|medium|high
```

Do not silently choose the reading that makes computation easiest. Ask the user only when official material cannot resolve a high-impact choice and different readings would produce materially different work.

## Data attachment contract

For each table or file record:

- role and relation to a subproblem;
- encoding, sheet, row count, keys, field types, units, time zone, and coverage;
- missingness, duplicates, impossible values, censored or derived fields;
- join cardinality and possible fan-out;
- target leakage, post-outcome information, or future data exposure;
- organizer definitions that differ from ordinary domain usage.

Do not alter the original attachment. Any corrected or derived dataset must identify its source version and transformation code.

## Minimal contract layout

`problem_contract.md` should contain: official-source inventory, global rules, subproblem matrix, constraint ledger, ambiguity register, dependency graph, team-introduced assumptions, and open decisions. `data_audit.md` owns the attachment schema and quality evidence; do not duplicate it in the contract.
