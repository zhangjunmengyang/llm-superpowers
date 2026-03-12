---
name: llm-research-to-recipe
description: Research-to-engineering translation for LLM training, alignment, reasoning, and systems papers or repositories. Use when Codex needs to answer questions such as 'what is the real contribution here', 'what is required for a faithful reproduction', 'what is the cheaper approximation', read a paper, benchmark, or public GitHub project, extract the real contribution, identify hidden implementation assumptions, and convert it into a runnable recipe, ablation plan, or reusable skill for an open-source algorithm engineering workflow.
---

# LLM Research To Recipe

Use this skill to stop papers from remaining PDFs and turn them into engineering assets.

## Use This Skill First When

- the starting point is a paper or public repo rather than an existing experiment plan
- the team needs a faithful reproduction target and a cheaper approximation
- a result looks strong but the real training recipe is unclear
- hidden implementation assumptions are likely more important than the headline claim

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

## Do Not Lead With This Skill When

- the research has already been translated and the remaining issue is execution
- the bottleneck is data construction, eval design, or systems performance
- the team already knows the recipe and only needs to scale it

## Typical Hand-Offs

- to `llm-posttrain-pipeline` for experiment planning
- to `llm-eval-loop` for reproduction validation
- to `llm-training-systems` if the reproduced recipe is operationally expensive

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
