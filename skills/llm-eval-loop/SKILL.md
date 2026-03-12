---
name: llm-eval-loop
description: Evaluation-board design for baseline-vs-candidate comparison, failure slices, ship or hold decisions, judge setup, and regression measurement in LLM training work. Use when Codex needs to answer questions such as 'how do we compare this checkpoint', 'what belongs on the eval board', 'which metrics should gate promotion', or turn raw outputs into a decision with hard blockers, watchlist metrics, and sampled failures.
---

# LLM Eval Loop

Use this skill to build a real eval board, not a generic benchmark list.

## Use This Skill First When

- there is already a baseline and at least one candidate
- the team needs a board that can support ship, hold, investigate, or rollback
- a promising run needs measurement before baseline advancement
- a regression exists and the team needs slice-level evidence

## Core Workflow

1. Define what changed between baseline and candidate.
2. Freeze prompts, datasets, and decoding settings.
3. Split metrics into hard blockers, watchlist, and diagnostic-only.
4. Review failure slices and sampled bad cases.
5. Produce a ship, hold, investigate, or rollback decision.

## Board Sections

- headline metrics
- hard blockers
- watchlist metrics
- failure slices
- final decision

## Required Output

When using this skill, return:

- baseline and candidate
- frozen measurement setup
- hard blocker metrics
- watchlist metrics
- failure slices
- final decision
- known blind spots

## Hard Rules

- Keep the benchmark set stable when comparing checkpoints.
- Always compare against a named baseline.
- Use targeted probes for debugging, but do not confuse them with the board.
- Do not use the same model family as both candidate and sole judge without noting the bias.
- Do not sign off from averages only.
- Do not let one better global mean hide a bad slice that actually matters.

## Do Not Lead With This Skill When

- the main question is which post-training stage to run
- the bottleneck is missing or low-quality training data
- the target is reasoning recipe design rather than evidence gathering
- the main blocker is memory, throughput, or instability

## References

- Read `references/benchmarks.md` for board design, harness choices, and failure review rules.
