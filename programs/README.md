# Programs

Programs are the orchestration layer of `llm-superpowers`.

They are not generic docs. They define the operating loops that make training work disciplined, reviewable, and repeatable.

## Why Programs Exist

The repository should not rely on loose skill-to-skill hopping.

Skills are local primitives.
Programs define:

- what artifact must exist before a run starts
- what gets logged after a run ends
- what metrics actually matter
- when to keep or discard a run
- when to escalate into eval, systems, or research review

## Current Programs

- [experiment-loop.md](experiment-loop.md)
  - the default operating loop for post-training work
- [eval-board.md](eval-board.md)
  - the canonical evaluation and release board
- [systems-war-room.md](systems-war-room.md)
  - the operating loop for OOMs, throughput collapse, and instability
- [research-to-experiment.md](research-to-experiment.md)
  - the translation path from paper or repo to first runnable experiment

## Templates

Programs use concrete artifacts, not vibes.

Start from:

- [templates/current-best.md](templates/current-best.md)
- [templates/experiment-card.md](templates/experiment-card.md)
- [templates/results.tsv](templates/results.tsv)
- [templates/eval-board.md](templates/eval-board.md)
- [templates/systems-triage.md](templates/systems-triage.md)
- [templates/reproduction-plan.md](templates/reproduction-plan.md)

## Rule

Programs own sequence.

Skills should be independently usable. If orchestration logic is needed, it belongs here.
