---
name: online-rl-posttraining
description: Online RL design for PPO, RLOO, GRPO, rollout-based reasoning improvement, and reward-driven post-training. Use when Codex needs to answer questions such as 'do we really need online RL', 'should we use PPO or GRPO', 'is the reward stable enough for rollouts', or design an online RL stack after SFT, preference optimization, or reward modeling.
---

# Online RL Posttraining

Use this skill when the project has crossed from offline alignment into rollout-based optimization.

## Use This Skill First When

- the team already has a plausible base policy and reward signal
- offline methods are no longer enough
- exploration and rollout feedback are central to further gains
- the project is considering PPO, RLOO, GRPO, or similar online optimization

## Core Workflow

1. Challenge whether online RL is actually necessary.
2. Audit the reward or verifier for exploitability.
3. Choose the rollout unit: completion, trajectory, or reasoning trace.
4. Choose the algorithm family and reference-policy strategy.
5. Define rollout, batching, and evaluation cadence.
6. Add reward-hacking and KL-collapse checks before scaling.

## Algorithm Families

- PPO
- RLOO
- GRPO
- custom rollout optimization for reasoning tasks

## Operating Rules

- Do not use online RL to fix a bad SFT base.
- Do not use RL before the reward or verifier is minimally trustworthy.
- Treat rollout design as part of the algorithm, not only infrastructure.
- Validate that gains survive outside the online training distribution.
- Distill or simplify later if the online policy is too expensive.

## Do Not Lead With This Skill When

- the project still lacks a clean offline baseline
- chosen and rejected preference data would likely solve the problem more cheaply
- the main question is reward construction rather than RL
- the main blocker is systems throughput before the RL plan is even sound

## Typical Hand-Offs

- to `reward-modeling` when the reward is still immature
- to `reasoning-prm-verifier` when reasoning rollouts need verifier support
- to `llm-eval-loop` for online-vs-offline comparison
- to `llm-training-systems` once rollout scale becomes the bottleneck

## Output Shape

When using this skill, produce:

- why online RL is needed
- reward readiness assessment
- rollout unit
- algorithm choice
- stability checks
- scale-up and distillation plan

## References

- Read `references/recipes.md` for online RL design heuristics and failure modes.
