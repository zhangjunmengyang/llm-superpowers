# Default Workflows

This document shows how the skills should compose in realistic algorithm-engineering work.

## Workflow 1: New Post-Training Plan

Use when a team has a base model and a target behavior but no settled recipe.

1. `llm-posttrain-pipeline`
2. `sft-recipe-design` or `preference-optimization`
3. `llm-synthetic-data` or `data-curation-and-filtering`
4. `llm-eval-loop`
5. `llm-training-systems` if scaling becomes the bottleneck

Expected outputs:

- stage and algorithm choice
- dataset schema
- benchmark plan
- scaling notes

## Workflow 2: Reasoning Improvement

Use when the model needs stronger math, code, or multi-step reasoning.

1. `llm-reasoning-posttrain`
2. `reasoning-prm-verifier`
3. `llm-synthetic-data` or `data-curation-and-filtering`
4. `llm-eval-loop`
5. `llm-training-systems` if the RL or verifier loop becomes expensive

Expected outputs:

- reasoning recipe
- trace and label schema
- verifier or reward definition
- reasoning-specific eval gates

## Workflow 3: Research Reproduction

Use when the starting point is a paper or public repo.

1. `llm-research-to-recipe`
2. `llm-posttrain-pipeline`
3. one specialist module such as `sft-recipe-design`, `preference-optimization`, or `reward-modeling`
4. `llm-eval-loop`
5. `llm-training-systems` if the reproduction must scale

Expected outputs:

- faithful recipe
- cheaper approximation
- experiment plan
- validation criteria

## Workflow 4: Regression Triage

Use when a new checkpoint looks better in demos but something feels off.

1. `llm-eval-loop`
2. `llm-posttrain-pipeline`
3. `llm-synthetic-data`, `reasoning-prm-verifier`, or `preference-optimization`

Expected outputs:

- regression diagnosis
- likely root-cause layer
- next experiment proposal

## Workflow 5: Systems Bottleneck

Use when the recipe is mostly settled and the run is blocked by systems issues.

1. `llm-training-systems`
2. `llm-eval-loop`

Expected outputs:

- bottleneck hypothesis
- measured intervention order
- rollback-safe optimization plan
