# Workflow Gates

Use these gates only to the depth required by the current mode. `solve` normally proceeds in order; `review`, `repair`, `score`, and `deliver` may enter later and trace failures upstream. A file's existence never proves a gate passed.

## Gate record

For each attempted gate, record in `求解/project_state.yaml`:

- status: `not_started`, `in_progress`, `passed`, `failed`, or `blocked`;
- evidence: artifact paths and, where useful, section, table, figure, or run identifiers;
- decision: what was accepted and by whom when user choice was required;
- unresolved: risks that remain visible downstream;
- next action and the stage that owns it.

## Universal route-back rule

Every `Route back when` condition opens a revision event before the repair begins. Record the
earliest affected gate, changed inputs or artifacts, invalidated downstream gates, replay Skills,
and closure evidence in `求解/计划/rework_log.jsonl`. Mark affected Skill records and artifacts
`superseded`; a stale file remaining on disk is not valid evidence. After repair, replay every active
Skill in the dependency cone, rerun the affected gates in order, regenerate frozen values and all
consumers, then close the event. The detailed impact matrix is in
[`skill-coverage-and-rework.md`](skill-coverage-and-rework.md).

## G0: launch and protection

**Inputs:** user request, official files, available runtimes, deadline, compute and interaction budget.

**Required evidence:** protected-path inventory; input hashes or version notes; project metadata; operating mode; planned checkpoints; recovery path; applicable AI-use rule record; `求解/计划/skill_use_ledger.json` with one applicability decision for every canonical Skill; and an initialized `求解/计划/rework_log.jsonl`.

**Pass:** scope and non-goals are explicit, original inputs are protected, required tools are known or a degradation path is recorded, every canonical Skill is `active` or `not_applicable` with a reason, and the next bounded action is clear.

**Route back when:** a later official correction, missing attachment, rule change, or Skill-trigger decision alters scope. Record the return in `rework_log.jsonl` before editing downstream artifacts.

## G1: problem forensics and data contract

**Inputs:** original statement, rules, attachments, organizer corrections, and any proposed external data requirement.

**Required evidence:** `求解/计划/problem_contract.md`; `求解/数据审计/data_audit.md`; subproblem deliverable matrix; ambiguity register; cross-question dependency map. When external data are used, also require a source contract, immutable raw snapshot, acquisition manifest, field dictionary, coverage checks, and join audit under `求解/数据审计/外部数据/`.

**Pass:** each requested deliverable maps to planned evidence; objective, hard constraints, time order, units, and output granularity are explicit; high-impact ambiguities are resolved or blocked. Every accepted external field traces to a lawful source, exact query or file, version or vintage, raw hash, and checked transformation path.

**Route back when:** the model answers a convenient proxy rather than the requested quantity, attachment semantics do not match the interpretation, or a live external source cannot reproduce the dataset actually analyzed.

## G1.5: literature and exemplar evidence

**Inputs:** decisions that need external facts or methods; relevant exemplary papers if available.

**Required evidence:** `求解/证据/literature_map.md`; `求解/证据/citation_ledger.csv` with source passports; search log; unresolved source list; optional `exemplar_patterns.md`.

**Pass:** planned external claims are verified at an access level sufficient for the claim or visibly unresolved; central source identities are independently cross-checked; source strength, version, access depth, support location, and scope are recorded; adopted exemplar patterns are transformed rather than copied.

When the request is a formal literature review, deep research, evidence map, or systematic review, also require `review_protocol.md`, `source_screening.csv`, a literature matrix, a source-quality report, a synthesis/gaps report, and a documented mode-appropriate stopping rule. Do not impose the formal-review artifacts on a small method lookup.

**Route back when:** a source does not support the implemented method, a novelty claim was not searched, a title/abstract is used for unobserved details, or only a search snippet was treated as verified evidence.

## G2: modeling blueprint

**Inputs:** problem contract, data audit, evidence map, computational constraints.

**Required evidence:** legal baseline; candidate decision matrix; variables, units, assumptions, equations and interfaces; solver and validation plan; failure conditions. When the project controls assignment, data collection, algorithm comparisons, or simulation runs, also require an experiment contract, independent-unit definition, allocation or run schedule, power/MDE analysis, analysis plan, multiplicity handling, and stopping rules. When a material result requires a derivation, theorem, bound, approximation or algorithm guarantee, require a derivation contract and proof-obligation ledger.

