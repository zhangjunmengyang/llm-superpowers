---
name: data-curation-and-filtering
description: Training-data curation, filtering, deduplication, contamination control, and mixture-quality design for LLM post-training. Use when Codex needs to answer questions such as 'which data should we keep', 'how should we score and filter examples', 'how do we avoid leakage and duplicate sludge', or design a high-signal dataset before SFT, preference optimization, reward modeling, or reasoning work.
---

# Data Curation And Filtering

Use this skill when the main bottleneck is training-data quality control.

## Use This Skill First When

- the dataset exists but its quality is suspect
- duplicate, low-signal, or leaked examples are likely hurting training
- the team needs a filtering rubric before generation or training
- data-mixture decisions matter more than model changes

## Core Workflow

1. Clarify the target behavior and target distribution.
2. Identify obvious failure modes: duplicates, leakage, low-signal noise, label conflicts, and format corruption.
3. Define scoring and filtering rules.
4. Decide what to discard, what to downweight, and what to review manually.
5. Build the final mixture with documented provenance.
6. Keep held-out eval and contamination checks separate from training curation.

## Main Jobs

- deduplication
- contamination control
- rubric-based filtering
- label conflict detection
- data-mixture balancing
- review queue design

## Operating Rules

- Filtering is part of the recipe, not cleanup after the fact.
- Preserve provenance whenever possible.
- Do not let generic bulk data swamp scarce but critical target behaviors.
- Keep train and eval sources separated aggressively.
- If the data is weak, adding more algorithms usually makes the problem harder, not better.

## Do Not Lead With This Skill When

- the dataset does not exist yet and the main problem is generation design
- the team still has not chosen the training stage
- the main blocker is online rollout infrastructure or reward design
- the issue is clearly systems throughput rather than data quality

## Typical Hand-Offs

- to `llm-synthetic-data` for new data generation
- to `sft-recipe-design` for SFT mixture planning
- to `preference-optimization` for pair-quality cleanup
- to `llm-eval-loop` for contamination-aware validation

## Output Shape

When using this skill, produce:

- target distribution
- filtering rubric
- dedup and leakage policy
- mixture decision
- review queue
- validation risks

## References

- Read `references/filters.md` for filtering policies and common failure modes.
