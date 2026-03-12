# Examples

This directory is for users who want to start fast.

Each example shows:

- when to use a skill
- a concrete starter prompt
- the expected output shape
- which supporting skill to call next

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
2. Copy the starter prompt into your coding-agent runtime.
3. Adjust the model, dataset, and target behavior.
4. Keep one lead skill and at most one or two support skills.

## Coverage

These examples cover all six umbrella skills in the repository, so a new user can reach every primary work mode without guessing where to start.
