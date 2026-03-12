# Work Scenarios

This document maps common LLM algorithm-engineering situations to the right lead skill.

## Scenario Matrix

| Scenario | Lead skill | Support skills | Expected output |
| --- | --- | --- | --- |
| New domain adaptation plan | `llm-posttrain-pipeline` | `sft-recipe-design`, `llm-eval-loop` | stage choice, recipe, metrics |
| DPO or RL decision for an existing model | `llm-posttrain-pipeline` | `preference-optimization`, `reward-modeling`, `online-rl-posttraining` | algorithm choice and scale-up path |
| Building a preference dataset | `llm-synthetic-data` | `data-curation-and-filtering`, `preference-optimization` | schema, generation path, filters |
| Building reasoning traces or PRM labels | `llm-reasoning-posttrain` | `reasoning-prm-verifier`, `llm-synthetic-data`, `llm-eval-loop` | trace schema, reward or verifier plan |
| Reproducing an R1-style or reasoning paper | `llm-research-to-recipe` | `llm-reasoning-posttrain`, `reasoning-prm-verifier`, `llm-posttrain-pipeline` | faithful recipe and cheaper approximation |
| Comparing several checkpoints | `llm-eval-loop` | `llm-posttrain-pipeline` | benchmark plan, pass or fail criteria |
| Safety regression after alignment | `llm-eval-loop` | `llm-posttrain-pipeline`, `preference-optimization`, `reward-modeling` | regression diagnosis and next experiment |
| OOM, divergence, or throughput collapse | `llm-training-systems` | `llm-eval-loop` | bottleneck hypothesis and fix sequence |
| Scaling a proof-of-life experiment | `llm-training-systems` | `llm-posttrain-pipeline`, `sft-recipe-design` or `online-rl-posttraining` | systems plan and rollback-safe scaling path |
| Turning a new paper into an internal experiment | `llm-research-to-recipe` | `llm-posttrain-pipeline`, one specialist module, `llm-eval-loop` | runnable recipe and validation plan |

## Scenario Notes

### 1. Choosing The First Recipe

Use `llm-posttrain-pipeline` first when the problem is still at the strategy layer.

Typical asks:

- should we start with SFT or DPO
- do we need a reward model
- is rejection sampling enough
- should we use TRL, veRL, or OpenRLHF

### 2. Fixing Data

Use `llm-synthetic-data` first when the bottleneck is clearly data quality, schema mismatch, negative sample quality, or reasoning-label quality.

Typical asks:

- how do we build high-quality DPO pairs
- what should the reward-model dataset look like
- how should we structure synthetic reasoning traces

Then bring in:

- `data-curation-and-filtering` when the hard part is filtering, dedup, or contamination
- `preference-optimization` when pair quality becomes the main question

### 3. Improving Reasoning

Use `llm-reasoning-posttrain` first when the target is reasoning correctness, step quality, verifier design, or R1-style improvement.

Typical asks:

- do we need PRM or verifier supervision
- should we use best-of-n or RL
- what does the reasoning trace schema need to look like

Then bring in:

- `reasoning-prm-verifier` for PRM vs verifier decisions
- `online-rl-posttraining` when the reasoning loop crosses into rollouts

### 4. Deciding If A Change Worked

Use `llm-eval-loop` first when the repository already has candidate outputs or checkpoints and the main problem is evidence.

Typical asks:

- which benchmark should we trust
- how should we compare baseline vs candidate
- what are the ship gates

### 5. Diagnosing Systems Problems

Use `llm-training-systems` first when the main blocker is memory, speed, instability, or serving behavior.

Typical asks:

- why are we OOMing
- why did throughput drop
- why does this run diverge only at scale
- should we switch to FSDP, ZeRO, vLLM, or SGLang

### 6. Reading Research Pragmatically

Use `llm-research-to-recipe` first when the main problem is turning research into an experiment plan.

Typical asks:

- what is the real contribution here
- what is required for a faithful reproduction
- what is the cheaper approximation we can run this week

Then hand off to:

- `sft-recipe-design`
- `preference-optimization`
- `reward-modeling`
- `online-rl-posttraining`
- `reasoning-prm-verifier`

depending on what the extracted recipe actually contains.
