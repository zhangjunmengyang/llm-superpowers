# Data Filtering Policies

Use this file to design curation rules for training data.

## Core Filter Types

- exact duplicate removal
- near-duplicate detection
- low-signal or generic-answer filtering
- label-conflict filtering
- broken-format filtering
- contamination and overlap checks

## Mixture Design Rules

- define the target distribution before balancing
- keep scarce high-value data visible instead of drowning it in bulk
- document why each source is included
- separate exploratory data from trusted core data

## Review Queue Heuristics

Send examples to manual review when:

- labels conflict
- formatting is suspicious
- the example is high-impact but ambiguous
- a filter score is near the threshold

## Failure Modes

- removing too aggressively and losing target behaviors
- keeping low-signal bulk data because it is large
- leakage between train and eval
- dedup only at exact-match level
- no provenance for later debugging
