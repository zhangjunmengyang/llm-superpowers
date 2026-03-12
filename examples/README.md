# Examples

This directory is for users who want to start fast.

Each example shows:

- which program to start from
- when to use a lead skill
- a concrete starter prompt
- the expected output shape
- what artifact should come out

## Start Here

- [new-posttrain-plan.md](new-posttrain-plan.md)
  - for deciding the next post-training stage
- [synthetic-data-plan.md](synthetic-data-plan.md)
  - for SFT, preference, and trace dataset design
- [reasoning-improvement.md](reasoning-improvement.md)
  - for reasoning, PRM, verifier, and RL style work
- [regression-triage.md](regression-triage.md)
  - for baseline vs candidate comparison and release decisions
- [systems-bottleneck.md](systems-bottleneck.md)
  - for memory, throughput, and stability debugging
- [paper-to-recipe.md](paper-to-recipe.md)
  - for turning papers and public repos into runnable experiment plans

## How To Use These

1. Pick the example closest to your situation.
2. Open the matching program under `programs/`.
3. Copy the starter prompt into your coding-agent runtime.
4. Adjust the model, dataset, and target behavior.
5. Keep one lead skill and one artifact contract.

## Coverage

These examples cover the main operating loops in the repository, so a new user can reach the primary training work modes without guessing where to start.
