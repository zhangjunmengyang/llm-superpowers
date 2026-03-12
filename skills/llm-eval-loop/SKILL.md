---
name: llm-eval-loop
description: Tight evaluation loops for LLM quality, safety, reasoning, reward, and regression detection. Use when Codex needs to answer questions such as 'how do we compare baseline vs candidate', 'which benchmark should we trust', 'what are the ship gates', compare checkpoints, choose benchmarks, define acceptance gates, set up judge or verifier evaluation, or turn pretraining, finetuning, alignment, and reasoning outputs into repeatable measurements across any repository or framework.
---

# LLM Eval Loop

Use this skill to keep training work grounded in measurable decisions instead of anecdotes from showcase prompts.

## Use This Skill First When

- there is already a baseline and at least one candidate
- the team needs ship gates, comparison logic, or benchmark selection
- a promising run needs to be validated before scale-up
- a regression is suspected but not yet localized

## Core Workflow

1. Define what changed between baseline and candidate.
2. Choose the smallest eval set that can detect the expected gain or regression.
3. Separate generation from scoring.
4. Track at least one task metric and one safety, preference, or success metric.
5. Produce a ship, hold, or investigate decision.

## Eval Types

- offline benchmark eval
- pairwise judge eval
- reward model eval
- safety eval
- reasoning correctness eval
- latency and cost eval

## Rules

- Keep the benchmark set stable when comparing checkpoints.
- Always compare against a named baseline.
- Use targeted probes for qualitative debugging, but do not mistake them for evaluation.
- Do not use the same model family as both candidate and sole judge without noting the bias.
- If the user asks for broad public benchmarking, use public harnesses instead of ad hoc prompt scripts.

## Do Not Lead With This Skill When

- the main question is which post-training stage to run
- the bottleneck is missing or low-quality training data
- the target is reasoning recipe design rather than evidence gathering
- the main blocker is memory, throughput, or instability

## Typical Hand-Offs

- to `llm-posttrain-pipeline` when results imply the wrong recipe was chosen
- to `llm-synthetic-data` when regressions trace back to data quality
- to `llm-training-systems` when performance or instability invalidates fair comparison

## Output Shape

When using this skill, return:

- baseline and candidate
- eval dataset or prompt suite
- generation settings
- scoring method
- pass or fail criteria
- decision
- known blind spots

## References

- Read `references/benchmarks.md` for benchmark and harness choices.
