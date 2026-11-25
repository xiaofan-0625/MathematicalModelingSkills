---
name: model-deliberation
description: Stress-test mathematical-modeling decisions, discover unknowns and blind spots, compare candidate methods, challenge assumptions, and produce a justified model decision. Use when a modeling direction is unclear, high-impact, disputed, under-specified, or ready for adversarial review.
---

# Deliberate on Model Design

Use structured disagreement to improve a decision. Do not multiply viewpoints when the answer is already routine and well-supported.

## Select a mode

- **Quick**: compare two or three plausible methods against explicit criteria.
- **Unknowns**: identify missing information, untestable assumptions, and fragile dependencies.
- **Interview**: ask one decisive question at a time until major branches are resolved.
- **Red team**: try to falsify the current formulation, constraints, or validation plan.
- **Council**: generate independent candidate analyses, then synthesize agreements and conflicts.
- **Supervisor gate**: evaluate a proposed contribution only after checking that its implementation and validation path are concrete.
- **Decision log**: record the chosen method, rejected alternatives, evidence, and reversal conditions.

## Workflow

1. State the decision, required output, constraints, available evidence, and deadline.
2. Separate known facts, inferred facts, assumptions, preferences, and unknowns.
3. For an innovative idea, require an implementation path before quality scoring: method components, required data, baseline, isolating experiment or proof obligation, expected failure mode, and feasible time/compute budget. If these cannot be stated, mark the idea `not yet evaluable` rather than rewarding ambition.
4. Generate only materially distinct candidates.
5. Evaluate candidates on task relevance, novelty relative to direct baselines and prior work, technical soundness, data fit, feasibility, interpretability, robustness, expected score or scientific significance, and paper communicability.
6. Identify any fatal flaw that caps the current recommendation: impossible data requirement, unsupported identifiability, missing legal baseline, infeasible compute, untestable contribution, or dependence on a result the project cannot produce.
7. Attack the leading candidate with counterexamples, leakage checks, feasibility tests, and the strongest plausible version of competing approaches.
8. Ask the user only questions whose answers can change the decision.
9. Recommend one approach, a baseline, validation plan, explicit fallback, current quality tier, and the smallest actions needed to reach the next tier.

## Output contract

Return:

```text
Decision
Evidence
Assumptions
Alternatives considered
Failure modes
Validation required
Reversal conditions
Current tier and limiting factor
Next-tier actions
Unresolved questions
```

Do not present simulated agents or model opinions as independent evidence. A council is a reasoning technique, not a substitute for data or literature.
