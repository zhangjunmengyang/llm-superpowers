# Default Workflows

This document shows the repository's program-led workflows.

## Workflow 1: New Experiment

Use when the team needs the next real run.

Program:

- `programs/experiment-loop.md`

Lead skills:

- `llm-posttrain-pipeline`
- `llm-synthetic-data`
- `llm-eval-loop`
- `run-ledger-and-keep-discard`

Expected outputs:

- experiment card
- `results.tsv` row
- explicit keep, discard, crash, or investigate decision
- next question

## Workflow 2: Candidate Review

Use when a checkpoint exists and baseline advancement is the decision.

Program:

- `programs/eval-board.md`

Lead skills:

- `llm-eval-loop`
- `checkpoint-regression-triage`

Expected outputs:

- eval board
- failure slices
- sampled bad cases
- ship, hold, investigate, or rollback decision

## Workflow 3: Systems Recovery

Use when the run is invalid because of OOM, instability, or throughput collapse.

Program:

- `programs/systems-war-room.md`

Lead skills:

- `llm-training-systems`
- `throughput-and-oom-triage`
- `llm-eval-loop`

Expected outputs:

- triage board
- one-axis intervention plan
- rollback point
- quality comparability check

## Workflow 4: Research Translation

Use when the starting point is a paper or public repo.

Program:

- `programs/research-to-experiment.md`

Lead skills:

- `llm-research-to-recipe`
- `llm-posttrain-pipeline`

Expected outputs:

- reproduction plan
- irreducibles
- cheap approximation
- first runnable experiment card

## Workflow 5: Reasoning Improvement

Use when the target is reasoning behavior specifically.

Program:

- usually `programs/experiment-loop.md`

Lead skills:

- `llm-reasoning-posttrain`
- `reasoning-prm-verifier`
- `llm-eval-loop`

Expected outputs:

- reasoning trace design
- verifier or PRM decision
- reasoning-specific eval gates
