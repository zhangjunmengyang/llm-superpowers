---
name: llm-reasoning-posttrain
description: Reasoning-focused post-training workflows for step SFT, verifier training, process reward models, rejection sampling, reasoning RL, and math or code tasks. Use when Codex needs to design R1-style reasoning recipes, preserve step structure, build process supervision data, choose verifier or reward strategies, or bridge a research idea to frameworks such as Open-R1, veRL, TRL, or other public reasoning stacks.
---

# LLM Reasoning Posttrain

Use this skill when the task is not generic alignment but reasoning quality: step decomposition, process supervision, verifier-friendly traces, tool-assisted reasoning, or math and code RL.

## Core Workflow

1. Decide whether the task is step SFT, verifier training, PRM, rejection sampling, or reasoning RL.
2. Preserve the reasoning trajectory as structured data. Do not flatten steps early.
3. Match the data format to the target framework.
4. Keep step boundaries, labels, and final-answer supervision consistent.
5. Evaluate reasoning quality separately from style quality.

## Typical Components

- step SFT
- verifier or judge
- process reward model
- candidate generation
- best-of-n or rejection sampling
- online RL or search
- final distillation

## Rules

- Treat step boundaries as first-class data.
- Keep the final answer or verifier target separate from intermediate reasoning.
- For PRM, labels belong to steps or separator positions, not to the whole sample.
- Use rule-based grading whenever the task admits a reliable verifier.
- Distinguish reasoning quality from verbosity.
- If the user asks for R1-style RL, define rollout, reward, and distillation separately.

## Output Shape

When using this skill, produce:

- reasoning objective
- trace schema
- verifier or reward definition
- recommended framework
- base recipe
- eval criteria for correctness

## References

- Read `references/recipes.md` for public reasoning recipes and upgrade paths.
