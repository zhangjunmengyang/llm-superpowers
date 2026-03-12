# Experiment Card

**experiment_id:**  
**parent_commit_or_checkpoint:**  
**owner_question:**  
**change_surface:**  

## Hypothesis

One sentence only.

## Why This Run Exists

- what is expected to improve
- what should stay flat
- what would make this run a waste

## Success Condition

- primary metric
- smallest meaningful delta vs baseline
- repeatability band or confidence note
- guardrail metrics that must not regress materially

## Kill Condition

- what regression immediately kills the run
- what operational failure invalidates the run

## Budget

- compute budget
- max acceptable memory
- expected runtime

## Smoke Set

- fixed prompts or tasks to rerun after systems changes
- fastest check that tells us whether quality drifted

## Non-Goals

- what this run is not trying to answer

## Rollback Point

- exact commit or checkpoint to return to if discarded
