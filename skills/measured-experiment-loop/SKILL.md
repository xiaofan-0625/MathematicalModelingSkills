---
name: measured-experiment-loop
description: Run bounded, measurable model or parameter experiments for mathematical-modeling projects. Use when several candidate implementations can be compared by a fixed metric and each trial must be logged, validated, retained, or discarded; do not use for ordinary one-shot coding or open-ended qualitative improvement.
---

# Measured Experiment Loop

Use a controlled loop for model comparison, solver tuning, simulation calibration, or code
optimization:

```text
inspect -> define metric and guard -> change one hypothesis
-> run verification -> keep or discard -> log evidence -> repeat
```

## Before the first write

Define in `求解/实验/experiment_contract.yaml`:

- one goal and one primary metric with direction and units;
- baseline command and target or stopping rule;
- explicit search space, candidate identity or configuration hash, and forbidden combinations;
- editable scope and protected inputs/results;
- correctness guard independent of the optimization metric;
- seed, split, wall-clock or compute budget, maximum iterations, patience, and noise policy;
- acceptance rule and reversal condition.

Run the baseline read-only. Ask for approval before launching a repeated loop or changing a
protected project file. Do not infer that a lower score is better from the metric name.

## Trial rules

1. Change one substantive hypothesis at a time.
2. Normalize and hash each configuration before execution. Skip exact duplicates and log why the
   trial was not run; do not spend budget on a renamed or reordered copy of an earlier candidate.
3. Use the same data split, preprocessing, seed policy, and metric for intended comparisons.
4. Run the independent guard even when the metric improves.
5. Keep failed, null, unstable, timed-out, and skipped trials in an append-only log. Preserve raw
   stdout, stderr, solver status, environment summary, and machine-readable results for every run.
6. Retain only candidates that improve the accepted metric and pass the guard; otherwise restore
   the last passing state without deleting the evidence.
7. Stop at target, budget, patience exhaustion, user stop, or a verified environmental blocker.

## Required artifacts

```text
求解/实验/experiment_contract.yaml
求解/实验/baseline.json
求解/实验/events.jsonl
求解/实验/raw/                    # 每次运行的原始输出与配置快照
求解/实验/experiment_report.md
```

For a modeling paper, accepted values still require the normal validation gate and must be copied
to the relevant `问题X/结果/frozen_numbers.json` only after review. This loop never authorizes
invented improvement claims or silent changes to the paper.
