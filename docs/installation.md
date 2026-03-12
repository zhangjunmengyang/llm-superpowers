# Installation And Usage

This repository is a skill pack. The exact installation flow depends on the coding-agent runtime.

## Repository Usage

At minimum, another agent runtime needs access to:

- `skills/*/SKILL.md`
- `skills/*/agents/openai.yaml`
- `skills/*/references/*`

## Generic Use Pattern

1. Clone the repository.
2. Point your runtime or skill loader at the `skills/` directory.
3. Invoke one umbrella skill first.
4. Hand off to one or two specialist modules only when needed.

## Recommended Starting Pattern

- use `llm-posttrain-pipeline` for new recipe planning
- use `llm-reasoning-posttrain` for reasoning-specific work
- use `llm-eval-loop` or `eval-and-regression-gates` for checkpoint comparison and signoff
- use `llm-training-systems` or `training-systems-debug` for systems bottlenecks

## Current Structure

Umbrella skills:

- `llm-posttrain-pipeline`
- `llm-synthetic-data`
- `llm-reasoning-posttrain`
- `llm-eval-loop`
- `llm-training-systems`
- `llm-research-to-recipe`

Specialist modules:

- `sft-recipe-design`
- `preference-optimization`
- `reward-modeling`
- `online-rl-posttraining`
- `reasoning-prm-verifier`
- `data-curation-and-filtering`
- `eval-and-regression-gates`
- `training-systems-debug`

## Future

Installation guides for specific runtimes should be added later:

- Codex
- Claude-compatible skill runtimes
- Cursor-compatible loaders
- other OpenSkills-style environments
