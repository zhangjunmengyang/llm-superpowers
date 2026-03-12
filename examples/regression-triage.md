# Example: Regression Triage

## When To Use

Use this pattern when a new checkpoint looks promising in demos but you do not yet know whether it should ship, scale, or be rolled back.

## Lead Skill

- `llm-eval-loop`

## Support Skills

- `eval-and-regression-gates`
- `llm-posttrain-pipeline`

## Starter Prompt

```text
Use $llm-eval-loop to compare this candidate checkpoint against the baseline and define whether we should ship, hold, or investigate.

Context:
- baseline: <checkpoint A>
- candidate: <checkpoint B>
- target improvements: <what was supposed to get better>
- known concerns: <safety / reasoning / latency / reward / style>
- available benchmarks: <current eval assets>

Return:
- minimum benchmark plan
- key metrics that should decide this comparison
- likely blind spots
- whether we need explicit regression gates
- recommended next action
```

## Expected Output

- benchmark plan
- comparison logic
- blind spots
- ship or hold recommendation

## Next Step

If the measurement is sound but signoff logic is vague, hand off to `eval-and-regression-gates`.

If the results imply the wrong recipe, hand off to `llm-posttrain-pipeline`.
