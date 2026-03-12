---
name: checkpoint-regression-triage
description: Checkpoint regression diagnosis for baseline-vs-candidate failures, slice review, sampled bad cases, likely root-cause assignment, and next-run proposals. Use when Codex needs to answer questions such as 'why did this candidate regress', 'which slices got worse', 'is this data, recipe, eval, or systems', or turn a confusing model comparison into a concrete next experiment.
---

# Checkpoint Regression Triage

Use this skill when the benchmark says something got worse and the team needs a diagnosis that can drive the next run.

## Use This Skill First When

- a candidate checkpoint regressed against the baseline
- the average looks fine but one slice looks bad
- a run improved the headline metric while making qualitative behavior worse
- the team needs a next-run proposal grounded in failures, not guesswork

## Core Workflow

1. Freeze the baseline, candidate, and exact eval slice.
2. Identify the worst regressions first, not the best wins.
3. Review actual failures and cluster them.
4. Assign the most likely root-cause layer:
   - data
   - recipe
   - reward or judge
   - systems
   - prompt or formatting
5. Write one next-run proposal that isolates the likely cause.

## Hard Rules

- do not triage from aggregate metrics alone
- inspect real generations before proposing fixes
- do not call something a data issue if formatting drift explains it
- do not call something algorithmic if systems instability may have corrupted the run
- do not propose more than one primary next-run question

## Artifact Contract

When using this skill, produce:

- worst slices
- sampled failures
- dominant failure cluster
- likely root-cause layer
- confidence level
- one next-run proposal

## References

- Read `references/review.md` for failure clustering, review coverage, severity, and next-run heuristics.
