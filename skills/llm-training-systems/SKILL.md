---
name: llm-training-systems
description: Systems triage and measurement for OOMs, throughput collapse, instability, parallelism issues, and serving bottlenecks in LLM training work. Use when Codex needs to answer questions such as 'what should we measure first', 'which axis do we change next', 'why is this run invalid operationally', or turn a systems failure into a measured intervention plan with rollback and quality guards.
---

# LLM Training Systems

Use this skill when the problem is systems reality and the team needs a measured triage loop.

## Use This Skill First When

- the run is OOMing
- throughput is unexpectedly poor
- a recipe works at small scale but fails at larger scale
- training diverges and the likely cause is precision, checkpointing, or parallelism
- serving behavior or inference throughput is blocking evaluation

## Core Workflow

1. Identify the bottleneck class: memory, throughput, stability, communication, or serving.
2. Reproduce the issue with the smallest credible configuration.
3. Build a measurement board before changing knobs.
4. Change one axis at a time: precision, batch, sequence length, parallelism, attention kernel, checkpointing, optimizer sharding, or serving engine.
5. Keep a rollback-safe baseline while exploring.

## Required Output

When using this skill, produce:

- bottleneck class
- smallest reproduction
- measurement board
- prioritized interventions
- rollback point
- quality guard

## Hard Rules

- Do not call a problem algorithmic until systems bottlenecks are measured.
- Do not change model size, batch size, sequence length, and parallelism simultaneously.
- Favor the simplest stack that meets the target scale.
- Treat logging, profiling, and reproducibility as part of system design.
- Separate training optimizations from inference optimizations.
- Do not call a throughput win “real” until quality is rechecked.

## Do Not Lead With This Skill When

- the project still has not chosen a post-training recipe
- the main blocker is dataset schema or synthetic data quality
- the team lacks a credible evaluation loop
- the real question is what a paper is actually proposing

## References

- Read `references/systems.md` for board fields, stack selection, and triage checklists.
