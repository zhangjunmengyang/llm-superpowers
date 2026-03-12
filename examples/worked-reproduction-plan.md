# Worked Artifact: Reproduction Plan

This is a filled example of the repository's reproduction-plan template.

# Reproduction Plan

**source:** public reasoning-paper and repo with an R1-style recipe  
**claimed_contribution:** improved reasoning through a combination of trace-rich data, verifier-backed filtering, and rollout optimization  

## Irreducible Ingredients

- data:
  - reasoning tasks with step-rich traces, not only final answers
- objective:
  - a supervised or preference stage that teaches the target reasoning format
- reward or verifier:
  - a signal that can distinguish correct from incorrect reasoning paths
- inference-time tricks:
  - candidate sampling plus filtering or reranking
- evaluation:
  - exact-answer or verifier-backed reasoning benchmarks, not style judges alone

## Faithful Reproduction

- keep the reasoning-task mix close to the source recipe
- keep verifier-backed filtering in the loop
- keep the evaluation family aligned with the paper's reasoning claims
- preserve the order of stages: base supervised recipe before rollout optimization

## Cheaper Approximation

- skip online RL at first
- run step-aware SFT plus verifier-filtered best-of-n
- use a smaller reasoning slice to check whether the claimed gains survive outside the source examples

## Scale-Sensitive Assumptions

- the number of sampled candidates at inference time may matter as much as the training objective
- verifier quality can matter more than policy size
- rollout improvements may not appear until the base supervised recipe is already strong

## First Ablation Queue

1. SFT only on the reasoning format
2. SFT plus verifier-filtered best-of-n
3. add rollout optimization only if the cheaper approximation still leaves a clear gap

## First Runnable Experiment

- baseline:
  - existing supervised checkpoint
- change surface:
  - add verifier-filtered best-of-n on a held-out reasoning slice
- success bar:
  - exact-answer gain above the repeatability band with no major regression on non-reasoning smoke checks

## Kill Criteria

What would make us stop reproducing this direction:

- the verifier cannot rank good and bad traces reliably in a small audit
- best-of-n already saturates the available gain
- rollout optimization improves only the paper's own distribution and not the external reasoning board
