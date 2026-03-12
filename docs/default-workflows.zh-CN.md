# 默认工作流

这个文档展示这些 skills 在真实算法工程里该如何组合。

## 工作流 1：新的后训练方案

适用场景：团队已经有底模和目标能力，但还没有确定 recipe。

1. `llm-posttrain-pipeline`
2. `sft-recipe-design` 或 `preference-optimization`
3. `llm-synthetic-data` 或 `data-curation-and-filtering`
4. `llm-eval-loop`
5. 如果放大规模成了瓶颈，再用 `llm-training-systems`

期望输出：

- 阶段与算法选择
- 数据集 schema
- benchmark 方案
- scale-up 注意事项

## 工作流 2：reasoning 增强

适用场景：模型需要更强的数学、代码或多步推理能力。

1. `llm-reasoning-posttrain`
2. `reasoning-prm-verifier`
3. `llm-synthetic-data` 或 `data-curation-and-filtering`
4. `llm-eval-loop`
5. 如果 RL 或 verifier 循环过贵，再用 `llm-training-systems`

期望输出：

- reasoning recipe
- trace 与 label schema
- verifier 或 reward 定义
- reasoning 专项评测门槛

## 工作流 3：研究复现

适用场景：起点是一篇论文或一个公开仓库。

1. `llm-research-to-recipe`
2. `llm-posttrain-pipeline`
3. 一个 specialist module，例如 `sft-recipe-design`、`preference-optimization` 或 `reward-modeling`
4. `llm-eval-loop`
5. 如果复现必须放大规模，再用 `llm-training-systems`

期望输出：

- faithful recipe
- 更便宜的近似版
- 实验计划
- 验证标准

## 工作流 4：回归排查

适用场景：新 checkpoint demo 看起来更好，但整体感觉不稳。

1. `llm-eval-loop`
2. `llm-posttrain-pipeline`
3. `llm-synthetic-data`、`reasoning-prm-verifier` 或 `preference-optimization`

期望输出：

- regression 诊断
- 最可能的根因层级
- 下一轮实验建议

## 工作流 5：系统瓶颈

适用场景：recipe 大体已定，但训练被系统问题卡住。

1. `llm-training-systems`
2. `llm-eval-loop`

期望输出：

- bottleneck 假设
- 有测量依据的干预顺序
- 可安全回滚的优化计划
