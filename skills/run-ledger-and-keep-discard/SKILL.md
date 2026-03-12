---
name: run-ledger-and-keep-discard
description: Experiment logging, keep-or-discard discipline, baseline advancement, rollback points, and run-ledger hygiene for LLM training work. Use when Codex needs to answer questions such as 'should we keep this run', 'what goes into results.tsv', 'how do we log this experiment', or turn a candidate run into an explicit keep, discard, crash, or investigate decision.
---

# Run Ledger And Keep Discard

Use this skill when a run has finished and the team needs disciplined experiment accounting instead of vibes.

## Use This Skill First When

- a candidate run just completed
- the team is arguing about whether a run really improved
- `results.tsv` or a run ledger is missing fields or decisions
- baseline advancement and rollback points are unclear

## Core Workflow

1. Identify the baseline the run was compared against.
2. Confirm the experiment card exists and names one primary hypothesis.
3. Record the run summary in a durable ledger row.
4. Decide one of four statuses only:
   - keep
   - discard
   - crash
   - investigate
5. Advance the baseline only if the run is both better and operationally valid.
6. Record the next question left open by the run.

## Hard Rules

- never keep a run without a named baseline
- never keep a run that is operationally invalid
- never keep a run on anecdotal prompt wins alone
- never discard a run without writing why it lost
- never advance the baseline if the eval suite changed silently
- one run should answer one main question

## Artifact Contract

When using this skill, produce:

- ledger row
- status
- keep or discard rationale
- rerun or investigate note if the result sits inside the noise band
- rollback point
- next question

## Decision Standard

Keep only when all of these are true:

- the primary metric improved or the tradeoff is explicitly accepted
- no hard blocker regressed materially
- the run was operationally valid
- the change surface is understood well enough to build on

Use `investigate` when:

- the run is neither clearly good nor clearly bad
- measurement is incomplete
- judge disagreement or systems instability makes the result ambiguous
- the delta is too small to beat the repeatability band confidently

## References

- Read `references/ledger.md` for the default row schema, rerun policy, decision tests, and anti-patterns.
