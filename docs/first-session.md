# First Session Guide

This document is for the first ten minutes after installation.

The objective is not to explore every skill. The objective is to produce one real artifact that can move training work forward.

## Step 1: Pick One Program

Choose the closest starting point:

- use `programs/experiment-loop.md` when you are planning or running the next experiment
- use `programs/eval-board.md` when you already have a candidate and need a promotion decision
- use `programs/systems-war-room.md` when the run is operationally invalid
- use `programs/research-to-experiment.md` when the starting point is a paper or public repo

Then pick one lead skill for that program.

## Step 2: Provide The Minimum Context

A first session becomes much better if you provide:

- model or checkpoint name
- named baseline
- target behavior that should improve
- current assets such as SFT data, preference data, reward labels, traces, or benchmarks
- constraints such as compute, latency, timeline, and serving limits
- current failure mode or uncertainty

## Step 3: Ask For A Structured Return

Do not ask for “thoughts.”

Ask for one of these artifacts:

- experiment card
- eval board
- systems triage board
- reproduction plan
- ledger row plus keep or discard decision

## Default Session Template

```text
Program:
- <experiment-loop | eval-board | systems-war-room | research-to-experiment>

Use $<lead-skill> to produce the next artifact for this program.

Context:
- model or checkpoint: <name>
- baseline: <named baseline>
- target behavior: <what should improve>
- current assets: <datasets, labels, traces, checkpoints, benchmarks>
- constraints: <compute, latency, timeline>
- main uncertainty: <what is unclear right now>

Return:
- artifact type: <experiment card | eval board | triage board | reproduction plan | ledger row>
- explicit decision
- hard blockers
- rollback point
- next question
```

## Good First Sessions

- choose SFT vs DPO vs reward-plus-RL for a new domain
- decide whether a reasoning problem needs traces, PRM, verifier ranking, or online RL
- compare a candidate checkpoint against a baseline with explicit ship or hold gates
- decide whether a paper should be reproduced faithfully or approximated cheaply

## Bad First Sessions

- asking for a full training stack without any model, data, or constraints
- invoking four or five skills at once
- asking for benchmark conclusions without a named baseline
- treating a systems slowdown as purely an algorithm problem

## Fastest Path

If you want the fastest useful path, start with one of these:

- [../examples/new-posttrain-plan.md](../examples/new-posttrain-plan.md)
- [../examples/synthetic-data-plan.md](../examples/synthetic-data-plan.md)
- [../examples/reasoning-improvement.md](../examples/reasoning-improvement.md)
- [../examples/regression-triage.md](../examples/regression-triage.md)
- [../examples/systems-bottleneck.md](../examples/systems-bottleneck.md)
- [../examples/paper-to-recipe.md](../examples/paper-to-recipe.md)
