# Skill Coverage and Rework Protocol

This document is the operational contract for using every canonical `mathskills` module in a
real mathematical-modeling project. It solves two different problems:

1. **Coverage:** every canonical Skill is considered at G0 and recorded as `active` or
   `not_applicable` with a reason. Conditional Skills are not forced into an irrelevant problem,
   but they may not be silently forgotten.
2. **Rework:** changing an upstream fact, source, design, model, result, claim, figure, or package
   invalidates the affected downstream artifacts. The project returns to the earliest affected
   gate, preserves the previous revision, and replays every required check before freezing again.

## 1. Skill-use ledger

Create `求解/计划/skill_use_ledger.json` during initialization. The ledger is the authoritative
record of module applicability and use. It must contain exactly one record for each canonical Skill
listed below. Aliases and external adapters are not additional records.

Each record contains:

```json
{
  "name": "problem-forensics",
  "status": "active",
  "trigger_checked": true,
  "planned_stages": ["G1"],
  "stage_status": {"G1": "pending"},
  "trigger": "题面、附件或规则需要结构化解释",
  "reason": "本题有四个子问题和两个附件，需要交付矩阵与歧义登记",
  "required_outputs": ["求解/计划/problem_contract.md"],
  "owner": "workflow-orchestration",
  "invocations": [],
  "last_revision": 0,
  "evidence": []
}
```

Allowed statuses are:

- `pending`: initialized but not yet decided; it blocks G0 completion.
- `active`: required for this project and must leave evidence in its listed stage.
- `not_applicable`: deliberately skipped with a concrete reason and a recorded trigger check.
- `blocked`: applicable but waiting for an explicit user decision, missing input, or external
  capability; it blocks the owning gate.
- `complete`: active work passed its acceptance checks for the current revision.
- `superseded`: an earlier invocation was invalidated by rework; a new invocation is required.

For a normal `solve` project, G0 may pass only when every record is `active` or
`not_applicable`, every active record has a planned stage and required output, and no record is
`pending` or `blocked`. A conditional Skill can be marked `not_applicable` only after its trigger
was checked. For example, a problem with no temporal target may mark forecasting as not applicable;
it may not omit the row.

An `active` record is evaluated stage by stage. `stage_status` uses `pending`, `complete`,
`not_applicable`, or `superseded`. `validate_project.py --through G3` requires every planned
G0–G3 invocation to be complete for the current revision; a later planned invocation may remain
pending. One early call therefore cannot satisfy all later review and repair duties of the same
Skill.

## 2. Canonical coverage matrix

