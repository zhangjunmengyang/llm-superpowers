# Example: New Post-Training Plan

## When To Use

Use this pattern when you have a model and a target behavior, but you have not yet decided whether to run SFT, preference optimization, reward modeling, or online RL.

## Lead Skill

- `llm-posttrain-pipeline`

## Support Skills

- `llm-synthetic-data`
- `llm-eval-loop`

## Starter Prompt

```text
Use $llm-posttrain-pipeline to decide the next post-training stage for this model.

Context:
- base model: <model-name>
- target behavior: <what should improve>
- current assets: <SFT data / preference data / reward data / checkpoints>
- constraints: <compute, latency, timeline>

Return:
- recommended next stage
- why this stage is better than the nearest alternatives
- best open-source framework to start from
- minimum dataset schema
- minimum eval plan
- likely failure risks
```

## Expected Output

- stage choice
- algorithm choice
- framework recommendation
- dataset schema
- evaluation requirements
- scale-up notes

## Next Step

If the answer chooses SFT, hand off to `sft-recipe-design`.

If the answer chooses DPO or another offline preference method, hand off to `preference-optimization`.

If the answer chooses reward-plus-RL, hand off to `reward-modeling` or `online-rl-posttraining`.
