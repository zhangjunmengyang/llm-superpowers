# Reward Model Design

Use this file to design and validate reward signals.

## Why Use A Reward Model

Use a reward model when:

- you need a reusable scalar for many candidates
- you need online RL
- you need checkpoint ranking or best-of-n selection
- the rubric is too rich for simple pairwise optimization alone

## Supervision Options

- pairwise ranking
- scalar labels
- rule-based score
- verifier outputs
- hybrid signals

## Validation Requirements

- held-out reward set
- pairwise agreement checks
- behavior-specific probes
- robustness to distribution shift
- reward-hacking probes

## Public Baselines

- [huggingface/trl](https://github.com/huggingface/trl)
- [allenai/reward-bench](https://github.com/allenai/reward-bench)
- [OpenRLHF/OpenRLHF](https://github.com/OpenRLHF/OpenRLHF)

## Failure Modes

- reward matches style rather than intended behavior
- reward is too narrow for the rollout distribution
- reward benchmark overfitting
- reward reused outside its intended scope
