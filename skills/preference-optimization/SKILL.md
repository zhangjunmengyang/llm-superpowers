---
name: preference-optimization
description: Preference optimization design for DPO, IPO, ORPO, KTO, SimPO, and related offline alignment methods. Use when Codex needs to answer questions such as 'should we use DPO or ORPO', 'are our chosen and rejected pairs good enough', 'do we need a reward model or is direct preference optimization enough', or design an offline preference-learning recipe after SFT.
---

# Preference Optimization

Use this skill when the problem is offline preference learning rather than broad stage selection or online RL.

## Use This Skill First When

- the team already has an SFT base and preference data
- the main question is which offline preference method to use
- chosen and rejected quality is central to the next improvement
- the project wants a simpler alternative to reward-model-plus-RL

## Core Workflow

1. Clarify the target behavior: helpfulness, harmlessness, style, reasoning quality, or task preference.
2. Audit the preference dataset for signal quality and ambiguity.
3. Choose the method family based on data quality, compute budget, and stability needs.
4. Set prompt and completion boundaries explicitly.
5. Define the baseline comparison: SFT vs preference-tuned candidate.
6. Decide whether direct preference optimization is enough or a reward model is still needed.

## Method Families

- DPO
- IPO
- ORPO
- KTO
- SimPO

## Operating Rules

- Pair quality matters more than method branding.
- Chosen and rejected examples must differ in a behavior you actually care about.
- Do not mix preference sources with incompatible rubrics without documenting the tradeoff.
- Treat prompt boundaries and truncation carefully; many preference bugs are formatting bugs.
- Compare against the SFT base, not just against another preference-tuned checkpoint.

## Do Not Lead With This Skill When

- the project still has not chosen whether SFT, preference optimization, reward modeling, or RL should come next
- the team lacks a credible SFT base
- the real need is reward-model design or online exploration
- the task is reasoning-specific verifier or PRM work

## Typical Hand-Offs

- to `llm-posttrain-pipeline` when stage choice is still open
- to `data-curation-and-filtering` for pair curation and rubric cleanup
- to `reward-modeling` when direct preference optimization is not enough
- to `llm-eval-loop` for baseline-vs-candidate comparison

## Output Shape

When using this skill, produce:

- target preference behavior
- chosen method and why
- pair quality requirements
- formatting assumptions
- baseline comparison plan
- failure risks

## References

- Read `references/methods.md` for method selection heuristics and data-quality rules.
