# Systems Debug Patterns

Use this file to structure debugging of LLM training or inference systems.

## Failure Classes

### OOM

Check:

- sequence length
- activation memory
- optimizer state sharding
- checkpointing
- precision mode

### Instability

Check:

- learning rate
- mixed precision settings
- gradient norm
- bad samples or corrupted batches
- loss scaling and kernel interactions

### Throughput Collapse

Check:

- dataloader bottlenecks
- kernel choice
- packing efficiency
- communication overhead
- microbatch sizing

### Distributed Bugs

Check:

- world size assumptions
- FSDP or ZeRO config mismatch
- checkpoint resharding behavior
- NCCL or communication setup

## Debug Rules

- reproduce first
- simplify second
- measure third
- scale fourth

## Failure Modes

- jumping to framework rewrites too early
- debugging at full scale only
- declaring a systems fix without checking model quality
- tuning around a bad recipe instead of exposing it
