# Find Skills Modeling Audit

Search dates: 2026-11-24 to 2026-11-25. Discovery command: `npx --yes skills find "<query>"`.

This audit records discovery and design decisions. No third-party Skill was installed into the user environment, no candidate command was executed, and `skills大全` was read only. Install counts are approximate observations at search time, not quality scores or endorsements.

## Search coverage

| Query | Representative result at search time | Observed installs | Decision |
|---|---|---:|---|
| `mathematical modeling competition` | `bzdmathclub/bzd-math-modeling-skills@bzd-ai-usage-disclosure` | 17 | Added a stricter, rule-first `ai-use-disclosure`; rejected duplicate generic workflow/review/format modules |
| `time series forecasting backtesting` | `k-dense-ai/scientific-agent-skills@timesfm-forecasting` | 2.2K | Added tool-neutral forecasting and rolling-backtest protocol; no model is privileged |
| same query | `jeremylongshore/...@forecasting-time-series-data` | 172 | Used as demand signal; generic forecasting overlap was distilled, not copied |
| same query | `sports-data-hq/...@walk-forward-validation` | 6 | Adopted the temporal-validation idea, generalized beyond sports |
| `monte carlo uncertainty quantification` | `k-dense-ai/scientific-agent-skills@uncertainty-and-units` | 1.3K | Added uncertainty-source, dependence, propagation and reporting gates |
| same query | `omer-metin/...@monte-carlo` | 127 | Added convergence and replication discipline, without a tool dependency |
| same query | `microsoft/cat-agent-skills@monte-carlo-analysis` | 12 | Corroborating candidate only |
| `geospatial analysis geopandas` | `davila7/claude-code-templates@geopandas` | 408 | Added CRS, geometry, join, scale and spatial-validation gates |
| same query | `kalarislabs/research-agent-skills@geomaster` | 109 | Corroborating candidate; no second spatial module |
| `network graph analysis networkx` | `k-dense-ai/scientific-agent-skills@networkx` | 2.3K | Added graph-contract, null-model and structural-robustness protocol |
| same query | `jaechang-hits/sciagent-skills@networkx-graph-analysis` | 72 | Corroborating candidate; library API was not copied |
| `scientific table generation` | `lingzhi227/agent-research-skills@table-generation` | 1.7K | Added provenance-first scientific tables and final-PDF readability gate |
| `multi objective optimization pymoo` | `k-dense-ai/scientific-agent-skills@pymoo` | 2.2K | Enhanced `model-formulation-and-solving`; rejected a duplicate generic optimizer Skill |
| same query | `davila7/claude-code-templates@pymoo` | 300 | Corroborating candidate only |
| `AI usage disclosure research` | `bzdmathclub/bzd-math-modeling-skills@bzd-ai-usage-disclosure` | 17 | Added internal ledger plus official-format reconciliation |
| `queueing simulation operations research` | `yuuqq/research-grade-skills@simpy` | 1 | Queueing was included inside simulation rather than as a narrow library Skill |
| `causal inference econometrics` | no direct match | 0 | No sourced module added; existing evidence and validation rules remain |

## Second-round search and merge decisions

