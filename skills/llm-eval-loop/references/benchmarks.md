# Eval Boards And Benchmarks

Use this file to build the smallest credible evaluation board.

## Core Public Tools

- [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)
- [open-compass/opencompass](https://github.com/open-compass/opencompass)
- [allenai/reward-bench](https://github.com/allenai/reward-bench)
- [tatsu-lab/alpaca_eval](https://github.com/tatsu-lab/alpaca_eval)
- [lm-sys/FastChat](https://github.com/lm-sys/FastChat)

## Minimum Credible Board

1. fixed baseline and candidate
2. fixed prompts or benchmark set
3. documented decoding settings
4. one task metric that should move
5. one guardrail metric that should not regress
6. sampled qualitative failures

## Default Review Coverage

- review at least 20 worst failures overall
- review 5 to 10 failures for each critical slice
- if a critical slice has fewer examples than that, review all of them
- keep prompt, baseline output, candidate output, and judge note together for each reviewed failure

## Default Gate Template

- Hard blockers:
  - safety, refusal, policy, factuality, or any metric that can stop release on its own
- Watchlist:
  - latency, verbosity, style, cost, or softer quality drift
- Diagnostic-only:
  - probes that help explain movement but should not decide promotion alone

## Repeatability And Confidence

- if the delta sits inside the repeatability band, rerun or investigate instead of promoting
- if you do not yet know the repeatability band, use prior reruns, judge disagreement, or bootstrap estimates as the confidence note
- if judge disagreement on a core comparison is high, the board is not promotion-ready

## Judge Rules

- pairwise judges are stronger than scalar vibes
- use rubric-conditioned judging when possible
- do not trust a single judge model as final truth
- for reasoning, prefer exact match or verifier signals over style judges
- shuffle output order when pairwise judging to reduce positional bias
- note when a candidate and the judge come from the same family

## Decision Heuristics

- if reward rises and safety falls, hold
- if benchmark rises but latency or cost explodes, report the tradeoff explicitly
- if gains appear only on self-generated eval, treat them as provisional
- if the worst slice regresses materially, do not sign off from the mean
- if the candidate wins only on judge-heavy metrics, strengthen human or rubric-backed review before promotion
- if a hard blocker regresses, prefer hold or rollback over ship-plus-follow-up
- if the board has unresolved blind spots on the primary product slice, do not call the win final
