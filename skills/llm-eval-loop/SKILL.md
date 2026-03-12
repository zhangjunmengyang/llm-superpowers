---
name: llm-eval-loop
description: Tight evaluation loops for LLM quality, safety, reasoning, reward, and regression detection. Use when Codex needs to compare checkpoints, choose benchmarks, define acceptance gates, set up judge or verifier evaluation, or turn pretraining, finetuning, alignment, and reasoning outputs into repeatable measurements across any repository or framework.
---

# LLM Eval Loop

Use this skill to keep training work grounded in measurable decisions instead of anecdotes from showcase prompts.

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
