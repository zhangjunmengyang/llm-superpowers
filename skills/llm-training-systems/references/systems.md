# Training Systems

Use this file to choose the right systems stack and debug path.

## Core Building Blocks

- [deepspeedai/DeepSpeed](https://github.com/deepspeedai/DeepSpeed)
- [pytorch/pytorch](https://github.com/pytorch/pytorch)
- [NVIDIA/Megatron-LM](https://github.com/NVIDIA/Megatron-LM)
- [pytorch/torchtitan](https://github.com/pytorch/torchtitan)
- [Dao-AILab/flash-attention](https://github.com/Dao-AILab/flash-attention)
- [vllm-project/vllm](https://github.com/vllm-project/vllm)
- [sgl-project/sglang](https://github.com/sgl-project/sglang)
- [AnswerDotAI/fsdp_qlora](https://github.com/AnswerDotAI/fsdp_qlora)

## Bottleneck Map

### OOM

Try:

- lower sequence length
- QLoRA or lower precision
- gradient checkpointing
- ZeRO or FSDP
- activation offload

### Low Throughput

Try:

- FlashAttention
- larger effective batch
- fused kernels
- dataloader cleanup
- better parallelism layout

### Instability

Try:

- reduce learning rate
- inspect gradient norms
- check mixed precision settings
- verify loss scaling and NaN sources
- isolate bad samples

### Serving Bottleneck

Try:

- vLLM or SGLang
- continuous batching
- KV cache tuning
- tensor parallelism only if needed

## Decision Heuristics

- use DeepSpeed when ZeRO and optimizer sharding dominate
- use FSDP when you want more native PyTorch control
- use Megatron or TorchTitan for larger-scale pretraining patterns
- use vLLM or SGLang for serious serving work instead of a raw transformers loop
