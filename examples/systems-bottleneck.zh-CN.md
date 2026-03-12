# 示例：系统瓶颈

## 什么时候使用

当一次运行被 OOM、低吞吐、不稳定、rollout collapse 或其他基础设施行为卡住，导致算法迭代无法稳定推进时，用这个模式。

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

## 期望输出

- bottleneck 分类
- 测量计划
- 修复优先级
- rollback 信号
- hand-off 建议

## 下一步

如果问题已经足够具体且局部化，hand off 给 `training-systems-debug`。

如果系统行为可能掩盖了真实模型质量，hand off 给 `llm-eval-loop`。
