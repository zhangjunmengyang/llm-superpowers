---
name: llm-synthetic-data
description: Synthetic dataset design and generation for LLM training, alignment, and reasoning. Use when Codex needs to answer questions such as 'what should the dataset schema look like', 'how do we build chosen and rejected pairs', 'how do we label reasoning traces', or create and refine instruction corpora, preference pairs, reward data, reasoning traces, rejection-sampling pools, and schema-compatible datasets for SFT, DPO, reward models, PRM, RL, or public frameworks such as TRL, OpenRLHF, veRL, and Open-R1.
---

# LLM Synthetic Data

Use this skill to design the cheapest high-signal dataset that matches the target stage and a public training stack.

## Use This Skill First When

- the bottleneck is data quality or schema design
- the team needs instruction, preference, reward, or reasoning data
- synthetic generation exists but filtering and negative-sample quality are unclear
- a training plan is blocked on dataset format rather than algorithm choice

## Core Workflow

1. Identify the target stage before generating any samples.
2. Choose the smallest viable schema for that stage.
3. Pick a data generation pattern that can be audited cheaply.
4. Validate schema and length constraints before writing training code.
5. Keep a clear split between source generation, filtering, and final export.

## Data Products

- instruction tuning data
- preference pairs
- reward model pairs or scalar labels
- step-by-step reasoning traces
- PRM labels
- rollout prompts

## Rules

- Start from schema, not from prompting style.
- Prefer narrow, high-quality datasets over huge noisy dumps.
- Keep synthetic provenance explicit.
- Generate contrastive negatives deliberately.
- Keep train and eval generation pipelines separate.
- Record contamination risk and reward rubric assumptions.

## Do Not Lead With This Skill When

- the main question is which post-training algorithm to choose
- the problem is primarily reasoning-recipe design rather than data shape
- the run is blocked by systems issues
- the team already has candidate checkpoints and needs evaluation rather than new data

## Typical Hand-Offs

- to `llm-posttrain-pipeline` for recipe selection
- to `data-curation-and-filtering` for filtering, dedup, and contamination control
- to `sft-recipe-design` when SFT format and supervision choices dominate
- to `preference-optimization` when pair quality becomes the main issue
- to `llm-reasoning-posttrain` for reasoning-specific trace design
- to `llm-eval-loop` for contamination-aware validation

## Output Shape

When using this skill, produce:

- target stage
- minimal schema
- generation recipe
- filtering rules
- export format
- acceptance checks
- contamination risks

## References

- Read `references/patterns.md` for generation patterns, schemas, and quality gates.
