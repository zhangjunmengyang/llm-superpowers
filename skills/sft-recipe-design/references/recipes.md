# SFT Recipes

Use this file to design strong supervised finetuning recipes.

## Common SFT Jobs

- instruction following bootstrap
- domain adaptation after CPT
- style and format alignment
- reasoning bootstrap before PRM or RL
- distillation from a stronger teacher

## Main Design Axes

### Format

- plain completion
- chat format
- assistant-only loss
- special-token conventions

### Finetuning Method

- full finetuning for maximal control
- LoRA when compute is limited
- QLoRA when memory is the real bottleneck

### Data Mixture

- keep high-signal core data separate from noisy bulk data
- upweight scarce but important behaviors deliberately
- avoid letting generic assistant data wash out the target behavior

### Sequence Strategy

- long sequence if the task genuinely needs it
- packing only when it does not distort supervision
- validate truncation behavior explicitly

## Public Baselines

- [huggingface/trl](https://github.com/huggingface/trl)
- [allenai/open-instruct](https://github.com/allenai/open-instruct)
- [pytorch/torchtune](https://github.com/pytorch/torchtune)
- [OpenAccess-AI-Collective/axolotl](https://github.com/OpenAccess-AI-Collective/axolotl)
- [hiyouga/LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)

## Failure Modes

- wrong chat template
- bad loss masking
- overmixed datasets with no target distribution
- eval contamination from synthetic generation
- using SFT to solve a problem that really needs preference optimization