| Canonical Skill | Default stage(s) | Activate when | Minimum evidence | Typical rework trigger |
|---|---|---|---|---|
| `workflow-orchestration` | G0–G7 | Any multi-stage project | state, gate history, task contracts | any cross-stage conflict |
| `plan-and-execution` | G0, G2 | Work has multiple outputs or dependencies | plan, owners, checks, stop conditions | scope, owner, dependency or deadline changes |
| `ai-use-disclosure` | G0, G7 | AI, search, coding assistant, translation, or model API contributes | rule record, use ledger, declaration | official rule or material-use change |
| `problem-forensics` | G1 | The statement has subproblems, constraints, data or ambiguity | problem contract, deliverable matrix, ambiguity log | corrected statement, attachment semantics, target/constraint change |
| `data-analysis` | G1, G3 | Any supplied data require audit, cleaning, EDA or statistical analysis | data audit, transformation log, diagnostics | source version, cleaning rule, variable definition or leakage change |
| `external-data-acquisition` | conditional | Public API, portal, webpage or secondary dataset is used | source contract, raw snapshot, field dictionary, join audit | query, vintage, source, schema, coverage or join change |
| `literature-evidence` | G1.5 | Any external method, fact, assumption or novelty statement is used | search log, source passport, citation ledger | source identity, access level, method interpretation or novelty change |
| `systematic-evidence-review` | conditional | Deep research, formal review, evidence map or state-of-the-art claim is requested | protocol, screening, matrix, synthesis and stopping rule | search boundary, inclusion rule or synthesis change |
| `exemplar-distillation` | G1.5 | Exemplary papers or award corpus inform structure or validation | provenance and transferable pattern table | selected exemplar, pattern interpretation or venue constraint change |
| `model-deliberation` | G2 | Multiple formulations, innovations or assumptions compete | candidate matrix, objections, decision log | new candidate, counterexample or feasibility objection |
| `model-formulation-and-solving` | G2, G3 | A mathematical model is formulated or solved | blueprint, equations, solver contract, diagnostics | variable, objective, constraint, solver, implementation or resource change |
| `mathematical-derivation-and-proof` | conditional | A material conclusion uses a nontrivial derivation, theorem, bound, approximation or guarantee | derivation contract, obligation ledger, audit report | assumption, quantifier, formula, theorem condition or claim-strength change |
| `experimental-design-and-inference` | conditional | Assignment, data collection, algorithm comparison or simulation is controlled prospectively | experiment contract, allocation, estimand, power and analysis plan | unit, randomization, split, stopping, multiplicity or estimand change |
| `measured-experiment-loop` | G3.5 | Candidate configurations are iterated under a fixed metric and budget | contract, baseline, append-only events and raw outputs | search space, budget, seed, metric, guard or acceptance rule change |
| `forecasting-and-backtesting` | conditional | Target or decision is ordered in time or predicts a future horizon | forecast contract, origins, baselines, rolling results | cutoff, horizon, covariate availability or backtest split change |
| `simulation-and-uncertainty` | conditional | Random inputs, scenarios, queues, events or uncertainty propagation matter | study contract, seeds, replications, convergence and tails | distribution, seed policy, replication count or scenario set change |
| `geospatial-modeling` | conditional | Coordinates, regions, routes, rasters, adjacency or geographic distance matter | CRS decision, geometry audit, joins, spatial split and derived layers | CRS, geometry repair, distance metric, scale or neighborhood change |
| `network-modeling` | conditional | Nodes, edges, paths, flows, communities or diffusion matter | graph contract, construction metadata, null model and perturbation | node/edge definition, direction, weight, threshold or graph scope change |
| `jupyter-live-analysis` | conditional | Stateful exploration or visible notebook state materially helps | notebook, executed cells, exported inputs and clean rerun path | notebook state, hidden variable, exploratory transformation or plot input change |
| `sql-data-analysis` | conditional | A relational database or SQL schema is part of the input | schema snapshot, query, plan/check and exported result | schema, join, filter, aggregation or query-plan change |
| `validation-and-robustness` | G3.5, G6 | Any candidate model has results that will be recommended or claimed | baseline, failure test, sensitivity, robustness report, frozen values | validation failure, new baseline, leakage, instability or reversal condition |
| `scientific-visualization` | G4 | A data-bearing figure is needed or an existing figure is reviewed | figure contract, source data/code, vector/raster output, QA | frozen values, aggregation, axis, uncertainty, style or size change |
| `technical-diagrams` | G4 | A route, mechanism, system, algorithm or causal structure is explained | editable diagram source, semantic mapping and visual QA | model architecture, process state, relationship or label change |
| `scientific-tables` | G4 | A descriptive, comparison, optimization, sensitivity or final-answer table is needed | machine-readable table data, units, rounding and provenance | frozen values, comparison set, denominator, precision or note change |
| `academic-writing` | G4–G6 | A paper, report, abstract, caption or reviewer response is produced | argument map, claim ledger, paper source and consistency checks | any factual, equation, result, scope or claim-strength change |
| `academic-translation` | G4–G5 | Bilingual or English publication text is requested | protected-token audit and translated source | equation, number, citation, terminology or meaning change |
| `academic-humanization` | G6 | Stable technical prose needs naturalness or authorship-voice review | protected-token audit, revised text and unresolved-language list | technical content, frozen number, claim or citation change |
| `national-award-paper-style` | G4–G5 | National competition style, template or award-paper comparison matters | style contract, layout checks and rule compliance | template, page limit, anonymity, section or figure layout change |
| `research-presentation` | G4 | Paper, results or method must be presented orally | evidence ledger, deck source, notes and rendered QA | frozen result, story order, figure, audience or time budget change |
| `reproducibility-audit` | G5–G7 | A result, paper or package is ready for delivery or has changed materially | manifest, clean rerun, cross-file consistency and report | any upstream material change, environment change or rerun failure |
| `competition-scoring` | G6 | Judge-style score, triage or rescore is requested | evidence-linked scorecard, issue ledger and confidence | any repair, hard-gate change or new evidence |
| `submission-packaging` | G7 | Final files must meet official delivery rules | manifest, hashes, clean extraction and anonymity check | any final source/file/rule/name/attachment change |

The matrix is a routing aid, not a requirement to load every file into context at once. The
orchestrator loads only the active module and its relevant references, while the ledger proves that
all modules were considered.

## 3. Rework is a controlled state transition

Never silently edit a passed artifact. Before changing it, append one event to
`求解/计划/rework_log.jsonl` and increase the project `revision`. The event must include:

