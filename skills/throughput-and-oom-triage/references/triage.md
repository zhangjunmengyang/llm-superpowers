# Throughput And OOM Triage

Use this file as the first-response checklist for operationally invalid runs.

## Minimum Board

- sequence length
- batch size
- tokens per second
- step time
- GPU utilization
- peak memory

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

## Anti-Patterns

- changing kernels and batch shape together
- debugging only at full scale
- accepting throughput gains without quality checks
