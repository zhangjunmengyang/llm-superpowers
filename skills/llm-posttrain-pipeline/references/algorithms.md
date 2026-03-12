# Post-Training Algorithm Heuristics

Use this file when designing the next run, not when writing a survey.

## Start With The Smallest Credible Move

- If the behavior is absent, start with SFT.
- If the behavior exists but the ranking is wrong, try preference optimization.
- If a reusable scalar is needed across many candidates, build a reward model.
- If search is cheap and judging is reliable, try rejection sampling before RL.
- Use online RL only when exploration or trajectory-level credit assignment really matters.

## Use Continued Pretraining When

- broad domain coverage is missing
- vocabulary or style drift is structural
- instruction tuning alone would be too shallow

## Use SFT When

- the task format is missing
- the model lacks the target interaction pattern
- you need a clean base before preference or RL stages

## Use Preference Optimization When

- chosen and rejected data already exists
- the main issue is preference ranking, not exploration
- a simpler stack than reward-plus-RL is desired

## Use Reward Modeling When

- the signal should be reused across many candidates or stages
- checkpoint ranking or best-of-n matters
- online RL is a serious possibility

## Use Online RL When

- offline methods no longer answer the question
- delayed reward matters
- the task genuinely benefits from exploration

## Use Rejection Sampling Or Best-of-N When

- many candidates can be sampled cheaply
- a reliable judge or verifier exists
- RL would add too much stack complexity for the expected gain

## Use Distillation When

- a stronger teacher or search policy already exists
- latency or cost matters
- deployment simplicity matters more than discovery

## Anti-Patterns

- using RL to fix formatting or templating
- changing algorithm and dataset at the same time in the same first run
- using DPO-like methods on contradictory preference labels
- trusting reward models without held-out validation
- evaluating only on synthetic prompts from the same generator