```json
{
  "event_type": "rework",
  "revision": 3,
  "timestamp": "2026-11-25T12:00:00+08:00",
  "trigger": "validation_failed",
  "changed_paths": ["求解/问题2/code/model.py"],
  "root_cause": "constraint violation on boundary case",
  "earliest_affected_gate": "G2",
  "invalidated_gates": ["G3", "G3.5", "G4", "G5", "G6", "G7"],
  "invalidated_artifacts": ["求解/问题2/结果/frozen_numbers.json", "论文/论文.tex"],
  "replay_skills": ["model-formulation-and-solving", "validation-and-robustness", "academic-writing", "reproducibility-audit", "competition-scoring", "submission-packaging"],
  "decision": "repair boundary constraint and rerun all affected checks",
  "approval_required": false,
  "status": "open"
}
```

The event is closed only after the new evidence is recorded, downstream artifacts are regenerated,
and the affected gates are rechecked. The previous revision remains available for comparison; do
not delete failed, rejected, or superseded evidence.

### Impact routing

| Changed object | Earliest gate | Invalidate / replay |
|---|---|---|
| official rule, problem statement, raw attachment, project scope | G0 or G1 | recheck G0–G7 as applicable; rerun skill applicability ledger |
| external source, citation, method fact, exemplar | G1.5 | G1.5–G7; revisit model decisions and claims |
| experiment design, split, allocation, estimand, stopping rule | G1 or G2 | G2–G7; do not reuse post-change inference |
| variables, assumptions, equations, objective, constraints, solver design | G2 | G3–G7; re-open proof and validation obligations |
| code, preprocessing, seed, solver version, environment or input transformation | G3 | G3.5–G7; invalidate all affected frozen values |
| validation, baseline, sensitivity, ablation, uncertainty or frozen numbers | G3.5 | G4–G7; regenerate figures, tables, prose and score |
| figure data, table transformation, caption, equation explanation or quantitative prose | G4 | G5–G7; if meaning or claim strength changes, route back to G2/G3.5 |
| translation or style-only wording | G4/G5 | affected language and format checks; do not reopen mathematics unless meaning changed |
| compile environment, template, page layout or font | G5 | G5–G7; rerun visual QA and package checks |
| score repair or judge finding | G6 | repair the owning earliest gate, then G5–G7 and targeted rescore |
| filename, anonymity, manifest, hash or official delivery rule | G7 | G7; if source content changes, route to its earliest owner |

### Rework checklist

1. **Record before edit.** Create the event, identify the root cause, and list protected inputs.
2. **Mark stale.** Set affected gate statuses and the matching per-Skill `stage_status` entries to
   `superseded` or `in_progress`; mark affected artifacts and ledger invocations as superseded. A
   file remaining on disk is not current evidence.
3. **Return early enough.** Choose the earliest gate whose assumptions or inputs changed. Do not
   restart only the final failing command if an upstream contract changed.
4. **Replay the dependency cone.** Re-run every active Skill listed in the event and every
   downstream gate required by the impact table. Recheck conditional Skill triggers if the scope
   changed.
5. **Compare revisions.** Preserve before/after values, diagnostics, score changes, and the reason
   for accepting or rejecting the revision.
6. **Refreeze.** Update `frozen_numbers.json` only after validation passes. Regenerate all figures,
   tables, paper claims, manifests, hashes, and scores that consume changed evidence.
7. **Close the event.** Add evidence paths, gate results, revision number, and any remaining
   limitations. An open event blocks delivery.

Use `scripts/record_rework.py` to create the revision and mark replay Skills stale. After the
affected gates pass and evidence files exist, use `scripts/close_rework.py` to append the close
event and mark those replay Skills complete for the revision. These helpers record control state;
they do not decide mathematical correctness.

### Repair versus exploratory work

Exploratory trials may live in the measured-experiment log and do not change the accepted revision.
Once a trial changes the chosen model, data transformation, metric, claim, or delivered artifact,
it becomes a formal rework event and must follow the checklist above.

## 4. Completion requirements

A full `solve` project is complete only when:

- the skill-use ledger has no `pending`, `blocked`, `superseded`, or incomplete `active` record;
- every active Skill has evidence at its planned stage, and every skipped Skill has a trigger check
  and concrete reason;
- no open rework event remains;
- every passed gate belongs to the current project revision;
- frozen values, figures, tables, paper, score, manifest and hashes all refer to the same revision;
- the final clean rerun and package check were performed after the last material change.

