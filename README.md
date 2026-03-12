# LLM Algorithm Engineer Superpowers

[English](README.md) | [简体中文](README.zh-CN.md)

Only the root README is translated. The rest of the repository is maintained in English to avoid documentation drift.

`llm-superpowers` is no longer centered on generic skill taxonomies.

Its core unit is now the **program**:

- a concrete operating loop
- explicit artifacts
- named metrics
- keep or discard decisions
- escalation paths into eval, systems, or research review

Skills remain, but they are now local primitives.
Programs own the sequence.

## What This Repository Is

This repository is for the training side of LLM engineering:

- post-training
- data design
- evaluation and regression review
- systems triage
- research reproduction

It is not:

- an AI application framework
- an awesome list
- a benchmark leaderboard
- a loose collection of algorithm category cards

## The Paradigm

The repository has three layers:

1. **Programs**
   - long-running operating loops such as experiment management, eval review, and systems triage
2. **Skills**
   - sharp local procedures such as experiment design, eval-board construction, data-product design, and run-ledger discipline
3. **Templates**
   - concrete artifacts such as `results.tsv`, experiment cards, eval boards, and triage logs

The rule is simple:

- programs orchestrate
- skills do one job well
- templates make the work durable

## Programs

Start here:

- [programs/README.md](programs/README.md)
- [programs/experiment-loop.md](programs/experiment-loop.md)
- [programs/eval-board.md](programs/eval-board.md)
- [programs/systems-war-room.md](programs/systems-war-room.md)
- [programs/research-to-experiment.md](programs/research-to-experiment.md)

These are the real operating modes of the repository.

## High-Value Skills

The most useful skills right now are:

- `llm-posttrain-pipeline`
  - design the next real run
- `llm-synthetic-data`
  - design a data product that can survive audit
- `llm-eval-loop`
  - build a real evaluation board
- `llm-training-systems`
  - run measured systems triage
- `llm-research-to-recipe`
  - extract irreducibles and first runnable experiments
- `run-ledger-and-keep-discard`
  - decide whether a run advances the baseline
- `checkpoint-regression-triage`
  - turn bad slices into the next isolating run
- `throughput-and-oom-triage`
  - fix operationally invalid runs one axis at a time

## Quick Start

1. Install the repository into your runtime.
   - see [docs/installation.md](docs/installation.md)
2. Create a `runboard/` directory in your project.
3. Copy the templates from [programs/templates](programs/templates).
4. Pick one program.
5. Run the loop with one lead skill at a time.

If you only want one first prompt, use:

```text
Use $llm-posttrain-pipeline to turn this objective into one experiment card with a named baseline, one change surface, a success condition, a kill condition, and a rollback point.
```

## Install

### Claude Code

```bash
curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh | bash -s -- --runtime claude-code --profile starter
```

### Codex

```bash
curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh | bash -s -- --runtime codex --profile starter
```

Or tell Codex:

```text
Fetch and follow instructions from https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/.codex/INSTALL.md
```

### OpenCode

```bash
curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh | bash -s -- --runtime opencode --profile starter
```

### OpenClaw

```bash
curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh | bash -s -- --runtime openclaw --profile starter
```

### OpenSkills-Compatible Environments

```bash
npx -y openskills install -u -y https://github.com/zhangjunmengyang/llm-superpowers.git
npx -y openskills sync
```

For the full matrix, see [docs/runtime-matrix.md](docs/runtime-matrix.md).

## Repository Layout

```text
llm-superpowers/
├── README.md
├── README.zh-CN.md
├── programs/
│   ├── README.md
│   ├── experiment-loop.md
│   ├── eval-board.md
│   ├── systems-war-room.md
│   ├── research-to-experiment.md
│   └── templates/
├── skills/
│   ├── llm-posttrain-pipeline/
│   ├── llm-synthetic-data/
│   ├── llm-eval-loop/
│   ├── llm-training-systems/
│   ├── llm-research-to-recipe/
│   ├── run-ledger-and-keep-discard/
│   ├── checkpoint-regression-triage/
│   └── throughput-and-oom-triage/
└── docs/
    ├── installation.md
    ├── runtime-matrix.md
    └── runtime-patterns.md
```

## Design Rules

- programs own orchestration
- skills should be independently usable
- every serious run should leave behind durable artifacts
- no keep decision without a named baseline
- no signoff from averages only
- no systems “fix” without quality recheck
- no paper reproduction without irreducibles, approximation, and kill criteria

## Public Foundations

This repository is especially informed by:

- [obra/superpowers](https://github.com/obra/superpowers)
- [karpathy/autoresearch](https://github.com/karpathy/autoresearch)
- [anthropics/skills](https://github.com/anthropics/skills)
- [huggingface/trl](https://github.com/huggingface/trl)
- [OpenRLHF/OpenRLHF](https://github.com/OpenRLHF/OpenRLHF)
- [volcengine/verl](https://github.com/volcengine/verl)
- [huggingface/open-r1](https://github.com/huggingface/open-r1)
- [allenai/open-instruct](https://github.com/allenai/open-instruct)

## Near-Term Direction

The next useful additions are not broader labels.

They are sharper operating modules such as:

- data-mixture-design
- reward-hacking-audit
- long-context-posttraining
- sample-review-protocol
- judge-and-reward-shaping

## Open Source Basics

- [LICENSE](LICENSE)
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [docs/installation.md](docs/installation.md)
