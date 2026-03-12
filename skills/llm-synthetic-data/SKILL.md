---
name: llm-synthetic-data
description: Synthetic dataset design and generation for LLM training, alignment, and reasoning. Use when Codex needs to create or refine instruction corpora, preference pairs, reward data, reasoning traces, rejection-sampling pools, or schema-compatible datasets for SFT, DPO, reward models, PRM, RL, or public frameworks such as TRL, OpenRLHF, veRL, and Open-R1.
---

# LLM Synthetic Data

Use this skill to design the cheapest high-signal dataset that matches the target stage and a public training stack.

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
