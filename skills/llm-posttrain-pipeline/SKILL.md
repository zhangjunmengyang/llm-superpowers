---
name: llm-posttrain-pipeline
description: Framework-agnostic LLM post-training workflow design for SFT, preference optimization, reward modeling, online RL, rejection sampling, distillation, and hybrid alignment pipelines. Use when Codex needs to choose the right post-training algorithm, compare public frameworks, translate a research idea into a runnable recipe, or design a minimal and scalable training plan for any LLM project rather than a single repository.
---

# LLM Posttrain Pipeline

Use this skill to turn a vague post-training request into a concrete algorithm and tooling plan without assuming a specific codebase.

## Core Workflow

1. Classify the request into a stage or short sequence of stages.
2. Decide whether offline post-training is enough or online RL is required.
3. Pick the lightest algorithm that can plausibly move the target metric.
4. Choose a public framework that matches the scale and engineering constraints.
5. Define the dataset schema, acceptance metrics, and compute budget before implementation.
6. Produce a smallest-runnable recipe first, then a scale-up path.

## Stage Map

- Continued pretraining
- SFT
- preference optimization
- reward modeling
- online RL
- rejection sampling and best-of-n
- distillation

## Operating Rules

- Prefer the cheapest stage that can change the target behavior.
- Do not jump to online RL when SFT, DPO, or rejection sampling can solve the problem.
- Treat data and evaluation as first-class. Most post-training failures are data or reward issues, not optimizer issues.
- Keep the base model, tokenizer, data schema, reward logic, and eval suite explicit in every plan.
- Separate proof-of-life, scaling recipe, and production recipe. They are not the same artifact.
- If the user asks for an open-source baseline, map the plan to a public framework and repo rather than inventing a private stack.

## Output Shape

When using this skill, produce:

- target stage
- algorithm choice and why
- minimal dataset schema
- recommended open-source framework
- smallest runnable recipe
- scale-up path
- acceptance metrics

## References

- Read `references/algorithms.md` for algorithm selection rules.
- Read `references/frameworks.md` for framework and repository choices.
