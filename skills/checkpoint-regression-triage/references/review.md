# Regression Review

Use this file to turn regressions into the next good experiment.

## Review Order

1. look at the worst slice first
2. inspect sampled failures
3. check whether failures are consistent or mixed
4. assign a likely layer
5. propose one isolating run

## Root-Cause Layers

### Data

Signals:

- target behavior disappeared only on one distribution
- answer quality suggests coverage gaps or wrong negatives

### Recipe

Signals:

- broad behavior shift after a stage change
- over-optimization on one objective with another objective drifting

### Reward Or Judge

Signals:

- the training signal and human reading disagree
- gains appear mostly on the same style the judge prefers

### Systems

Signals:

- instability, throughput collapse, or truncation changed the comparison

### Prompt Or Formatting

Signals:

- regressions disappear when formatting is normalized
- failures cluster around template, tokenizer, or chat-style drift

## Anti-Patterns

- averaging away the worst slice
- proposing three next runs at once
- reading only “interesting” examples instead of the worst examples
