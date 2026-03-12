# LLM Algorithm Engineer Superpowers

An open skill pack for LLM algorithm engineers.

This repository is for the core training side of LLM engineering: post-training, finetuning, alignment, reasoning, evaluation, data, and training systems. It is intentionally not an agent-product or AI application workflow pack.

## Why This Exists

High-value algorithm engineering knowledge is still scattered across:

- papers
- training repositories
- notebooks
- benchmark scripts
- issue threads
- team tribal knowledge

The goal of `llm-superpowers` is to compress that knowledge into reusable skills that another coding agent can invoke directly.

This repo is not trying to be:

- another giant awesome-list
- a framework wrapper
- a benchmark leaderboard
- a product-agent toolkit

It is trying to be an operating layer for LLM algorithm work.

## Who This Is For

This repository is for engineers working on:

- continued pretraining
- SFT
- preference optimization
- reward modeling
- online RL for LLMs
- reasoning post-training
- synthetic training data
- evaluation and regression detection
- distributed training and inference systems
- paper-to-recipe translation

Typical users:

- post-training engineers
- alignment and reasoning engineers
- training systems engineers
- research engineers translating papers into production experiments

## Top-Level Design

The design assumption is that an algorithm engineer usually works in one of four modes:

1. Decide what to run.
2. Build the data or recipe.
3. Evaluate whether it worked.
4. Debug why it failed.

The repo is organized around those modes.

### Skill Layers

- Strategy skills
  - choose stage, algorithm, framework, and experiment plan
- Execution skills
  - design data, reasoning recipes, and reproduction plans
- Judgment skills
  - define eval gates and compare baselines
- Systems skills
  - diagnose memory, throughput, stability, and serving bottlenecks

### Two-Layer Architecture

- umbrella skills
  - broad work-mode leaders
  - decide direction, stage, and composition
- specialist modules
  - narrower algorithm modules
  - make one part of the recipe concrete

### Composition Model

Use one lead skill and, at most, one or two support skills.

Examples:

- new alignment plan:
  - lead: `llm-posttrain-pipeline`
  - support: `llm-synthetic-data`, `llm-eval-loop`
- reasoning model improvement:
  - lead: `llm-reasoning-posttrain`
  - support: `llm-synthetic-data`, `llm-eval-loop`
- paper reproduction:
  - lead: `llm-research-to-recipe`
  - support: `llm-posttrain-pipeline`, `llm-training-systems`
- scaling failure:
  - lead: `llm-training-systems`
  - support: `llm-eval-loop`

## Current Skills

| Skill | Primary job | Use first when | Typical hand-off |
| --- | --- | --- | --- |
| `llm-posttrain-pipeline` | Choose stage, algorithm, and framework | you need to decide what recipe to run | `llm-synthetic-data`, `llm-eval-loop` |
| `llm-synthetic-data` | Design reusable training datasets | the bottleneck is data quality, schema, or preference construction | `llm-posttrain-pipeline`, `llm-reasoning-posttrain` |
| `llm-reasoning-posttrain` | Build reasoning, verifier, PRM, and RL recipes | the target is reasoning correctness rather than generic alignment | `llm-synthetic-data`, `llm-eval-loop` |
| `llm-eval-loop` | Define benchmark plans and acceptance gates | you need to compare baseline vs candidate or set ship criteria | `llm-posttrain-pipeline`, `llm-training-systems` |
| `llm-training-systems` | Debug scale, memory, throughput, and stability | the blocker is systems behavior rather than algorithm choice | `llm-eval-loop` |
| `llm-research-to-recipe` | Turn papers and repos into runnable engineering recipes | you need to extract the real recipe from research | `llm-posttrain-pipeline`, `llm-training-systems` |

## Specialist Modules

These are the first V1 modules that sharpen the broad umbrella skills.

| Module | Primary job | Typical umbrella lead |
| --- | --- | --- |
| `sft-recipe-design` | design strong SFT recipes | `llm-posttrain-pipeline` |
| `preference-optimization` | choose and design offline preference methods | `llm-posttrain-pipeline` |
| `reward-modeling` | build and validate reward signals | `llm-posttrain-pipeline` |
| `online-rl-posttraining` | design rollout-based RL recipes | `llm-posttrain-pipeline` |
| `reasoning-prm-verifier` | build process supervision for reasoning | `llm-reasoning-posttrain` |
| `data-curation-and-filtering` | curate and filter training data | `llm-synthetic-data` |
| `eval-and-regression-gates` | turn evaluation into release or rollback decisions | `llm-eval-loop` |
| `training-systems-debug` | diagnose concrete systems failures safely | `llm-training-systems` |

