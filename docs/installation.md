# Installation And Usage

This repository is a training operating system packaged as a skill pack.

Install the skills into your runtime, then use the repository's `programs/` docs and templates to run real experiment loops.

## Distribution Model

The install story combines three patterns that already work well in public skill ecosystems:

- bootstrap-file install for agent-driven setup
- one-command shell install for direct users
- universal repo install through OpenSkills

## Install By Runtime

### Claude Code

Global install:

```bash
curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh | bash -s -- --runtime claude-code --profile starter
```

Project-local install:

```bash
curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh | bash -s -- --runtime claude-code-project --profile starter
```

### Codex

Global install:

```bash
curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh | bash -s -- --runtime codex --profile starter
```

Bootstrap file:

- [../.codex/INSTALL.md](../.codex/INSTALL.md)

### OpenCode

Global install:

```bash
curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh | bash -s -- --runtime opencode --profile starter
```

Project-local install:

```bash
curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh | bash -s -- --runtime opencode-project --profile starter
```

### OpenClaw

Global install:

```bash
curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh | bash -s -- --runtime openclaw --profile starter
```

### OpenSkills-Compatible Agents

```bash
npx -y openskills install -u -y https://github.com/zhangjunmengyang/llm-superpowers.git
npx -y openskills sync
```

See [runtime-matrix.md](runtime-matrix.md) for the compact compatibility table.

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

This repository has been verified to install cleanly through OpenSkills and exposes all 17 current skills.

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

## What `starter` Installs

The `starter` profile is the operating-system core:

- `llm-posttrain-pipeline`
- `llm-synthetic-data`
- `llm-eval-loop`
- `llm-training-systems`
- `llm-research-to-recipe`
- `run-ledger-and-keep-discard`
- `checkpoint-regression-triage`
- `throughput-and-oom-triage`

Add reasoning-specific skills with `--skill llm-reasoning-posttrain --skill reasoning-prm-verifier`, or switch to `--profile all`.

## Repository Usage

At minimum, another agent runtime needs access to:

- `skills/*/SKILL.md`
- `skills/*/agents/openai.yaml`
- `skills/*/references/*`
- `programs/*`
- `programs/templates/*`

## Generic Use Pattern

1. Clone the repository.
2. Point your runtime or skill loader at the `skills/` directory.
3. Open one program in `programs/`.
4. Create a `runboard/` directory and copy the needed templates.
5. Invoke one lead skill to produce the next artifact.
6. Log the result and keep or discard the run.

If your runtime cannot discover skills directly, use the fallback patterns in [runtime-patterns.md](runtime-patterns.md).

## Five-Minute Start

If you want the shortest path:

1. Clone the repository.
2. Load or expose the `skills/` directory to your runtime.
3. Open `programs/experiment-loop.md`.
4. Create `runboard/` and copy `programs/templates/experiment-card.md` plus `programs/templates/results.tsv`.
5. Start with this prompt:

```text
Use $llm-posttrain-pipeline to turn this objective into one experiment card with a named baseline, one change surface, a success condition, a kill condition, and a rollback point.
```

6. Run the experiment.
7. Use `$llm-eval-loop` and `$run-ledger-and-keep-discard` to decide whether the run advances the baseline.

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

- `--runtime claude-code`
- `--runtime claude-code-project`
- `--runtime codex`
- `--runtime opencode`
- `--runtime opencode-project`
- `--runtime openclaw`
- `--target-dir <path>`
- `--profile starter`
- `--profile all`
- `--skill <name>` repeated for selective installs
- `--mode auto|symlink|copy`
- `--force`
- `--dry-run`
- `--list`

## Installation Modes By Use Case

- use `./scripts/install.sh --runtime claude-code --profile starter` for a personal Claude Code install
- use `./scripts/install.sh --runtime codex --profile starter` when you want the fastest Codex setup
- use `./scripts/install.sh --runtime opencode --profile starter` for a personal OpenCode install
- use `./scripts/install.sh --runtime openclaw --profile starter` for a personal OpenClaw install
- use `./scripts/install.sh --target-dir <path> --profile all` when another runtime has a known skill directory
- use `npx -y openskills install -u -y https://github.com/zhangjunmengyang/llm-superpowers.git` when you want a cross-tool repo installer

## Recommended Starting Pattern

- use `programs/experiment-loop.md` plus `llm-posttrain-pipeline` for new runs
- use `programs/eval-board.md` plus `llm-eval-loop` for checkpoint comparison
- use `programs/systems-war-room.md` plus `llm-training-systems` for OOM or throughput triage
- use `programs/research-to-experiment.md` plus `llm-research-to-recipe` for paper-to-run translation
- add `llm-reasoning-posttrain` only when the target is reasoning behavior specifically

## Current Structure

Programs:

- `experiment-loop`
- `eval-board`
- `systems-war-room`
- `research-to-experiment`

Core operating skills:

- `llm-posttrain-pipeline`
- `llm-synthetic-data`
- `llm-eval-loop`
- `llm-training-systems`
- `llm-research-to-recipe`
- `run-ledger-and-keep-discard`
- `checkpoint-regression-triage`
- `throughput-and-oom-triage`

Additional skills:

- `llm-reasoning-posttrain`
- `sft-recipe-design`
- `preference-optimization`
- `reward-modeling`
- `online-rl-posttraining`
- `reasoning-prm-verifier`
- `data-curation-and-filtering`
- `eval-and-regression-gates`
- `training-systems-debug`

## Next Additions

The next install-layer improvements worth adding are:

- more native runtime presets once their skill directories are stable
- a compatibility table for more AGENTS-based editors
- optional package-manager wrappers for teams that want pinned internal installs
