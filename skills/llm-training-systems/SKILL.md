---
name: llm-training-systems
description: Distributed training, inference, and systems optimization for LLM development. Use when Codex needs to diagnose OOMs, unstable loss, slow throughput, broken parallelism, checkpointing issues, attention kernel problems, FSDP or DeepSpeed tradeoffs, or serving bottlenecks across training and inference stacks such as PyTorch, DeepSpeed, FSDP, Megatron, vLLM, and SGLang.
---

# LLM Training Systems

Use this skill when the problem is systems reality rather than algorithm theory.

## Core Workflow

1. Identify the bottleneck class: memory, throughput, stability, communication, or serving.
2. Reproduce the issue with the smallest credible configuration.
3. Measure before changing multiple knobs.
4. Change one axis at a time: precision, batch, sequence length, parallelism, attention kernel, checkpointing, optimizer sharding, or serving engine.
5. Keep a working baseline while exploring aggressive optimizations.

## Operating Rules

- Do not call a problem algorithmic until systems bottlenecks are measured.
- Do not change model size, batch size, sequence length, and parallelism simultaneously.
- Favor the simplest stack that meets the target scale.
- Treat logging, profiling, and reproducibility as part of system design.
- Separate training optimizations from inference optimizations.

## Output Shape

When using this skill, produce:

- bottleneck hypothesis
- measurement plan
- prioritized interventions
- rollback point
- validation criteria

## References

- Read `references/systems.md` for stack selection and debug checklists.
