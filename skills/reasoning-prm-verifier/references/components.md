# PRM And Verifier Components

Use this file to choose the right process-supervision primitive.

## Choose A PRM When

- you need dense process supervision
- step quality matters during rollout or distillation
- you can label or synthesize step-level correctness

## Choose A Verifier When

- candidate ranking is more important than token-level process supervision
- final correctness can be checked more reliably than every step
- best-of-n or rejection sampling is likely sufficient

## Choose Best-of-N Alone When

- you already have a strong candidate generator
- a verifier is cheap and reliable
- online RL would be overkill

## Label Sources

- human step annotation
- rule-based grading
- synthetic teacher traces
- hybrid review

## Failure Modes

- step labels that reward verbosity
- verifier judging presentation instead of correctness
- process supervision misaligned with downstream ranking use
- expensive process supervision with no measurable gain
