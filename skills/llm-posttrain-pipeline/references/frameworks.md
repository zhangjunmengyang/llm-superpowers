# Framework Map

Use this file to map an experiment idea to the smallest public stack that can run it.

## Core Frameworks

- [huggingface/trl](https://github.com/huggingface/trl)
- [OpenRLHF/OpenRLHF](https://github.com/OpenRLHF/OpenRLHF)
- [volcengine/verl](https://github.com/volcengine/verl)
- [huggingface/open-r1](https://github.com/huggingface/open-r1)
- [allenai/open-instruct](https://github.com/allenai/open-instruct)
- [huggingface/alignment-handbook](https://github.com/huggingface/alignment-handbook)
- [hiyouga/LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)
- [OpenAccess-AI-Collective/axolotl](https://github.com/OpenAccess-AI-Collective/axolotl)
- [pytorch/torchtune](https://github.com/pytorch/torchtune)
- [Lightning-AI/litgpt](https://github.com/Lightning-AI/litgpt)
- [mosaicml/llm-foundry](https://github.com/mosaicml/llm-foundry)

## First-Run Mapping

- choose `trl` for quick offline post-training iteration
- choose `verl` or `OpenRLHF` for distributed RL-heavy work
- choose `open-r1` for public reasoning-first baselines
- choose `open-instruct` when you want a readable post-training reference stack
- choose `LLaMA-Factory` or `axolotl` when speed and breadth matter more than conceptual purity
- choose `torchtune` or `litgpt` when readability and small-surface modification matter

## Rules

- prefer the smallest stack that can answer the experiment question
- map one first run to one framework
- do not build a new trainer before exhausting public baselines
- do not claim a framework choice without naming the exact runnable path
