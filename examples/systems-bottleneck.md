# Example: Systems Bottleneck

## When To Use

Use this pattern when a run is blocked by OOMs, low throughput, instability, rollout collapse, or infrastructure behavior that makes algorithm iteration unreliable.

## Lead Skill

- `llm-training-systems`

## Support Skills

- `training-systems-debug`
- `llm-eval-loop`

## Starter Prompt

```text
Use $llm-training-systems to diagnose this training or rollout bottleneck.

Context:
- stage: <CPT / SFT / DPO / RM / RL>
- hardware: <GPU type, count, interconnect>
- stack: <framework, trainer, inference engine, launch method>
- observed bottleneck: <OOM / slow tokens/sec / instability / deadlock / rollout underfill>
- recent changes: <what changed before the regression>
- current measurements: <memory, throughput, utilization, latency, failure logs>

Return:
- most likely bottleneck class
- next measurements to collect
- highest-leverage fixes
- rollback condition
- whether this is purely a systems issue or is confounded with recipe quality
```

## Expected Output

- bottleneck classification
- measurement plan
- ranked fixes
- rollback signal
- hand-off recommendation

## Next Step

If the issue is now concrete and local, hand off to `training-systems-debug`.

If the systems behavior may be masking true model quality, hand off to `llm-eval-loop`.
