# Eval Board

This is the canonical review board for deciding whether a run is real, ready, or regressing.

Use it after a candidate run exists.

## Required Artifact

Create or update:

- `runboard/eval-board.md`

Start from:

- [templates/eval-board.md](templates/eval-board.md)

## Board Sections

The board should have five sections only:

- headline metrics
- hard blockers
- watchlist metrics
- failure slices
- final decision

## Review Procedure

1. Use `$llm-eval-loop` to define the measurement stack.
2. Freeze baseline, candidate, prompts, and decoding settings.
3. Split metrics into:
   - hard blockers
   - watchlist
   - diagnostic-only
4. Use `$checkpoint-regression-triage` on the worst slices and sampled failures.
5. Record the final board decision:
   - ship
   - hold
   - investigate
   - rollback

## Minimum Required Slices

Every serious board should include:

- target task performance
- one safety or refusal slice if relevant
- one reasoning or correctness slice if relevant
- latency or throughput if deployment matters
- qualitative worst-case review

## Hard Rules

- do not gate on metrics whose movement you cannot interpret
- do not compare candidates under different decoding settings without saying so
- do not trust a single judge model as final truth
- do not sign off from averages only
- do not hide bad slices behind a better global mean

## Output

A complete board must end with:

- what improved
- what regressed
- what is still uncertain
- what blocks promotion
- what the next action is
