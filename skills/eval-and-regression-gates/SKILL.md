---
name: eval-and-regression-gates
description: Evaluation-gate design for baseline comparisons, release criteria, regression detection, benchmark slices, and model-quality signoff. Use when Codex needs to answer questions such as 'what should block a release', 'what counts as a regression', 'which metrics are required before scaling', or turn raw evaluation into explicit go, hold, or investigate gates.
---

# Eval And Regression Gates

Use this skill when the team already has candidate outputs or checkpoints and needs explicit decision gates rather than generic evaluation advice.

## Use This Skill First When

- the baseline and candidate already exist
- the team needs ship, hold, or investigate criteria
- regressions are suspected but not yet formalized
- evaluation exists, but release gating logic is still vague

## Core Workflow

1. Define the baseline, candidate, and decision point.
2. Identify the minimum metric set that should control the decision.
3. Split metrics into must-pass, watchlist, and diagnostic-only groups.
4. Add regression gates for safety, reasoning, reward, and latency where relevant.
5. Define fail-fast rules and exceptions.
6. Produce a decision template that another engineer can apply consistently.

## Gate Types

- hard release blockers
- regression thresholds
- watchlist metrics
- diagnostic metrics
- scaling prerequisites

## Operating Rules

- Not every metric deserves gate power.
- A metric should only gate releases if the team agrees what bad movement means.
- Separate diagnosis from signoff.
- Prefer a small, stable gate set over a giant dashboard.
- Always define what baseline the gate compares against.

## Do Not Lead With This Skill When

- the team still lacks a basic evaluation plan
- the main problem is benchmark choice rather than decision logic
- the bottleneck is recipe design, not signoff
- the issue is systems failure rather than release criteria

## Typical Hand-Offs

- to `llm-eval-loop` for benchmark design and measurement
- to `llm-posttrain-pipeline` when a failed gate implies the wrong recipe choice
- to `training-systems-debug` when latency or throughput gates fail for systems reasons

## Output Shape

When using this skill, produce:

- baseline and candidate
- must-pass gates
- regression thresholds
- watchlist metrics
- exception policy
- final decision template

## References

- Read `references/gates.md` for gate design patterns and anti-patterns.
