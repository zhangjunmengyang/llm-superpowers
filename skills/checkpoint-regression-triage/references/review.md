# Regression Review

Use this file to turn regressions into the next good experiment.

## Review Order

1. look at the worst slice first
2. inspect sampled failures
3. check whether failures are consistent or mixed
4. assign a likely layer
5. propose one isolating run

## Default Coverage

- review the 20 worst failures overall
- review 5 to 10 failures for each critical slice
- if failures are heterogeneous, cluster before proposing a fix
- if confidence is low, write `investigate` instead of inventing certainty

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

## Common Failure Clusters

### Formatting Drift

- markers, delimiters, or chat turns changed
- baseline and candidate become comparable again after normalization

### Verbosity Drift

- candidate wins style judges by being longer
- quality does not improve when outputs are length-matched

### Truncation Or Early Stop

- answers look clipped, incomplete, or suddenly terse
- regressions concentrate on long-context prompts

### Data Coverage Hole

- easy slices improve while one domain or task family collapses
- failures reflect missing or low-quality training support

### Reward Shortcut

- reward or judge-facing metrics improve while human reading worsens
- failures follow the same superficial pattern repeatedly

## Next-Run Mapping

- formatting drift -> freeze template and rerun one formatting-only isolation
- verbosity drift -> normalize length and audit judge or reward bias
- truncation -> isolate sequence, decoding, or systems changes
- data coverage hole -> build one targeted data patch, not a broad algorithm swap
- reward shortcut -> audit reward or pair rubric before more RL or preference tuning

## Anti-Patterns

- averaging away the worst slice
- proposing three next runs at once
- reading only “interesting” examples instead of the worst examples
