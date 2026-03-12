# Example: Synthetic Data Plan

## When To Use

Use this pattern when the algorithm stage is mostly decided, but the bottleneck is the training data itself: coverage, schema, filtering, preference construction, or trace quality.

## Lead Skill

- `llm-synthetic-data`

## Support Skills

- `data-curation-and-filtering`
- `sft-recipe-design`

## Starter Prompt

```text
Use $llm-synthetic-data to design the best training-data plan for this model update.

Context:
- task family: <general assistant / coding / math / domain-specific>
- training objective: <SFT / preference optimization / reward model / reasoning traces>
- current source material: <raw corpus, prompts, demos, pairwise labels, traces>
- known data problems: <coverage gaps, label noise, verbosity bias, contamination risk>
- constraints: <data budget, labeling budget, turnaround time>

Return:
- recommended dataset type and schema
- generation or collection path
- filtering and curation rules
- minimum quality checks
- what should not be synthesized
```

## Expected Output

- dataset objective
- schema
- generation path
- filtering policy
- quality checks
- escalation risk

## Next Step

If the dataset is primarily for SFT, hand off to `sft-recipe-design`.

If the main issue is filtering, deduplication, or data quality, hand off to `data-curation-and-filtering`.

If the dataset needs reasoning traces or verifier signals, hand off to `llm-reasoning-posttrain`.
