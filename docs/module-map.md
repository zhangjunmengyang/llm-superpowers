# Module Map

This document explains the relationship between umbrella skills and specialist modules.

## Two-Layer Model

`llm-superpowers` now has two layers:

### 1. Umbrella Skills

These lead broad work modes.

- `llm-posttrain-pipeline`
- `llm-synthetic-data`
- `llm-reasoning-posttrain`
- `llm-eval-loop`
- `llm-training-systems`
- `llm-research-to-recipe`

### 2. Specialist Modules

These handle deeper execution inside a narrower slice of work.

- `sft-recipe-design`
- `preference-optimization`
- `reward-modeling`
- `online-rl-posttraining`
- `reasoning-prm-verifier`
- `data-curation-and-filtering`

## Mapping

| Umbrella skill | Specialist modules it should commonly hand off to |
| --- | --- |
| `llm-posttrain-pipeline` | `sft-recipe-design`, `preference-optimization`, `reward-modeling`, `online-rl-posttraining` |
| `llm-synthetic-data` | `data-curation-and-filtering` |
| `llm-reasoning-posttrain` | `reasoning-prm-verifier` |
| `llm-eval-loop` | none yet; a future `eval-and-regression-gates` module should live here |
| `llm-training-systems` | none yet; a future `training-systems-debug` module should sharpen this layer |
| `llm-research-to-recipe` | can hand off to any umbrella or specialist module after extraction |

## Design Rule

Use umbrellas to decide direction.

Use specialists to make the direction concrete.

If a specialist starts absorbing broad orchestration, it should probably move back into an umbrella.