## Work Scenarios

Common scenarios this repo is designed for:

- “We need to improve a base model on a new domain. Should we do CPT, SFT, or DPO first?”
- “Our DPO model got better on demos but regressed on safety and reasoning.”
- “We want to build reasoning data for math or code. Do we need PRM, verifier, or best-of-n?”
- “This paper looks strong. What is the minimum faithful reproduction and what is the cheaper approximation?”
- “The run is OOMing or throughput collapsed. Is this a systems problem or a recipe problem?”
- “We have several checkpoints. What does a credible evaluation loop look like?”

Detailed scenario mapping lives in:

- [docs/work-scenarios.md](/Users/zhangjunmengyang/PycharmProjects/llm-superpowers/docs/work-scenarios.md)
- [docs/default-workflows.md](/Users/zhangjunmengyang/PycharmProjects/llm-superpowers/docs/default-workflows.md)
- [docs/design-principles.md](/Users/zhangjunmengyang/PycharmProjects/llm-superpowers/docs/design-principles.md)
- [docs/module-map.md](/Users/zhangjunmengyang/PycharmProjects/llm-superpowers/docs/module-map.md)
- [docs/installation.md](/Users/zhangjunmengyang/PycharmProjects/llm-superpowers/docs/installation.md)

## Repository Layout

```text
llm-superpowers/
├── README.md
├── docs/
│   ├── design-principles.md
│   ├── work-scenarios.md
│   ├── default-workflows.md
│   ├── module-map.md
│   └── installation.md
└── skills/
    ├── data-curation-and-filtering/
    ├── eval-and-regression-gates/
    ├── llm-posttrain-pipeline/
    ├── llm-synthetic-data/
    ├── llm-reasoning-posttrain/
    ├── llm-eval-loop/
    ├── llm-training-systems/
    ├── llm-research-to-recipe/
    ├── online-rl-posttraining/
    ├── preference-optimization/
    ├── reasoning-prm-verifier/
    ├── reward-modeling/
    ├── sft-recipe-design/
    └── training-systems-debug/
```

Each skill contains:

- `SKILL.md`
- `agents/openai.yaml`
- `references/`

## Design Principles

- framework-agnostic
- open-source first
- operational over academic
- narrow but high-leverage
- reusable across repositories
- optimized for training and post-training work
- explicit about boundaries between skills

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

Add and refine sharper algorithm modules:

- `sft-recipe-design`
- `preference-optimization`
- `reward-modeling`
- `online-rl-posttraining`
- `reasoning-prm-verifier`
- `data-curation-and-filtering`
- `eval-and-regression-gates`
- `training-systems-debug`

### V2

Add deeper algorithm engineering coverage:

- data mixture design
- decontamination and leakage checks
- long-context post-training
- distillation and model merging
- rejection sampling and best-of-n pipelines
- curriculum and staged post-training
- reward shaping and judge design
- scaling-law-aware recipe selection

### V3

Make the pack production-grade as a standalone repo:

- installation docs for Codex, Claude, Cursor, and compatible runtimes
- skill packaging conventions
- cross-framework examples
- tests and validation for skill quality
- optional MCP integrations for papers, GitHub, datasets, and experiments

## Near-Term Additions

The next skills worth adding are:

- `long-context-posttraining`
- `distillation-and-merging`
- `data-mixture-design`
- `judge-and-reward-shaping`

## Non-Goals

- being tied to one framework
- being tied to one codebase
- mixing algorithm-training skills with product-agent skills
- replacing framework docs or academic papers

## Status

This is an early but real starting point.

The next quality jump is not “more categories.” It is sharper boundaries, stronger scenario coverage, and better workflow composition between the skills that already exist.

## Open Source Basics

This repository now includes:

- [LICENSE](/Users/zhangjunmengyang/PycharmProjects/llm-superpowers/LICENSE)
- [CONTRIBUTING.md](/Users/zhangjunmengyang/PycharmProjects/llm-superpowers/CONTRIBUTING.md)
- [docs/installation.md](/Users/zhangjunmengyang/PycharmProjects/llm-superpowers/docs/installation.md)
