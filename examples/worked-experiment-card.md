# Worked Artifact: Experiment Card

This is a filled example of the repository's experiment-card template.

# Experiment Card

**experiment_id:** `2026-03-12-dpo-refusal-calibration-v1`  
**parent_commit_or_checkpoint:** `sft-helpful-v3`  
**owner_question:** Can a narrow DPO run on cleaned refusal-calibration pairs improve over-compliance behavior without hurting safety blockers or reasoning?  
**change_surface:** `preference_data`  

## Hypothesis

A narrow DPO pass on rubric-cleaned refusal-calibration pairs will reduce over-compliance and improve pairwise helpfulness on refusal prompts without materially hurting safety or reasoning.

## Why This Run Exists

- what is expected to improve:
  - pairwise win rate on refusal-calibration prompts
  - over-compliance rate on harmful-but-ambiguous requests
- what should stay flat:
  - safety blocker pass rate
  - math and reasoning spot-check performance
  - median answer length
- what would make this run a waste:
  - the candidate wins only by becoming longer or more hedged
  - safety blockers regress
  - gains appear only on judge-heavy prompts

## Success Condition

- primary metric:
  - pairwise win rate on the refusal-calibration held-out slice
- smallest meaningful delta vs baseline:
  - at least +3 absolute points and above the repeatability band
- repeatability band or confidence note:
  - prior reruns on this slice moved by about 1.5 points
- guardrail metrics that must not regress materially:
  - safety blocker pass rate
  - math spot-check exact match
  - median output length

## Kill Condition

- what regression immediately kills the run:
  - any repeatable safety blocker regression
  - math spot-check down by more than 1 absolute point
  - verbosity up enough to explain the win by style rather than behavior
- what operational failure invalidates the run:
  - eval prompts changed
  - pair audit finds contradictory chosen and rejected labels
  - run is unstable or not comparable to the baseline

## Budget

- compute budget:
  - no more than one short DPO run on the cleaned slice
- max acceptable memory:
  - within the current training stack envelope
- expected runtime:
  - a same-day loop including eval and failure review

## Smoke Set

- fixed prompts or tasks to rerun after systems changes:
  - 20 refusal-calibration prompts
  - 10 harmful-request safety blockers
  - 10 math spot checks
- fastest check that tells us whether quality drifted:
  - pairwise refusal win rate plus safety blocker pass rate on the smoke set

## Non-Goals

- what this run is not trying to answer:
  - whether reward modeling should replace DPO
  - whether online RL should come next
  - whether the base chat template should change

## Rollback Point

- exact commit or checkpoint to return to if discarded:
  - `sft-helpful-v3`
