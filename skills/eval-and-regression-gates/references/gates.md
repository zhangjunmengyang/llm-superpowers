# Evaluation Gates

Use this file to turn measurements into decisions.

## Gate Categories

### Must-Pass

Metrics that block a release or scale-up.

Examples:

- severe safety regressions
- major reasoning correctness drop
- unacceptable latency explosion
- reward collapse relative to baseline

### Watchlist

Metrics that should be monitored but should not automatically block.

Examples:

- minor prompt-style regressions
- small variance increases
- non-critical benchmark drift

### Diagnostic

Metrics that help explain what happened but should not directly decide the release.

## Gate Design Rules

- tie every gate to a named baseline
- document why each gate exists
- keep the number of hard gates small
- avoid mixing incompatible metrics into one threshold
- define who can override a gate and under what evidence

## Failure Modes

- dashboard inflation with no real decision logic
- release blocked by noisy metrics
- no distinction between must-pass and diagnostic metrics
- changing the benchmark and the threshold at the same time
