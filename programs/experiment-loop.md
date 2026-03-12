# Experiment Loop

This is the default operating loop for LLM post-training work.

Use it when you are running actual experiments, not just discussing algorithms.

## Required Artifacts

Before the first real run, create:

- `runboard/results.tsv`
- `runboard/current-best.md`
- `runboard/experiments/<timestamp>-<slug>.md`
- `runboard/failures/` for sampled regressions

Use:

- [templates/current-best.md](templates/current-best.md)
- [templates/results.tsv](templates/results.tsv)
- [templates/experiment-card.md](templates/experiment-card.md)

## Start Gate

Do not start the loop until all of these are explicit:

- named baseline commit or checkpoint
- named primary metric
- named kill metric or blocker metric
- fixed eval slice or benchmark version
- fixed compute budget
- one owner question for this run

## Canonical Loop

1. Frame the run.
   - Use `$llm-posttrain-pipeline`, `$llm-synthetic-data`, or `$llm-research-to-recipe` to decide the smallest meaningful next move.
2. Write the experiment card.
   - Record hypothesis, change surface, success condition, kill condition, rollback point, and non-goals.
3. Change one coherent surface only.
   - Examples: algorithm, data mixture, reward rubric, rollout unit, chat template, sequence length.
   - Do not change multiple surfaces unless the run is explicitly a bundled recipe test.
4. Run and capture the full summary.
   - Training metrics
   - eval metrics
   - systems metrics
5. Evaluate the run.
   - Use `$llm-eval-loop` to compare the candidate against the baseline.
6. Review failure evidence.
   - Inspect worst regressions, not only averages.
   - Review at least 20 worst failures overall, and more if one critical slice is small.
   - Save representative failures into `runboard/failures/`.
7. Make a keep or discard decision.
   - Use `$run-ledger-and-keep-discard`.
8. Advance the branch or revert.
   - Keep: promote candidate to new baseline.
   - Discard: revert and preserve the ledger entry.
9. Queue the next run.
   - One next question only.

## Hard Rules

- one primary hypothesis per run
- one change surface unless explicitly testing a bundled recipe
- no silent benchmark drift
- no keep decision without failure review
- no scale-up from a delta that still sits inside the repeatability band
- no algorithm conclusion from a run invalidated by systems instability
- no data conclusion from a run contaminated by eval overlap

## Minimum Metrics To Log

Every row in `results.tsv` should capture at least:

- experiment id
- parent commit or checkpoint
- change surface
- primary metric
- key guardrail metrics
- peak memory
- throughput
- status: keep, discard, crash, investigate
- one-line rationale

## Escalation Paths

- if the run crashes or the summary is operationally invalid, switch to [systems-war-room.md](systems-war-room.md)
- if the benchmark picture is unclear, switch to [eval-board.md](eval-board.md)
- if the run was based on a paper or public repo and the recipe itself is unclear, switch to [research-to-experiment.md](research-to-experiment.md)

## Success Condition

The loop is healthy when each run leaves behind:

- one explicit hypothesis
- one explicit artifact trail
- one explicit keep or discard decision
- one explicit next question
