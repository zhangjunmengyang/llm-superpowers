# Synthetic Data Patterns

Use this file to design a data product that another engineer could generate and audit.

## Product Matrix

| Target stage | Minimal schema | Strong default pattern | Quality gate |
| --- | --- | --- | --- |
| SFT | `instruction`, `input`, `output` | source tasks plus rubric-filtered teacher answers | schema complete and target behavior visible |
| DPO | `prompt`, `chosen`, `rejected` | multi-sample plus contrastive ranking | chosen wins for a named reason |
| Reward model | pairwise or scalar labels | rubric-backed ranking or scalar score | signal explainable and held-out checks exist |
| PPO or RL | prompt or trajectory | curated rollout pool | reward and prompt diversity explicit |
| Step SFT | step arrays | teacher traces split into steps | boundaries valid |
| PRM | steps plus labels | verifier or rubric labeling | labels align to steps |
| veRL or R1 export | messages plus reward metadata | deterministic rule-graded tasks | reward target reproducible |

## Source Inventory Questions

- what is the raw source
- who or what labels it
- what gets synthesized
- what gets reviewed manually
- what gets filtered out before export

## Quality Gates

- provenance recorded
- duplicates controlled
- train and eval split
- rubric documented
- contamination risk noted
- token length distribution checked
- negative examples are intentionally bad for the target behavior
