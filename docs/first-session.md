# First Session Guide

This document is for the first ten minutes after installation.

The objective is not to explore every skill. The objective is to get one useful answer with the right lead skill and a clear output contract.

## Step 1: Pick One Work Mode

Choose the closest starting point:

- use `llm-posttrain-pipeline` when you need to decide the next training stage
- use `llm-synthetic-data` when data quality or schema is the bottleneck
- use `llm-reasoning-posttrain` when the target is reasoning correctness
- use `llm-eval-loop` when you need to compare checkpoints
- use `llm-training-systems` when runs are unstable, slow, or memory-bound
- use `llm-research-to-recipe` when you need to turn a paper or repo into a runnable plan

If two skills both seem plausible, start with the broader umbrella and let it hand off.

## Step 2: Provide The Minimum Context

A first session becomes much better if you provide:

- model or checkpoint name
- target behavior that should improve
- current assets such as SFT data, preference data, reward labels, traces, or benchmarks
- constraints such as compute, latency, timeline, and serving limits
- current failure mode or uncertainty

## Step 3: Ask For A Structured Return

Do not ask for “thoughts.”

Ask for a decision artifact. A good first-session return usually includes:

- recommendation
- nearest alternatives and why they lost
- minimum viable recipe
- minimum viable evaluation plan
- likely failure risks
- next hand-off skill if needed

## Default Session Template

```text
Use $<lead-skill> to help with this training decision.

Context:
- model or checkpoint: <name>
- target behavior: <what should improve>
- current assets: <datasets, labels, traces, checkpoints, benchmarks>
- constraints: <compute, latency, timeline>
- main uncertainty: <what is unclear right now>

Return:
- best next move
- why it beats the nearest alternatives
- minimum recipe to try first
- minimum eval plan
- main risks
- next skill to call if the task needs to go deeper
```

## Good First Sessions

- choose SFT vs DPO vs reward-plus-RL for a new domain
- decide whether a reasoning problem needs traces, PRM, verifier ranking, or online RL
- compare a candidate checkpoint against a baseline with explicit ship or hold gates
- decide whether a paper should be reproduced faithfully or approximated cheaply

## Bad First Sessions

- asking for a full training stack without any model, data, or constraints
- invoking four or five skills at once
- asking for benchmarking before defining the target behavior
- treating a systems slowdown as purely an algorithm problem

## Fastest Path

If you want the fastest useful path, start with one of these:

- [../examples/new-posttrain-plan.md](../examples/new-posttrain-plan.md)
- [../examples/synthetic-data-plan.md](../examples/synthetic-data-plan.md)
- [../examples/reasoning-improvement.md](../examples/reasoning-improvement.md)
- [../examples/regression-triage.md](../examples/regression-triage.md)
- [../examples/systems-bottleneck.md](../examples/systems-bottleneck.md)
- [../examples/paper-to-recipe.md](../examples/paper-to-recipe.md)