| Query family | Representative candidates observed | Mechanisms extracted | Decision |
|---|---|---|---|
| `mathematical modeling skill` | `zhnnky329/mathmodeling-skills` (problem classifier, method selector, reference manager, consistency auditor, quality auditor, figure-table planner); `yushui2022/mathmodel-skill`; `bzdmathclub/bzd-math-modeling-skills` | stage labels, model routing, symbol/notation checks, paper and figure QA | Added only the missing formal evidence-review layer; merged the rest into existing canonical modules |
| `scientific research skill literature review` | `k-dense-ai/scientific-agent-skills@literature-review` (2.7K); `bytedance/deer-flow@academic-paper-review` (2.8K); `brycewang-stanford/auto-empirical-research-skills@literature-review` | source screening, review modes, synthesis, paper evaluation | Added `systematic-evidence-review`; kept paper review in `competition-scoring` and `math-modeling-paper-review` |
| `research data analysis skill` | `lingzhi227/agent-research-skills@data-analysis` (2.1K); `k-dense-ai/scientific-agent-skills@statistical-analysis` (2.6K); `vincenzoimp/academic-research-skills@research-data-analysis` | audit, analysis, visualization, reproducibility | Existing `data-analysis`, `validation-and-robustness`, and `reproducibility-audit` already cover the decision surface; no duplicate module |
| `reproducible research / open notebook` | `k-dense-ai/scientific-agent-skills@open-notebook` (2.2K); academic research suite deep-research references | resumable state, preregistration, source provenance, code/data landscape | Added the formal-review artifacts and gates to the new module; existing G5/G7 remain owners of rerun and package checks |
| `scientific writing / paper / figure` | paper section writer, paper polisher, figure-table planner, modelviz candidates | section order, symbol table, figure/table planning, consistency checks | Merged into existing writing, visualization, scientific-tables, and reproducibility modules |
| WeChat public-web searches | verified or traceable articles from 佬刘AI、卡尔的 AI 沃茨、iDS智能设计系统小助手、AI信息Gap and two additional account listings | query translation, source merging and de-duplication, independent identity checks, access-level honesty, claim audit, research passport, data/statistics audit | Strengthened `literature-evidence`, `systematic-evidence-review`, G1.5, and ledger validation; no duplicate recommendation-list module |

## Local read-only references inspected

- `scientific-agent-skills/skills/timesfm-forecasting/SKILL.md`;
- `scientific-agent-skills/skills/uncertainty-and-units/SKILL.md`;
- `scientific-agent-skills/skills/simpy/SKILL.md`;
- `scientific-agent-skills/skills/geopandas/SKILL.md`;
- `scientific-agent-skills/skills/networkx/SKILL.md`;
- `scientific-agent-skills/skills/pymoo/SKILL.md`;
- `agent-research-skills/skills/table-generation/SKILL.md`.

These sources were treated as untrusted reference material. Version-specific installation steps, platform commands, large code examples, credentials, remote downloads, and tool-specific API catalogs were excluded.

## Inclusion test

A candidate mechanism was added only if it:

1. closes a distinct mathematical-modeling failure mode not already covered;
2. changes a real modeling, validation, reporting, or compliance decision;
3. can be expressed independently of one package or vendor;
4. produces auditable artifacts and has a meaningful gate;
5. does not weaken official-rule priority, evidence traceability, or user control.

The resulting additions are `forecasting-and-backtesting`, `simulation-and-uncertainty`, `geospatial-modeling`, `network-modeling`, `scientific-tables`, `ai-use-disclosure`, and `systematic-evidence-review`. Multi-objective optimization was integrated into the existing solver module because a separate generic Skill would duplicate formulation, feasibility, termination, and validation rules. GitHub's HTML/API endpoints were attempted but timed out in this environment; repository names and install counts were treated as discovery signals, while detailed mechanisms were accepted only when corroborated by the local read-only reference collection.

The later WeChat audit corrected the initial conclusion that no useful public-account material was verifiable. The dated titles, account names, verification grades, exclusions, and mechanism-level merge decisions are recorded in [wechat-research-skills-audit.md](wechat-research-skills-audit.md). Article popularity was treated only as a discovery signal; primary repository bodies and auditable mechanisms remained the adoption requirement.

## User-selected candidate review

On 2026-11-25, `figures4papers`, `Anatomy`, and `Supervisor-Skills` were reviewed against the workbook and their primary repositories. No repository was installed or executed. The review strengthened idea evaluation, contribution-evidence tracing, figure role selection, final-size planning, and semantic mechanism diagrams without adding duplicate canonical modules. Exact adoptions, exclusions, and licensing boundaries are recorded in [selected-candidate-skills-audit.md](selected-candidate-skills-audit.md).
