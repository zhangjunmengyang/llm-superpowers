# Example: Paper To Recipe

## When To Use

Use this pattern when a paper or public repo looks promising, but the real question is what the minimum faithful reproduction is and what the cheaper engineering approximation should be.

## Lead Skill

- `llm-research-to-recipe`

## Support Skills

- `llm-posttrain-pipeline`
- `llm-training-systems`

## Starter Prompt

```text
Use $llm-research-to-recipe to turn this paper or repository into a runnable engineering plan.

Context:
- source: <paper title / arXiv link / GitHub repo>
- target capability: <what we want to reproduce or borrow>
- available hardware: <compute and serving limits>
- acceptable approximation: <how far we can simplify>
- current stack: <frameworks and infra we already trust>

Return:
- minimum faithful recipe
- irreducible components we cannot skip
- cheapest useful approximation
- evaluation plan for deciding whether reproduction worked
- major implementation traps
```

## Expected Output

- faithful recipe
- approximation plan
- non-negotiable components
- evaluation plan
- implementation risks

## Next Step

If the recipe is sound and needs stage selection, hand off to `llm-posttrain-pipeline`.

If the paper is blocked by systems mismatch, hand off to `llm-training-systems`.
