---
name: workflow-orchestration
description: Coordinate multi-stage mathematical-modeling work, route tasks to specialist skills, maintain state and approval gates, reconcile outputs, and handle missing capabilities. Use when the main mathskills workflow needs to invoke or emulate child skills across different AI platforms.
---

# Orchestrate Specialist Skills

Coordinate work by contracts, not by model or tool brand. Keep one owner for shared state and one canonical artifact for every result.

## Invocation protocol

For each child task, specify:

```yaml
stage: workflow stage
skill: canonical child skill
goal: one bounded outcome
inputs: files and confirmed context
protected: facts or artifacts that must not change
outputs: required files and response schema
acceptance: objective completion checks
fallback: behavior when the skill or capability is unavailable
```

## Workflow

1. Read `skills/registry.yaml` and resolve an alias to one canonical child Skill.
2. Resolve entries under `external_skills` by their declared installed name. If unavailable, execute the registered fallback and record the reduced capability.
3. Pass only the context required for the child task.
4. Prefer native Skill invocation when the platform supports it.
5. Otherwise read the canonical child `SKILL.md` and execute it in the current context.
6. Validate returned artifacts against the contract before advancing the stage.
7. Record assumptions, decisions, failures, and user approvals in the main task state.
8. Never let two child Skills independently overwrite the same canonical artifact.

## Coverage and rework control

At G0, create `求解/计划/skill_use_ledger.json` and record every canonical Skill from
`skills/registry.yaml` as `active` or `not_applicable` with a trigger check, reason, planned stage,
required output, and owner. Conditional modules are considered; they are not silently skipped.
When a child Skill runs, append its invocation, revision, inputs, outputs, acceptance result, and
evidence paths to the ledger. A module remains `complete` only for the current project revision.

Before changing any passed artifact, append a structured event to
`求解/计划/rework_log.jsonl`. Record the root cause, earliest affected gate, invalidated artifacts,
replay Skills, approval requirement, and stop condition. Mark stale downstream records as
`superseded`, return to the earliest affected gate, rerun the dependency cone, and close the event
only after revalidation and refreezing. Never let a new file on disk imply that an old gate still
passes.

## Shared project state

Create or update `求解/project_state.yaml` as the single coordination record. At minimum it contains:

```yaml
project_id: short-stable-name
schema_version: 3
current_mode: solve
current_stage: G0
user_request: "..."
protected_paths: [题目/, 数据/]
input_versions: []
decisions: []
approvals: []
artifacts: []
gates: {}
open_gates: []
failures: []
next_action: "..."
```

Child Skills may create their own reports, but only the orchestrator updates the shared stage, gate status, and next action. A stage is not complete because a file exists; its acceptance checks and unresolved risks must be recorded.

Before a long-running phase, tool handoff, interruption, or stage transition, write a resumable checkpoint into the existing state records: current gate, accepted inputs and versions, artifacts produced, decisions and approvals, unresolved risks, failed attempts, and the exact next bounded action. A checkpoint is a recovery aid, not evidence that the gate passed; validate the recorded artifacts again after resuming.

For a new workspace use `scripts/init_project.py`. Before advancing a gate use `scripts/validate_project.py <root> --through <gate>`; it is a deterministic structural check, not proof that the mathematics or evidence is correct.

## Failure handling

- Missing Skill: execute the canonical instructions directly.
- Missing runtime or tool: use the documented fallback and mark unverified work.
- Conflicting outputs: compare evidence and acceptance criteria; do not merge blindly.
- Repeated failure: stop the stage, preserve diagnostics, and request the smallest necessary user decision.
- User rejection: return to the relevant decision gate without discarding valid earlier artifacts.
- Missing evidence or an unverified citation: keep the item unresolved and stop the dependent gate; do not silently substitute a plausible source.
- A failed validation or clean rerun: preserve diagnostics, freeze no new headline numbers, and route back to the producing stage.

Do not invoke a child Skill merely because it exists. Invoke it only when its specialized workflow materially improves the current stage.
