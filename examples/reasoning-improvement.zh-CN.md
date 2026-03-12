# 示例：reasoning 增强

## 什么时候使用

当目标是 reasoning correctness、step 质量、PRM 设计、verifier 设计，或者 R1 风格增强时，用这个模式。

## Lead Skill

- `llm-reasoning-posttrain`

## Support Skills

- `reasoning-prm-verifier`
- `llm-eval-loop`

## Starter Prompt

```text
Use $llm-reasoning-posttrain to design the best reasoning-improvement path for this model.

Context:
- task family: <math / code / science / mixed reasoning>
- current baseline: <current model and observed failure pattern>
- available assets: <reasoning traces / verifier / reward model / none>
- constraints: <compute, turnaround time, need for inference efficiency>

Return:
- whether we should use step SFT, PRM, verifier ranking, best-of-n, or online RL
- the minimum trace schema
- how to supervise correctness
- how to evaluate reasoning gains
- what to avoid
```

## 期望输出

- reasoning recipe 选择
- process supervision 方案
- trace schema
- verifier 或 reward 定义
- 评测方案

## 下一步

如果瓶颈在 process supervision，hand off 给 `reasoning-prm-verifier`。

如果瓶颈在 reasoning 数据生成，hand off 给 `llm-synthetic-data`。

如果瓶颈在 rollout optimization，hand off 给 `online-rl-posttraining`。
