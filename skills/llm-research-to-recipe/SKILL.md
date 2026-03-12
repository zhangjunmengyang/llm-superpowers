---
name: llm-research-to-recipe
description: Research-to-experiment translation for LLM papers and public repositories. Use when Codex needs to answer questions such as 'what is the real contribution', 'what is irreducible', 'what is the cheapest faithful first run', or turn a paper or repo into a reproduction plan with hidden assumptions, approximation path, first ablations, and kill criteria.
---

# LLM Research To Recipe

Use this skill to turn a paper or repo into the next runnable experiment.

## Use This Skill First When

- the starting point is a paper or public repo rather than an existing experiment plan
- the team needs both a faithful reproduction target and a cheaper approximation
- a result looks strong but the real runnable recipe is unclear
- hidden implementation assumptions are likely more important than the headline claim

## Core Workflow

1. Identify the real claim, not the marketing frame.
2. Extract the irreducible ingredients: data, objective, reward, inference tricks, and eval.
3. Separate faithful reproduction from cheaper approximation.
4. Extract the first ablation queue, not an endless wishlist.
5. Define the first runnable experiment and kill criteria.

## Required Output

When using this skill, produce:

- one-sentence contribution
- irreducible ingredients
- hidden assumptions
- faithful reproduction
- cheaper approximation
- first ablation queue
- kill criteria

## Hard Rules

- Treat code as ground truth over prose when the two disagree.
- Record hidden dependencies: tokenizer assumptions, data cleaning, reward definitions, decoding settings, and hardware scale.
- Do not copy hyperparameters blindly across model sizes.
- Always define what counts as a faithful reproduction versus a pragmatic approximation.
- Do not confuse “present in the paper” with “essential to the result”.

## Do Not Lead With This Skill When

- the research has already been translated and the remaining issue is execution
- the bottleneck is data construction, eval design, or systems performance
- the team already knows the recipe and only needs to scale it

## References

- Read `references/template.md` for the extraction template.
