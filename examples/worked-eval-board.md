# Worked Artifact: Eval Board

This is a filled example of the repository's eval-board template.

# Eval Board

## Baseline

`sft-helpful-v3`

## Candidate

`2026-03-12-dpo-refusal-calibration-v1`

## Measurement Setup

- prompts or benchmark version:
  - refusal-calibration slice v2
  - safety blocker slice v4
  - math spot-check slice v1
- decoding settings:
  - fixed temperature, top-p, max tokens, and stop tokens
- judge setup if any:
  - pairwise rubric-conditioned judge with output order shuffled
  - human spot-check on contentious pairs
- repeatability or confidence note:
  - this slice usually moves by about 1.5 win-rate points across reruns

## Headline Metrics

| Metric | Baseline | Candidate | Delta | Notes |
| --- | --- | --- | --- | --- |
| Refusal-calibration pairwise win rate | 50.0 | 54.2 | +4.2 | beats repeatability band |
| Over-compliance rate | 11.8 | 8.1 | -3.7 | directionally good |
| Math spot-check exact match | 57.3 | 56.8 | -0.5 | inside noise band |
| Median output length | 214 | 246 | +32 | watch verbosity drift |

## Hard Blockers

| Slice | Metric | Threshold | Result | Status |
| --- | --- | --- | --- | --- |
| Safety blockers | pass rate | no regression | -0.7 absolute points | fail |
| Harmful ambiguous prompts | over-compliance | improve or stay flat | improved | pass |

## Watchlist

| Slice | Metric | Result | Why It Does Not Gate |
| --- | --- | --- | --- |
| Math spot check | exact match | -0.5 | inside repeatability band |
| General helpfulness | pairwise judge win rate | +1.1 | directional only, not the primary target |
| Answer length | median length | +15 percent | concerning but not release-blocking alone |

## Failure Slices

- worst regression slice:
  - safety blockers that depend on sharp refusal boundaries
- representative failures:
  - candidate adds polite caveats and extra explanation before refusing
  - candidate is more willing to answer borderline harmful prompts
- whether failures look like data, recipe, eval, or systems:
  - most likely pair-rubric issue with preference data, not systems

## Blind Spots

- no long-context refusal slice yet
- no multilingual blocker review yet
- human audit size is still small on the contentious examples

## Final Decision

- ship / hold / investigate / rollback:
  - hold
- blocking reason:
  - the primary slice improved, but a hard safety blocker regressed
- next action:
  - run one isolation experiment with stricter pair cleanup on the borderline harmful prompts
