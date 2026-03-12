# Run Ledger

Use this file to record experiments in a way that survives memory loss and hype.

## Minimum Row Schema

Use at least:

- experiment id
- parent commit or checkpoint
- change surface
- primary metric
- primary delta vs baseline
- repeatability or noise band
- guardrail summary
- peak memory
- throughput
- status
- decision rationale
- next question

## Rerun Policy

Rerun or investigate before promotion when:

- the primary delta sits inside the repeatability band
- judge disagreement is still high
- systems instability may have corrupted comparability
- the eval suite, decoding, or prompts drifted
- failure review has not happened yet

## Decision Tests

### Keep

Use `keep` only when:

- the run beat the named baseline
- hard blockers stayed acceptable
- the result was not invalidated by systems or eval drift

### Discard

Use `discard` when:

- the run is clearly worse
- the tradeoff is not worth the complexity
- the run answered the question negatively

### Crash

Use `crash` when:

- the run never produced a valid comparable result
- the idea itself or implementation failed before judgment

### Investigate

Use `investigate` when:

- the result is ambiguous
- judge disagreement is high
- systems instability or contamination may have invalidated the comparison

## Promotion Checklist

Do not advance the baseline until all of these are true:

- named baseline is still the comparison target
- primary gain beats the repeatability band
- hard blockers stayed acceptable
- the result survives worst-slice review
- the change surface is understood well enough to build on next

## Anti-Patterns

- keeping a run because samples looked cool
- discarding a run without writing the reason
- changing the baseline silently
- overwriting the ledger instead of appending evidence
