# Research Extraction Template

Use this template when converting a paper or repo into an engineering recipe.

## Extract

- problem
- claimed contribution
- base model or environment
- data sources
- supervision type
- reward or verifier
- training stages
- inference-time tricks
- evaluation suite
- ablations that actually matter

## Cross-Check

- does the public repo implement the paper faithfully
- which pieces are missing
- which hyperparameters are scale-specific
- which datasets are unavailable or replaced

## Good Public Sources

- [huggingface/open-r1](https://github.com/huggingface/open-r1)
- [allenai/open-instruct](https://github.com/allenai/open-instruct)
- [huggingface/alignment-handbook](https://github.com/huggingface/alignment-handbook)
- [volcengine/verl](https://github.com/volcengine/verl)
- [OpenRLHF/OpenRLHF](https://github.com/OpenRLHF/OpenRLHF)
- [rllm-org/rllm](https://github.com/rllm-org/rllm)

## Output Contract

- faithful recipe
- cheaper recipe
- required data schema
- required evaluation
- open questions
