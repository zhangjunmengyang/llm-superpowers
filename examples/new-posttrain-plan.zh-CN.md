# 示例：新的后训练方案

## 什么时候使用

当你已经有一个模型和目标行为，但还没决定下一步该做 SFT、preference optimization、reward modeling 还是 online RL 时，用这个模式。

## Lead Skill

- `llm-posttrain-pipeline`

## Support Skills

- `llm-synthetic-data`
- `llm-eval-loop`

## Starter Prompt

```text
Use $llm-posttrain-pipeline to decide the next post-training stage for this model.

Context:
- base model: <model-name>
- target behavior: <what should improve>
- current assets: <SFT data / preference data / reward data / checkpoints>
- constraints: <compute, latency, timeline>

Return:
- recommended next stage
- why this stage is better than the nearest alternatives
- best open-source framework to start from
- minimum dataset schema
- minimum eval plan
- likely failure risks
```

## 期望输出

- 阶段选择
- 算法选择
- 框架建议
- 数据集 schema
- 评测要求
- scale-up 说明

## 下一步

如果答案选的是 SFT，hand off 给 `sft-recipe-design`。

如果答案选的是 DPO 或其他离线 preference 方法，hand off 给 `preference-optimization`。

如果答案选的是 reward-plus-RL，hand off 给 `reward-modeling` 或 `online-rl-posttraining`。
