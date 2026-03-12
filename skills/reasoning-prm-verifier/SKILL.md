---
name: reasoning-prm-verifier
description: Reasoning process-supervision design for PRMs, verifiers, step labels, candidate selection, and reasoning-specific reward signals. Use when Codex needs to answer questions such as 'should we train a PRM or a verifier', 'how do we label reasoning steps', 'is best-of-n enough', or build process supervision for reasoning improvement.
---

# Reasoning PRM Verifier

Use this skill when the reasoning bottleneck is process supervision rather than broad reasoning strategy.

## Use This Skill First When

- the team already knows the target is reasoning improvement
- the main question is PRM vs verifier vs candidate ranking
- reasoning traces and labels are the hard part
- a reasoning model needs stronger process-level supervision

## Core Workflow

1. Clarify whether the supervision target is step quality, final correctness, or candidate ranking.
2. Decide whether PRM, verifier, or best-of-n is the right primitive.
3. Define the reasoning trace schema and step-boundary policy.
4. Choose labeling strategy: human, synthetic, rule-based, or hybrid.
5. Define how the process signal will be used: filtering, ranking, RL, or distillation.
6. Add correctness-focused evaluation rather than style-focused judging.

## Components

- step schema
- step labels
- PRM objective
- verifier objective
- candidate ranking
- downstream use in best-of-n or RL

## Operating Rules

- Step quality and final correctness are related but not identical.
- Use rule-based supervision whenever the domain allows it.
- Keep reasoning traces structured; do not flatten them too early.
- Prefer the cheapest process signal that actually improves reasoning.
- Make sure the verifier or PRM is evaluated on correctness, not verbosity.

## Do Not Lead With This Skill When

- the project still has not decided whether reasoning is the real target
- the main issue is generic preference alignment
- the task does not require process-level supervision
- the bottleneck is systems throughput rather than reasoning supervision

## Typical Hand-Offs

- to `llm-reasoning-posttrain` for the broader reasoning recipe
- to `llm-synthetic-data` for trace and label generation
- to `online-rl-posttraining` if process signals will drive rollouts
- to `llm-eval-loop` for correctness-focused validation

## Output Shape

When using this skill, produce:

- supervision target
- PRM vs verifier decision
- trace schema
- label strategy
- downstream use plan
- evaluation checks

## References

- Read `references/components.md` for PRM and verifier design choices.
