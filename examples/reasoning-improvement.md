# Example: Reasoning Improvement

## When To Use

Use this pattern when the target is reasoning correctness, step quality, PRM design, verifier design, or R1-style improvement.

## Lead Skill

- `llm-reasoning-posttrain`

## Support Skills

- `reasoning-prm-verifier`
- `llm-eval-loop`

## Starter Prompt

```text
Use $llm-reasoning-posttrain to design the best reasoning-improvement path for this model.

Context:
- task family: <math / code / science / mixed reasoning>
- current baseline: <current model and observed failure pattern>
- available assets: <reasoning traces / verifier / reward model / none>
- constraints: <compute, turnaround time, need for inference efficiency>

Return:
- whether we should use step SFT, PRM, verifier ranking, best-of-n, or online RL
- the minimum trace schema
- how to supervise correctness
- how to evaluate reasoning gains
- what to avoid
```

## Expected Output

- reasoning recipe choice
- process-supervision plan
- trace schema
- verifier or reward definition
- evaluation plan

## Next Step

If the bottleneck is process supervision, hand off to `reasoning-prm-verifier`.

If the bottleneck is reasoning data generation, hand off to `llm-synthetic-data`.

If the bottleneck is rollout optimization, hand off to `online-rl-posttraining`.
