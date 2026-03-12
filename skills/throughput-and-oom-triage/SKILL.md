---
name: throughput-and-oom-triage
description: Operational triage for OOMs, throughput collapse, utilization drops, and invalid training runs in LLM systems. Use when Codex needs to answer questions such as 'what should we measure first', 'which knob do we touch next', 'is this memory, throughput, or instability', or build a one-axis intervention plan with rollback and quality guards.
---

# Throughput And OOM Triage

Use this skill when the failure is operationally concrete and the team needs the next measured intervention, not a broad systems overview.

## Use This Skill First When

- the run OOMs
- throughput is far below expectation
- utilization is low and the bottleneck is unclear
- the run is operationally invalid and must be made comparable again

## Core Workflow

1. Classify the symptom: memory, throughput, utilization, or instability.
2. Record the current board: batch, sequence, tokens per second, step time, util, memory.
3. Choose one intervention axis only.
4. Re-run and compare before vs after.
5. Keep the fix only if the run remains quality-comparable.

## Intervention Axes

- sequence length
- batch size or microbatch
- checkpointing
- kernel choice
- sharding or parallelism
- dataloader behavior
- precision mode

## Hard Rules

- do not turn one triage run into a framework migration
- do not touch multiple axes in one measured step
- do not accept a systems fix that ruins quality comparability
- do not keep tuning without a rollback point

## Artifact Contract

When using this skill, produce:

- bottleneck class
- measurement board
- next one-axis intervention
- rollback point
- comparability guard

## References

- Read `references/triage.md` for board fields and first-response heuristics.
