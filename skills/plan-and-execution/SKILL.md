---
name: plan-and-execution
description: Turn a multi-stage mathematical-modeling or paper-production specification into a bite-sized, testable implementation plan before making substantial changes. Use for complex projects, not for trivial edits or when the user explicitly wants an uninterrupted one-shot run.
---

# Plan and Execute

Map files, ownership, inputs, outputs, tests, and stage gates before implementation. Each task
must end with an independently checkable artifact. A useful plan records:

- goal and assumptions;
- exact files or directories to create or modify;
- inputs and protected artifacts;
- interfaces and downstream consumers;
- validation command or observable acceptance criterion;
- rollback or stop condition.

For a multi-stage modeling project, add two explicit control artifacts to the plan:

- `求解/计划/skill_use_ledger.json`: one applicability and evidence record for every canonical
  Skill, including conditional modules that are marked not applicable;
- `求解/计划/rework_log.jsonl`: append-only revision events with the earliest affected gate,
  invalidated outputs, replay order, acceptance checks, and closure evidence.

The plan is incomplete if it describes only the first pass. For each material decision, state what
would invalidate it, where execution returns, which downstream artifacts become stale, and what
must be regenerated before the decision can be accepted again.

For a mathskills project, save the plan under `求解/计划/` and connect it to
`project_state.yaml`. Use the existing G0--G7 workflow as the top-level decomposition. Do not
create a plan to disguise missing evidence; unresolved choices remain explicit.
