# Training Systems Triage

Use this file to structure the measurement board before you touch knobs.

## Core Building Blocks

- [deepspeedai/DeepSpeed](https://github.com/deepspeedai/DeepSpeed)
- [pytorch/pytorch](https://github.com/pytorch/pytorch)
- [NVIDIA/Megatron-LM](https://github.com/NVIDIA/Megatron-LM)
- [pytorch/torchtitan](https://github.com/pytorch/torchtitan)
- [Dao-AILab/flash-attention](https://github.com/Dao-AILab/flash-attention)
- [vllm-project/vllm](https://github.com/vllm-project/vllm)
- [sgl-project/sglang](https://github.com/sgl-project/sglang)
- [AnswerDotAI/fsdp_qlora](https://github.com/AnswerDotAI/fsdp_qlora)

## Minimum Measurement Board

Record:

- batch size
- sequence length
- tokens per second
- step time
- GPU utilization
- peak memory
- compile or data wait if visible
- quality check after the intervention

## Failure Signatures

| Symptom | Likely cause | First thing to measure | First safe intervention |
| --- | --- | --- | --- |
| OOM at step 0 | optimizer state, sharding, launch config, model too large for the stack | memory at init and optimizer allocation | lower microbatch, add checkpointing, then shard |
| OOM after a few steps | activation growth, long-example outliers, packing issues, leaks | max sequence length and activation footprint | cap length, inspect packing, enable checkpointing |
| Low utilization and low memory | underbatching, dataloader stalls, host-device gaps | data wait, CPU load, batch formation | clean the loader, raise effective batch if comparable |
| High utilization but low tokens per second | kernel choice, communication, bad parallel layout | step breakdown and communication time | better kernel, then better parallel layout |
| Stable at small scale, unstable at large scale | effective batch change, precision, sharding interaction | grad norm, overflow, loss-scale behavior | lower LR, verify precision settings, reduce batch |
| Quality dropped after a systems fix | comparability broken by a changed recipe surface | same smoke set before vs after | revert or isolate the systems fix |

## Bottleneck Map

### OOM

First levers:

- lower sequence length
- lower activation footprint
- checkpointing
- ZeRO or FSDP
- lower-precision or QLoRA-style paths

### Low Throughput

First levers:

- FlashAttention or kernel choice
- larger effective batch if utilization is low
- dataloader cleanup
- better parallelism layout
- remove needless host-device stalls

### Instability

First levers:

- reduce learning rate
- inspect gradient norms
- verify mixed precision settings
- check loss scaling and NaN origin
- isolate bad samples

### Serving Bottleneck

First levers:

- vLLM or SGLang
- continuous batching
- KV cache tuning
- only then tensor parallelism if needed

## Stop Rules

- if three one-axis interventions fail to move the board, reclassify the problem before trying more knobs
- if the smallest reproduction is still unstable, stop scaling work and fix the minimal case first
- if a systems fix changes quality on the smoke set, do not call it a systems-only win
- if you are about to switch frameworks without a measured local bottleneck, stop and justify the migration first

## Decision Heuristics

- use DeepSpeed when ZeRO and optimizer sharding dominate
- use FSDP when you want native PyTorch control
- use Megatron or TorchTitan for larger-scale pretraining patterns
- use vLLM or SGLang for serious serving instead of a raw transformers loop
