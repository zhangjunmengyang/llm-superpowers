---
name: llm-research-to-recipe
description: Research-to-engineering translation for LLM training, alignment, reasoning, and systems papers or repositories. Use when Codex needs to read a paper, benchmark, or public GitHub project, extract the real contribution, identify hidden implementation assumptions, and convert it into a runnable recipe, ablation plan, or reusable skill for an open-source algorithm engineering workflow.
---

# LLM Research To Recipe

Use this skill to stop papers from remaining PDFs and turn them into engineering assets.

## Core Workflow

1. Identify the paper's real claim, not the marketing frame.
2. Extract the minimum recipe: objective, data, model, training loop, reward, and eval.
3. Separate must-have ingredients from optional ablations.
4. Check whether a public repo exists and how faithful it is.
5. Produce a runnable reproduction plan and a cheaper approximation plan.

## Operating Rules

- Treat code as ground truth over prose when the two disagree.
- Record hidden dependencies: tokenizer assumptions, data cleaning, reward definitions, decoding settings, and hardware scale.
- Do not copy hyperparameters blindly across model sizes.
- Always define what counts as a faithful reproduction versus a pragmatic approximation.

## Output Shape

When using this skill, produce:

- one-sentence contribution
- minimum recipe
- hidden assumptions
- public repo mapping
- reproduction plan
- cheaper approximation plan

## References

- Read `references/template.md` for the extraction template.
