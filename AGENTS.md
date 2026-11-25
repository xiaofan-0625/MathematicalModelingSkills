# Mathematical Modeling Workspace

Read `SKILL.md` as the source of truth, then resolve only the current mode and stage through `skills/registry.yaml`.

- Choose the smallest sufficient mode: `solve`, `review`, `repair`, `score`, or `deliver`.
- Preserve original files under `题目/` and `数据/`; write work under `求解/`, `论文/`, and `提交/`.
- Advance G0–G7 only on evidence, not because a named file exists.
- At G0, classify every canonical Skill in `求解/计划/skill_use_ledger.json`; never silently omit a conditional module.
- Before a material upstream edit, record rework, mark dependent artifacts stale, return to the earliest affected gate, and replay the downstream dependency cone before refreezing.
- Keep problem facts, model decisions, frozen numbers, citations, score issues, and package hashes in their canonical artifacts.
- Treat `CLAUDE.md` as a legacy compatibility reference; it cannot override `SKILL.md`.
