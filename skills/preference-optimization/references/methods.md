# Preference Optimization Methods

Use this file to choose among offline preference-learning methods.

## When To Use Direct Preference Optimization

Use a direct method when:

- you have solid chosen and rejected pairs
- exploration is not the main bottleneck
- you want a simpler training stack than reward-model-plus-RL

## Method Heuristics

- DPO: strongest default baseline
- IPO: useful when you want more conservative behavior than vanilla DPO
- ORPO: useful when you want a compact objective that integrates ranking pressure directly
- KTO: useful when preference signal is closer to binary desirability than pairwise ranking
- SimPO: useful when you want a simple preference objective without a frozen reference in some setups

## Data Quality Rules

- chosen should be better for a specific reason
- rejected should be meaningfully worse, not random noise
- keep the rubric stable inside a dataset split
- avoid pairing answers that differ only stylistically if the target is factuality or safety

## Public Baselines

- [huggingface/trl](https://github.com/huggingface/trl)
- [allenai/open-instruct](https://github.com/allenai/open-instruct)
- [hiyouga/LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)
- [OpenAccess-AI-Collective/axolotl](https://github.com/OpenAccess-AI-Collective/axolotl)

## Failure Modes

- preference pairs with no real signal
- method choice hiding dataset problems
- no clean SFT baseline
- evaluating only with a judge aligned to the same training signal
