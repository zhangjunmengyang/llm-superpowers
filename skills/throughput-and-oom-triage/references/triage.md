# Throughput And OOM Triage

Use this file as the first-response checklist for operationally invalid runs.

## Minimum Board

- sequence length
- batch size
- tokens per second
- step time
- GPU utilization
- peak memory

## Symptom Signatures

| Symptom | Likely cause | First measurement | First safe move |
| --- | --- | --- | --- |
| step-0 OOM | model or optimizer footprint | init memory | lower microbatch, checkpoint, shard |
| late-step OOM | activations or long-example outliers | max active sequence | lower length, inspect packing |
| low util and low memory | input or host stalls | data wait or CPU bottleneck | fix loader, then raise effective batch |
| high util and low throughput | kernels or communication | step breakdown | better kernel, then better parallel layout |
| intermittent instability | precision, overflow, bad samples | grad norm and NaN origin | lower LR, verify precision, isolate samples |

## First Responses

### OOM

- reduce sequence length
- reduce activation footprint
- checkpoint
- shard optimizer state

### Low Throughput

- check dataloader stalls
- check kernel choice
- check microbatch sizing
- check communication overhead

### Low Utilization

- look for host stalls
- look for too-small batches
- look for uneven parallelism

## Stop Rules

- after three non-directional one-axis interventions, stop and reclassify the problem
- if the issue disappears only when quality comparability breaks, do not count it as fixed
- if the symptom is not reproducible on a smaller setup, record that before changing more knobs

## Anti-Patterns

- changing kernels and batch shape together
- debugging only at full scale
- accepting throughput gains without quality checks
