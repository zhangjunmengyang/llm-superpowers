# Framework Map

Use this file to choose a public codebase or framework. Favor mature open-source baselines over custom reinvention.

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

## Selection Heuristics

- choose `trl` for fast algorithm iteration
- choose `verl` or `OpenRLHF` for distributed RL-heavy work
- choose `open-r1` for reasoning-first public baselines
- choose `LLaMA-Factory` or `axolotl` when breadth and speed matter more than purity
- choose `torchtune` or `litgpt` when readability and teaching value matter

## Avoid

- building a new trainer before exhausting public baselines
- claiming framework support without a runnable recipe
- mixing multiple frameworks in one first-pass experiment
