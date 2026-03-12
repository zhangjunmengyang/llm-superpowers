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

If your runtime cannot discover skills directly, use the fallback patterns in [runtime-patterns.md](runtime-patterns.md).

## Five-Minute Start

If you want the shortest path:

1. Clone the repository.
2. Load or expose the `skills/` directory to your runtime.
3. Start with this prompt:

```text
Use $llm-posttrain-pipeline to decide the next post-training stage for this model, recommend the best open-source framework, and define the minimum dataset and eval plan.
```

4. If the answer points to a narrower job, switch to the corresponding specialist module.
5. Use the worked examples in `examples/` as templates.

For the fastest first session, also read [first-session.md](first-session.md).

## Integration Patterns

The repository supports three stable integration patterns:

1. direct folder discovery
2. selective symlink install
3. vendored internal dependency

The details are in [runtime-patterns.md](runtime-patterns.md).

If you do not yet have runtime integration, you can still use the repository in prompt-only mode with the examples in [../examples/README.md](../examples/README.md).

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
