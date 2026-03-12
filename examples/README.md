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

## Worked Artifacts

These are filled examples, not starter prompts.

- [worked-experiment-card.md](worked-experiment-card.md)
  - a concrete experiment card with success and kill bars
- [worked-eval-board.md](worked-eval-board.md)
  - a candidate-vs-baseline board with a real hold decision
- [worked-results.tsv](worked-results.tsv)
  - a ledger row that matches the repository template
- [worked-systems-triage.md](worked-systems-triage.md)
  - a measured OOM recovery board
- [worked-reproduction-plan.md](worked-reproduction-plan.md)
  - a paper-to-experiment plan with irreducibles and kill criteria

## How To Use These

1. Pick the example closest to your situation.
2. Open the matching program under `programs/`.
3. Copy the starter prompt into your coding-agent runtime.
4. Adjust the model, dataset, and target behavior.
5. Keep one lead skill and one artifact contract.

If you want to see what good output should look like, start from the worked artifacts first and only then use the starter prompts.

## Coverage

These examples cover the main operating loops in the repository, so a new user can reach the primary training work modes without guessing where to start.
