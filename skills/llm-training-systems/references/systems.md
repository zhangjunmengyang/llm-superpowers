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

## Decision Heuristics

- use DeepSpeed when ZeRO and optimizer sharding dominate
- use FSDP when you want native PyTorch control
- use Megatron or TorchTitan for larger-scale pretraining patterns
- use vLLM or SGLang for serious serving instead of a raw transformers loop
