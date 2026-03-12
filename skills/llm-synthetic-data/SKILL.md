---
name: llm-synthetic-data
description: Synthetic-data design for instruction corpora, preference pairs, reward data, reasoning traces, and rollout pools in LLM training. Use when Codex needs to answer questions such as 'what exact schema should we generate', 'what should be synthesized versus reviewed', 'how do we control contamination and negative quality', or turn a vague data need into a concrete source inventory, rubric, schema, and quality gates.
---

# LLM Synthetic Data

Use this skill to design a data product that can survive audit, not just a prompting idea.

## Use This Skill First When

- the bottleneck is data quality or schema design
- the team needs instruction, preference, reward, or reasoning data
- synthetic generation exists but filtering and negative-sample quality are unclear
- a training plan is blocked on dataset format rather than algorithm choice

## Core Workflow

1. Name the target stage before generating any samples.
2. Build a source inventory: raw sources, teacher model, human review, or rule-based labels.
3. Choose the smallest viable schema for the stage.
4. Define what should be synthesized, what should be filtered, and what requires manual review.
5. Freeze quality gates before bulk generation.

## Data Products

- instruction tuning data
- preference pairs
- reward model pairs or scalar labels
- step-by-step reasoning traces
- PRM labels
- rollout prompts

## Required Output

When using this skill, produce:

- target stage
- source inventory
- minimal schema
- generation pattern
- filtering or review policy
- export format
- contamination risks

## Hard Rules

- Start from schema, not from prompting style.
- Prefer narrow, high-quality datasets over huge noisy dumps.
- Keep synthetic provenance explicit.
- Generate contrastive negatives deliberately.
- Keep train and eval generation pipelines separate.
- Record contamination risk and reward rubric assumptions.
- Do not generate at scale before the quality gates are fixed.

## Do Not Lead With This Skill When

- the main question is which post-training algorithm to choose
- the problem is primarily reasoning-recipe design rather than data shape
- the run is blocked by systems issues
- the team already has candidate checkpoints and needs evaluation rather than new data

## References

- Read `references/patterns.md` for product matrices, quality gates, and common generation paths.
