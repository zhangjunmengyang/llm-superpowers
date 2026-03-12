---
name: reward-modeling
description: Reward-model design for pairwise reward training, scalar rewards, verifier-backed rewards, and reward validation. Use when Codex needs to answer questions such as 'do we need a reward model', 'what should the reward dataset look like', 'how do we validate reward quality', or design a reward signal that can support rejection sampling, online RL, or checkpoint ranking.
---

# Reward Modeling

Use this skill when the main challenge is building or validating a reusable reward signal.

## Use This Skill First When

- the team needs a scalar signal for ranking or RL
- direct preference optimization is not enough
- a verifier or safety score must become a training-time signal
- reward hacking or judge mismatch is a core risk

## Core Workflow

1. Clarify what the reward is meant to value.
2. Choose pairwise, scalar, rule-based, or hybrid supervision.
3. Design the reward dataset and rubric.
4. Define calibration and validation checks.
5. Decide how the reward will be used: ranking, best-of-n, rejection sampling, or RL.
6. Stress-test for reward hacking and distribution shift.

## Reward Types

- pairwise reward models
- scalar reward models
- verifier-backed rewards
- hybrid rubric or safety rewards

## Operating Rules

- Reward quality is mostly a data and rubric problem, not a model-size problem.
- If the reward is reused across stages, document its intended scope explicitly.
- Validate on held-out preference or reward benchmarks before trusting the signal.
- Assume the policy will exploit any shortcut in the reward.
- Keep reward design and policy evaluation separate.

## Do Not Lead With This Skill When

- direct preference optimization already solves the problem well enough
- the project still lacks a clean SFT base
- the task is primarily reasoning-trace design rather than reward design
- the main blocker is throughput, memory, or distributed infrastructure

## Typical Hand-Offs

- to `preference-optimization` when a direct objective may be sufficient
- to `online-rl-posttraining` once a reward is stable enough for RL
- to `llm-eval-loop` for reward validation and policy comparison
- to `data-curation-and-filtering` for reward dataset cleanup

## Output Shape

When using this skill, produce:

- reward objective
- supervision type
- dataset and rubric design
- validation plan
- deployment scope
- reward-hacking risks

## References

- Read `references/design.md` for reward-model design heuristics and validation rules.
