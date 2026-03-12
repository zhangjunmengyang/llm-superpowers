# Research To Experiment

Use this program when a paper or public repo is the starting point and the question is “what do we actually run next?”

## Required Artifact

Create or update:

- `runboard/reproduction-plan.md`

Start from:

- [templates/reproduction-plan.md](templates/reproduction-plan.md)

## Canonical Loop

1. Use `$llm-research-to-recipe`.
2. Extract:
   - claimed contribution
   - irreducible ingredients
   - scale-sensitive assumptions
   - evaluation standard
3. Split the result into:
   - faithful reproduction
   - cheaper approximation
   - first ablation queue
4. Define the first runnable experiment, not the whole research agenda.
5. Move into [experiment-loop.md](experiment-loop.md).

## Hard Rules

- code beats prose when they disagree
- do not copy hyperparameters across scales blindly
- do not call something “faithful” if data, reward, or eval changed materially
- always separate what is essential from what is merely in the paper

## Exit Condition

This program is complete only when another engineer could launch the first experiment without rereading the paper.
