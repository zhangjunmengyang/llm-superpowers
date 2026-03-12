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

## What Changes In Practice

`superpowers` changes coding by making the agent follow a tighter development loop.

`llm-superpowers` is trying to do the analogous thing for training work:

- experiment card before scale-up
- eval board before promotion
- keep or discard after every serious run
- smallest reproduction before systems tuning

If the repository does not materially change behavior in the scenarios below, it still needs iteration.

### Scenario 1: Starting An SFT Run

Without `llm-superpowers`, a strong agent will often produce a reasonable recipe, but it tends to stay generic:

- data, template, and finetuning method may change together
- there may be no smallest meaningful delta
- there may be no kill condition or rollback point
- the result is advice, not an experiment artifact

With `llm-superpowers`, the expected path is:

- start from [programs/experiment-loop.md](programs/experiment-loop.md)
- use `$llm-posttrain-pipeline`
- write one experiment card with one change surface
- define the smoke set, success bar, and kill bar before the run
- log a keep, discard, crash, or investigate decision after the run

### Scenario 2: A DPO Candidate Looks Better In Demos But Feels Wrong

Without `llm-superpowers`, the common failure mode is:

- chase the global mean
- hand-wave the worst slice
- blame “the algorithm” too early
- propose three next experiments instead of one isolating run

With `llm-superpowers`, the expected path is:

- start from [programs/eval-board.md](programs/eval-board.md)
- use `$llm-eval-loop`
- review the worst failures first, not the best wins
- use `$checkpoint-regression-triage` to cluster the failures
- produce one next-run proposal grounded in a failure cluster

### Scenario 3: The Run OOMs Or Throughput Collapses

Without `llm-superpowers`, agents often:

- change sequence length, batch, kernels, and framework together
- debug only at full scale
- call a throughput win “real” without a quality recheck
- lose comparability with the baseline

With `llm-superpowers`, the expected path is:

- start from [programs/systems-war-room.md](programs/systems-war-room.md)
- use `$llm-training-systems`
- build the smallest credible reproduction
- change one axis only
- use `$throughput-and-oom-triage` plus a quality smoke set before accepting the fix

### Scenario 4: Reproducing A Paper Or Public Repo

Without `llm-superpowers`, the common pattern is:

- copy the paper stack too literally
- inherit scale assumptions blindly
- spend too much compute before the core claim is tested
- discover late that the paper's gains depended on ingredients you did not preserve

With `llm-superpowers`, the expected path is:

- start from [programs/research-to-experiment.md](programs/research-to-experiment.md)
- use `$llm-research-to-recipe`
- separate irreducibles from paper-specific details
- write a cheaper approximation before a faithful large-scale reproduction
- define kill criteria before the reproduction becomes a long-running project

The repository is strongest when it turns a capable agent from “helpful and plausible” into “disciplined and comparable.”

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
