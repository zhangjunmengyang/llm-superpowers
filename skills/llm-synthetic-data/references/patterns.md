# Synthetic Data Patterns

Use this file as a compact cookbook for choosing the right synthetic data recipe.

## Product Matrix

| Target stage | Minimal schema | Cheapest strong pattern | Acceptance checks |
| --- | --- | --- | --- |
| SFT | `instruction`, `input`, `output` | self-instruct plus rubric filtering | schema complete, output useful, duplicates low |
| DPO | `prompt`, `chosen`, `rejected` | best-of-n plus contrastive selection | chosen better for target behavior |
| Reward model | pairwise or scalar labels | rank with a policy or safety rubric | preference explainable |
| PPO or RL | prompt or trajectory | curated rollout pool | prompt diversity, reward defined |
| Step SFT | step arrays | teacher traces split into steps | step boundaries valid |
| PRM | steps plus labels | trajectory labeling with verifier or rubric | labels align to steps |
| veRL or R1 export | messages plus reward metadata | rule-graded reasoning tasks | reward target deterministic |

## Good Generation Patterns

### Instruction Data

- extract tasks from source corpora
- ask a strong teacher for one useful answer
- filter for clarity and diversity

### Preference Data

- build a prompt pool
- sample multiple answers
- rank with a rubric tied to the target behavior

### Reasoning Data

- store steps explicitly
- preserve final answer separately
- use rules or verifiers when possible

## Quality Gates

- provenance recorded
- duplicates controlled
- train and eval split
- reward or preference rubric documented
- contamination risk noted
- token length distribution checked

## Public Inspirations

- [huggingface/open-r1](https://github.com/huggingface/open-r1)
- [open-thoughts/open-thoughts](https://github.com/open-thoughts/open-thoughts)
- [magpie-align/magpie](https://github.com/magpie-align/magpie)
- [huggingface/trl](https://github.com/huggingface/trl)
