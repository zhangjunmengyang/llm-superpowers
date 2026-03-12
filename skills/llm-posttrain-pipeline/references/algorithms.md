# Post-Training Algorithms

Use this file to choose an algorithm based on the target behavior, feedback type, and engineering budget.

## Quick Selection

### Use Continued Pretraining When

- the model lacks domain coverage
- vocabulary or style drift is the main issue
- you need broad adaptation before instruction tuning

### Use SFT When

- the task format is missing
- behavior is mostly correctable with demonstrations
- you need a strong bootstrap model for later alignment

### Use DPO-Like Methods When

- you have pairwise preferences
- the main objective is response ranking rather than exploration
- you want a simpler alternative to PPO

Good families:

- DPO
- IPO
- ORPO
- KTO
- SimPO

### Use Reward Modeling When

- you need a reusable scalar signal
- the system will later run online RL or best-of-n selection
- safety or verifier score matters independently of SFT quality

### Use PPO, RLOO, or GRPO When

- the model must improve through online rollouts
- delayed reward matters
- the task benefits from exploration or trajectory-level feedback

### Use Rejection Sampling or Best-of-N When

- you can cheaply sample many candidates
- you have a reliable judge or verifier
- full online RL is too expensive

### Use Distillation When

- you already have a stronger teacher
- latency or cost matters
- the target is to compress a policy rather than discover behavior

## Decision Heuristics

- If the behavior is absent, start with SFT.
- If the behavior exists but ranking is wrong, use preference optimization.
- If the score is complex but reusable, build a reward model.
- If the task needs exploration, use RL.
- If you can score many candidates cheaply, try rejection sampling before RL.

## Failure Modes

- using RL to fix formatting
- using DPO when preference labels are noisy or contradictory
- using reward models without reward-bench style checks
- changing algorithm and dataset at the same time
- evaluating only on synthetic prompts created by the same generator
