# Installation And Usage

This repository is a skill pack. The exact installation flow depends on the coding-agent runtime.

## Distribution Model

The install story combines three patterns that already work well in public skill ecosystems:

- bootstrap-file install for agent-driven setup
- one-command shell install for direct users
- universal repo install through OpenSkills

## One-Command Install

For runtimes with a preset:

```bash
curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh | bash -s -- --runtime codex --profile starter
```

For any runtime with a custom skills directory:

```bash
curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh | bash -s -- --target-dir /path/to/your/runtime/skills --profile all
```

The remote installer clones the repository to a temporary directory and installs from there.

## Universal Install Via OpenSkills

If you want a repo-based install path that already works across OpenSkills-compatible agent environments, use:

```bash
npx -y openskills install -u -y https://github.com/zhangjunmengyang/llm-superpowers.git
npx -y openskills sync
```

This repository has been verified to install cleanly through OpenSkills and exposes all 14 current skills.

## Codex Bootstrap File

For a `superpowers`-style bootstrap flow, this repository also ships:

- [../.codex/INSTALL.md](../.codex/INSTALL.md)

That file is meant to be fetched and followed directly by Codex.

## Local Install

If you prefer to inspect the repository first:

```bash
git clone https://github.com/zhangjunmengyang/llm-superpowers.git
cd llm-superpowers
./scripts/install.sh --runtime codex --profile starter
```

You can switch to `--profile all` when you want the full pack.

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

## Installer Options

The installer supports:

- `--runtime codex`
- `--target-dir <path>`
- `--profile starter`
- `--profile all`
- `--skill <name>` repeated for selective installs
- `--mode auto|symlink|copy`
- `--force`
- `--dry-run`
- `--list`

## Installation Modes By Use Case

- use `./scripts/install.sh --runtime codex --profile starter` when you want the fastest Codex setup
- use `./scripts/install.sh --target-dir <path> --profile all` when another runtime has a known skill directory
- use `npx -y openskills install -u -y https://github.com/zhangjunmengyang/llm-superpowers.git` when you want a cross-tool repo installer

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
