# LLM Algorithm Engineer Superpowers

An open skill pack for LLM algorithm engineers.

This project is for the core training side of LLM engineering: post-training, finetuning, alignment, reasoning, evaluation, data, and training systems. It is intentionally not an AI application or agent workflow pack.

## Vision

The goal is to turn high-value algorithm engineering workflows into reusable superpowers.

Most open LLM work is still fragmented across:

- papers
- training repos
- notebooks
- issue threads
- benchmark scripts
- tribal knowledge

This pack tries to compress that mess into reusable skills that another coding agent can invoke directly.

The end state is not an awesome-list. The end state is a practical operating layer for LLM algorithm engineers:

- choose the right post-training algorithm
- design the right dataset schema
- turn a paper into a runnable recipe
- debug scaling and systems issues
- evaluate progress with real gates instead of vibes

## Scope

This pack focuses on:

- continued pretraining
- SFT
- preference optimization
- reward modeling
- online RL for LLMs
- reasoning post-training
- synthetic data for training
- evaluation and regression detection
- distributed training and inference systems
- research-to-recipe translation

This pack does not focus on:

- agent products
- RAG application architecture
- workflow automation for business apps
- general-purpose prompt engineering

## Principles

- framework-agnostic
- open-source first
- operational over academic
- narrow but high-leverage
- reusable across repositories
- optimized for training and post-training work

## Current Skills

- `llm-posttrain-pipeline`
  - choose stage, algorithm, and framework
- `llm-synthetic-data`
  - design reusable synthetic training datasets
- `llm-reasoning-posttrain`
  - build reasoning, verifier, PRM, and RL recipes
- `llm-eval-loop`
  - define benchmark plans and acceptance gates
- `llm-training-systems`
  - debug memory, throughput, stability, and serving bottlenecks
- `llm-research-to-recipe`
  - turn papers and repos into runnable engineering recipes

## Repository Layout

```text
llm-superpowers/
├── README.md
└── skills/
    ├── llm-posttrain-pipeline/
    ├── llm-synthetic-data/
    ├── llm-reasoning-posttrain/
    ├── llm-eval-loop/
    ├── llm-training-systems/
    └── llm-research-to-recipe/
```

Each skill contains:

- `SKILL.md`
- `agents/openai.yaml`
- `references/`

## Public Foundations

This pack is informed by strong open-source work, especially:

- [anthropics/skills](https://github.com/anthropics/skills)
- [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs)
- [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills)
- [huggingface/trl](https://github.com/huggingface/trl)
- [OpenRLHF/OpenRLHF](https://github.com/OpenRLHF/OpenRLHF)
- [volcengine/verl](https://github.com/volcengine/verl)
- [huggingface/open-r1](https://github.com/huggingface/open-r1)
- [allenai/open-instruct](https://github.com/allenai/open-instruct)
- [pytorch/torchtune](https://github.com/pytorch/torchtune)
- [OpenAccess-AI-Collective/axolotl](https://github.com/OpenAccess-AI-Collective/axolotl)

## Roadmap

### V0

Build the minimum useful core:

- post-training pipeline selection
- synthetic data patterns
- reasoning and PRM recipes
- evaluation loops
- training systems debugging
- paper-to-recipe extraction

### V1

Split the current skills into sharper algorithm modules:

- `sft-recipe-design`
- `preference-optimization`
- `reward-modeling`
- `online-rl-posttraining`
- `reasoning-prm-verifier`
- `data-curation-and-filtering`
- `eval-and-regression-gates`
- `training-systems-debug`

### V2

Add more advanced algorithm engineering coverage:

- data mixture design
- decontamination and leakage checks
- long-context post-training
- distillation and model merging
- rejection sampling and best-of-n pipelines
- curriculum and staged post-training
- reward shaping and judge design
- scaling-law-aware recipe selection

### V3

Make the pack production-grade as a standalone public repo:

- installation docs for Codex, Claude, Cursor, and compatible runtimes
- skill packaging conventions
- cross-framework examples
- tests and validation for skill quality
- optional MCP integrations for papers, GitHub, datasets, and experiments

## Planned Additions

Near-term additions I would make next:

- `sft-recipe-design`
- `preference-optimization`
- `reward-modeling`
- `online-rl-posttraining`
- `reasoning-prm-verifier`
- `data-curation-and-filtering`
- `long-context-posttraining`
- `distillation-and-merging`

## Repository Strategy

Right now this lives under `skills/` inside another repo. The intended direction is to extract it into its own public repository once the core modules stabilize.

That standalone repo should eventually have:

- a clean root README
- install and usage docs
- examples by framework
- contribution guidelines
- release notes
- a stable naming scheme for skills

## Non-Goals

- being a benchmark leaderboard repo
- being another giant awesome-list
- being tied to one framework
- being tied to one codebase
- mixing algorithm training skills with product-layer application skills

## Status

This is an early but real starting point, not the finished system.

The right next step is to keep sharpening the algorithm modules until each one feels like a real superpower, not a category label.
