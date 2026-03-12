# Worked Artifact: Systems Triage

This is a filled example of the repository's systems-triage template.

# Systems Triage

**symptom:** step-0 OOM after increasing sequence length from 4k to 8k  
**last_known_good:** DPO training at 4k sequence length with the current stack  
**current_failing_setup:** same recipe and model, same hardware target, sequence length raised to 8k  

## Bottleneck Class

Activation-memory bottleneck, not a generic framework failure.

## Smallest Reproduction

- same model and stack
- one node
- same tokenizer and data packing rules
- sequence length 8k
- microbatch 1 still fails at step 0
- sequence length 4k passes cleanly

## Measurement Board

| Axis | Before | After | Notes |
| --- | --- | --- | --- |
| Sequence length | 8192 | 4096 | direct memory split confirmed |
| Peak memory | step-0 OOM | 54 GB | failure disappears immediately at 4k |
| Tokens per second | n/a | 18.4k | proof-of-life only |
| GPU utilization | n/a | 71 percent | enough for a credible small repro |

## Intervention Queue

1. Keep the recipe fixed and prove the issue is sequence-length-driven, not launch drift.
2. Add activation checkpointing and retry 8k before any framework migration.
3. If memory is still invalid, retune microbatch and effective batch while keeping the eval smoke set fixed.

## Rollback Point

Return to the 4k configuration that is already comparable and operationally valid.

## Quality Guard

How we know the systems fix did not corrupt the experiment:

- rerun the same refusal-calibration smoke set at 4k and after the first 8k fix
- compare answer length, refusal behavior, and the primary pairwise metric before counting the fix as real

## Stop Rule

When to stop turning knobs and reclassify the problem:

- if three one-axis interventions fail to make 8k operationally valid, stop and treat long-context scale as unrealistic for this recipe on the current stack