**Pass:** the chosen formulation is implementable, testable, and sufficient for all subproblems; every assumption has purpose, impact, and a planned challenge. Controlled comparisons have an estimable target, correct replication level, reproducible assignment, and an analysis model that matches the design. Proof-critical claims have an exact target, stable notation, explicit assumptions, dependency map and counterexample plan.

**Route back when:** feasibility, identifiability, boundedness, data availability, inter-question dependency, independent replication, or experimental estimability fails.

## G3: implementation and solving

**Inputs:** approved blueprint and frozen input versions.

**Required evidence:** deterministic code or documented environment; raw output; run log; solver diagnostics; independent constraint checks; small-instance or alternate check where feasible. Specialized models also preserve forecast origins, simulation replications, spatial CRS/join audits, graph construction metadata, realized experimental assignment and protocol deviations, or derivation/proof reports with open obligations as applicable.

**Pass:** the code implements the documented model, returns legal outputs, records stopping conditions and seeds, and does not overstate solver guarantees.

**Route back when:** solver success hides constraint violations, results depend on notebook state, or code and equations diverge.

## G3.5: validation and result freeze

**Inputs:** baseline and candidate outputs under a shared evaluation protocol.

**Required evidence:** baseline comparison; sensitivity or uncertainty analysis; at least one failure-oriented test; appropriate ablation, stress test, holdout, or bound; `validation_report.md`; machine-readable `frozen_numbers.json`. For designed experiments, reconcile realized sample structure with the predeclared estimand, exclusions, multiplicity and stopping rule before inference.

**Pass:** the evidence supports the strength of every headline conclusion, reversal conditions are stated, and invalidated results are not frozen.

**Route back when:** leakage, instability, implausible sensitivity, failed conservation or feasibility checks, or a stronger baseline overturns the result.

## G4: figures, diagrams, and paper

**Inputs:** frozen numbers, verified citations, accepted model and limits.

**Required evidence:** editable figure and diagram sources; machine-readable plot and table data; deterministic table transformations; paper source; tables; appendices; cross-reference and claim mapping.

**Pass:** each subproblem closes with method, result, validation, and boundary; every visual answers a question; all reported numbers consume frozen results. Formula, theorem, approximation and guarantee wording matches the completed proof obligations and declared status.

**Route back when:** prose creates a new claim, a visual conflicts with its source data, or layout hides uncertainty.

## G5: compile, visual QA, and reproducibility

**Inputs:** paper source, code, manifest, documented environment.

**Required evidence:** clean compile log; final PDF; page-by-page visual inspection; clean or bounded rerun; `artifact_manifest.json`; `reproducibility_report.md`; cross-file consistency report. External data manifests, raw hashes, vintages and transformation commands must be reachable from the artifact graph.

**Pass:** the final PDF is readable, references resolve, rerun results match declared tolerances, and all headline artifacts trace to producing inputs and code.

**Route back when:** compilation uses stale output, fonts or equations are broken, rerun fails, or paper values diverge from the manifest.

## G6: adversarial judge review

**Inputs:** final-form PDF and all auditable support files.

**Required evidence:** hard-gate results; evidence-linked `scorecard.json` and report; issue ledger with severity and repair owner; corrected version and targeted rechecks. Headline claims must pass paper-to-evidence integrity checks; proof-critical claims must expose open, repaired or refuted obligations.

**Pass:** integrity and rule gates pass; no blocking issue remains; score arithmetic is valid; unresolved limitations are visible in the paper.

**Route back when:** any issue points to an upstream factual, mathematical, computational, or evidence failure.

## G7: submission package

**Inputs:** accepted revision and current official delivery rules.

**Required evidence:** `提交/` contents; compliance checklist; relative-path manifest; SHA-256 hashes; clean archive extraction check; final PDF open check; AI-use ledger and declaration reconciliation when applicable.

**Pass:** every official requirement maps to evidence, the archive contains exactly the allowed files, anonymity is satisfied, and extracted contents match the manifest.

The G7 gate also requires no open rework event and no `pending`, `blocked`, `superseded`, or
incomplete `active` Skill record. Every passed gate, frozen value, figure, table, paper, scorecard,
manifest and hash must belong to the current revision.

Packaging completion is not proof of external upload. Record upload or receipt only when actually observed.
