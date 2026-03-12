# Reasoning Recipes

Use this file when the user asks for PRM, verifiers, reasoning RL, or R1-style post-training.

## Canonical Ladder

### 1. Step SFT

Use when the model must emit structured intermediate reasoning.

### 2. Process Supervision

Use when intermediate steps can be labeled or checked.

Variants:

- process reward model
- step verifier
- boundary-level labels

### 3. Candidate Search

Use when the model can generate multiple traces and a verifier can rank them.

Variants:

- best-of-n
- rejection sampling
- self-consistency
- tree or search-based selection

### 4. Reasoning RL

Use when trajectory-level rewards are reliable enough to justify online optimization.

Variants:

- PPO
- RLOO
- GRPO
- custom search or environment-based RL

### 5. Distillation

Use when the stronger search or RL policy is too expensive for deployment.

## Strong Public Baselines

- [huggingface/open-r1](https://github.com/huggingface/open-r1)
- [volcengine/verl](https://github.com/volcengine/verl)
- [open-thoughts/open-thoughts](https://github.com/open-thoughts/open-thoughts)
- [rllm-org/rllm](https://github.com/rllm-org/rllm)
- [Agent-One-Lab/AgentFly](https://github.com/Agent-One-Lab/AgentFly)

## Selection Heuristics

- use step SFT when the model lacks decomposition
- use PRM or verifiers when correctness can be checked per step
- use best-of-n when search is cheaper than RL
- use RL when exploration matters and reward is trustworthy
- distill after search or RL if inference cost matters

## Common Failure Modes

- rewarding verbosity instead of correctness
- missing or inconsistent step boundaries
- noisy synthetic labels treated as ground truth
- verifier leakage from answer string instead of reasoning quality
- no final distillation after expensive search-time improvements
