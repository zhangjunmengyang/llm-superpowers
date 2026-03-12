# Eval Benchmarks

Use this file to choose a lightweight but defensible evaluation stack.

## Core Public Tools

- [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)
- [open-compass/opencompass](https://github.com/open-compass/opencompass)
- [allenai/reward-bench](https://github.com/allenai/reward-bench)
- [tatsu-lab/alpaca_eval](https://github.com/tatsu-lab/alpaca_eval)
- [lm-sys/FastChat](https://github.com/lm-sys/FastChat)

## Minimum Credible Loop

1. fixed baseline and candidate
2. fixed prompt or benchmark set
3. documented decoding settings
4. task metric
5. safety or reward metric
6. manual review of sampled failures

## Judge Guidelines

- pairwise judges are stronger than one-shot scalar vibes
- use rubric-conditioned judging when possible
- do not trust a single judge model as final truth
- for reasoning, prefer exact match or verifier signals over style judges

## Decision Heuristics

- if reward rises and safety falls, hold
- if benchmark rises but latency or cost explodes, report the tradeoff
- if gains appear only on your own synthetic eval, treat them as provisional
