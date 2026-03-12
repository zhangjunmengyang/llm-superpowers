---
name: llm-posttrain-pipeline
description: Concrete experiment design for LLM post-training stages such as SFT, preference optimization, reward modeling, rejection sampling, and online RL. Use when Codex needs to answer questions such as 'what is the next run', 'what single change surface should we test', 'what is the smallest runnable recipe', or turn a vague post-training goal into an experiment card with hypothesis, success metric, budget, and rollback point.
---

# LLM Posttrain Pipeline

Use this skill to design the next real experiment, not to create a taxonomy of training stages.

## Use This Skill First When

- the team has a post-training goal but no disciplined next run
- the next experiment should choose among SFT, preference optimization, reward modeling, rejection sampling, or online RL
- the user needs one smallest-runnable recipe with a named baseline and metric
- a research idea has to become an experiment card instead of a whiteboard debate

## Core Workflow

1. Name the baseline, target behavior, and primary metric.
2. Choose one change surface only: stage, data, reward, rollout, or formatting.
3. Pick the lightest stage that can plausibly move the target metric.
4. Choose the smallest public framework or codebase that can run the idea.
5. Define the first run, not the whole research roadmap.
6. Write explicit success, kill, and rollback conditions.

## Allowed Change Surfaces

- training stage
- dataset schema
- reward or verifier
- rollout unit
- chat template or formatting
- sequence regime
- distillation target

## Required Output

When using this skill, produce:

- baseline
- owner question
- chosen change surface
- chosen stage and why
- smallest runnable recipe
- recommended open-source framework
- success condition
- kill condition
- rollback point

## Hard Rules

- prefer the cheapest stage that can move the target behavior
- do not jump to online RL if SFT, DPO, or rejection sampling can answer the question
- do not change algorithm, dataset, and eval suite simultaneously in the first serious run
- keep the baseline, tokenizer, data schema, reward logic, and eval slice explicit
- separate proof-of-life, scale-up, and production recipes
- if the user wants an open-source starting point, map to a public repo instead of inventing a stack

## Do Not Lead With This Skill When

- the algorithm is already chosen and the bottleneck is now data curation only
- the issue is a finished candidate run that needs evaluation or regression diagnosis
- the run is failing for systems reasons rather than recipe reasons
- the starting point is already a concrete paper reproduction plan

## References

- Read `references/algorithms.md` for experiment-design heuristics and stage choice rules.
- Read `references/frameworks.md` for public framework selection and first-run mapping.
