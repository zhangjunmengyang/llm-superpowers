# Systems War Room

Use this program when the experiment loop is blocked by systems behavior instead of algorithm choice.

## Required Artifact

Create or update:

- `runboard/systems-triage.md`

Start from:

- [templates/systems-triage.md](templates/systems-triage.md)

## Before You Start

Freeze these first:

- baseline recipe or checkpoint
- hardware target
- current failing symptom
- last known good configuration

## Canonical Loop

1. Use `$llm-training-systems` to classify the bottleneck.
2. Reproduce the issue on the smallest credible setup.
3. Build a measurement board before changing knobs.
4. Change one axis only.
5. Re-measure.
6. Use `$throughput-and-oom-triage` if the issue is operationally concrete.
7. Use `$llm-eval-loop` before declaring a systems fix successful if quality could have shifted.
8. Reclassify the problem if three one-axis interventions fail to move the board.

## Minimum Board Metrics

- batch size
- sequence length
- tokens per second
- step time
- GPU utilization
- peak memory
- communication overhead if distributed
- quality check after the fix

## Hard Rules

- no multi-knob guessing
- no full-scale debugging before small-scale reproduction
- no “throughput win” without confirming quality did not drift
- no switching frameworks until simpler measurements fail
- no blaming the algorithm before the system is measured
- no endless knob turning without a stop rule

## Exit Conditions

The war room ends only when one of these is true:

- the issue is fixed and the fix is measured
- the issue is reclassified as recipe or data, not systems
- the system pain proves the original recipe is unrealistic
