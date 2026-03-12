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

## Judge Rules

- pairwise judges are stronger than scalar vibes
- use rubric-conditioned judging when possible
- do not trust a single judge model as final truth
- for reasoning, prefer exact match or verifier signals over style judges

## Decision Heuristics

- if reward rises and safety falls, hold
- if benchmark rises but latency or cost explodes, report the tradeoff explicitly
- if gains appear only on self-generated eval, treat them as provisional
- if the worst slice regresses materially, do not sign off from the mean
