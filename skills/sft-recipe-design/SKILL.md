---
name: sft-recipe-design
description: Supervised finetuning recipe design for instruction tuning, format alignment, domain adaptation, long-context adaptation, and teacher distillation bootstraps. Use when Codex needs to answer questions such as 'what should the SFT dataset look like', 'should we use full finetuning or PEFT', 'how should we mask loss and format prompts', or design and review a strong SFT recipe before DPO, reward modeling, or RL.
---

# SFT Recipe Design

Use this skill when the main problem is building a strong supervised finetuning recipe rather than choosing between broad post-training stages.

## Use This Skill First When

- the team already knows SFT is the next stage
- the main question is how to structure the SFT recipe
- the model needs instruction following, format alignment, or domain behavior bootstrapping
- the project needs a clean SFT foundation before preference optimization or RL

## Core Workflow

1. Clarify the SFT objective: instruction following, domain adaptation, formatting, reasoning bootstrap, or distillation.
2. Choose the conversation or completion format and loss-mask policy.
3. Define the dataset mixture, balancing strategy, and chat template.
4. Decide between full finetuning, LoRA, QLoRA, or another PEFT variant.
5. Set sequence length, packing strategy, and tokenizer assumptions.
6. Define the eval slice that proves the SFT recipe is helping rather than memorizing.

## Critical Decisions

- prompt and response format
- loss on assistant-only tokens vs full sequence
- data mixture weights
- instruction diversity vs domain density
- chat-template or special-token policy
- PEFT vs full finetuning
- sequence length and packing

## Operating Rules

- Treat SFT as a recipe-design problem, not just a dataset-dumping problem.
- A mediocre SFT base poisons later DPO, reward modeling, and RL.
- Keep formatting and target behavior explicit; do not hide them in generic chat data.
- Avoid mixing unrelated distributions until you can explain why each one is included.
- Validate the chat template and loss mask before long runs.

## Do Not Lead With This Skill When

- the team still has not decided whether SFT is the right stage
- the real bottleneck is preference data or reward design
- the target is reasoning-specific PRM or verifier design
- the main blocker is systems performance rather than SFT recipe quality

## Typical Hand-Offs

- to `llm-posttrain-pipeline` when stage choice is still open
- to `data-curation-and-filtering` for dataset triage and mixture cleanup
- to `llm-eval-loop` for baseline vs candidate SFT checks
- to `preference-optimization` once a strong SFT base exists

## Output Shape

When using this skill, produce:

- SFT objective
- data schema and chat format
- loss-mask policy
- mixture design
- finetuning method
- acceptance checks

## References

- Read `references/recipes.md` for SFT design heuristics and failure modes.
