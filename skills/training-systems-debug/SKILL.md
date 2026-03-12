---
name: training-systems-debug
description: Systems-debug workflows for OOMs, divergence, throughput collapse, parallelism misconfiguration, kernel issues, and scaling failures in LLM training and inference. Use when Codex needs to answer questions such as 'why did this run OOM', 'why is throughput so low', 'why does it diverge only at scale', or build a stepwise debug plan for distributed training systems.
---

# Training Systems Debug

Use this skill when the recipe is mostly known and the main blocker is operational failure or systems instability.

## Use This Skill First When

- the run OOMs
- throughput is much worse than expected
- the same recipe works small-scale but fails at larger scale
- divergence appears tied to precision, checkpointing, kernels, or parallelism
- a serving or inference engine bottleneck blocks evaluation

## Core Workflow

1. Classify the failure: memory, throughput, stability, communication, or serving.
2. Reproduce the failure on the smallest credible configuration.
3. Isolate one axis at a time: precision, batch, sequence length, checkpointing, kernel, optimizer sharding, or parallelism.
4. Measure before and after each intervention.
5. Keep a rollback-safe baseline.
6. Confirm that the fix does not corrupt training quality or evaluation fairness.

## Debug Classes

- OOM
- instability or divergence
- throughput collapse
- distributed communication issues
- bad checkpointing behavior
- inference or serving bottlenecks

## Operating Rules

- Do not debug five knobs at once.
- Separate algorithm failure from systems failure.
- Small-scale reproduction beats guessing at full scale.
- If the systems stack is too complex to reason about, simplify before tuning.
- A throughput gain is not a win if it invalidates the quality comparison.

## Do Not Lead With This Skill When

- the training stage is still undecided
- the main issue is dataset quality or evaluation design
- the team still does not know whether the algorithm is correct at small scale
- the paper recipe itself is not yet understood

## Typical Hand-Offs

- to `llm-training-systems` for broader systems architecture choices
- to `llm-eval-loop` or `eval-and-regression-gates` to preserve fair comparison after fixes
- to `llm-posttrain-pipeline` if systems pain reveals an unrealistic recipe choice

## Output Shape

When using this skill, produce:

- failure class
- smallest reproduction
- prioritized intervention list
- measurement plan
- rollback point
- validation checks

## References

- Read `references/debug.md` for debug patterns and common root causes.
