# Online RL Recipes

Use this file to design rollout-based post-training plans.

## When Online RL Is Worth It

Use online RL when:

- the task needs exploration
- rollout-time reward matters
- best-of-n is no longer enough
- you have a reward or verifier strong enough to guide learning

## Core Design Axes

- rollout unit
- reward latency
- KL or reference control
- batch and trajectory budget
- online eval cadence

## Method Heuristics

- PPO: solid baseline when you need a general-purpose RLHF method
- RLOO: attractive when you want simpler or lower-variance group-relative updates in some settings
- GRPO: attractive for reasoning-heavy group-relative objectives

## Public Baselines

- [huggingface/trl](https://github.com/huggingface/trl)
- [OpenRLHF/OpenRLHF](https://github.com/OpenRLHF/OpenRLHF)
- [volcengine/verl](https://github.com/volcengine/verl)
- [huggingface/open-r1](https://github.com/huggingface/open-r1)

## Failure Modes

- online RL compensating for bad data
- reward exploitability
- KL collapse or reward chasing
- rollout distribution too narrow
- no clean evaluation against offline baselines
