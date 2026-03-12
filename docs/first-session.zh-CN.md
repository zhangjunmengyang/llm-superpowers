# 第一次会话指南

这个文档面向安装后的前十分钟。

目标不是把所有 skill 都看一遍，而是用正确的 lead skill 和清晰的输出契约，拿到第一条真正有用的回答。

## 第一步：先选一种工作模式

按最接近的起点选：

- 当你需要决定下一训练阶段时，用 `llm-posttrain-pipeline`
- 当瓶颈是数据质量或 schema 时，用 `llm-synthetic-data`
- 当目标是 reasoning correctness 时，用 `llm-reasoning-posttrain`
- 当你需要比较 checkpoints 时，用 `llm-eval-loop`
- 当运行不稳、很慢或内存受限时，用 `llm-training-systems`
- 当你需要把论文或 repo 转成可执行计划时，用 `llm-research-to-recipe`

如果两个 skill 看起来都像，先用更宽的 umbrella，让它来 hand off。

## 第二步：提供最小必要上下文

如果你给出这些信息，第一次会话质量会好很多：

- 模型或 checkpoint 名称
- 想提升的目标行为
- 当前资产，例如 SFT 数据、preference 数据、reward 标签、traces 或 benchmarks
- 约束条件，例如算力、时延、时间线和 serving 限制
- 当前最不确定的点或主要失败模式

## 第三步：要结构化返回

不要只问“你怎么看”。

要让它产出一个决策工件。一个好的首轮返回通常包括：

- recommendation
- 最接近的备选方案以及为什么没选
- 最小可行 recipe
- 最小可行评测计划
- 最可能的失败风险
- 如果要继续深入，下一个该 hand off 给哪个 skill

## 默认会话模板

```text
Use $<lead-skill> to help with this training decision.

Context:
- model or checkpoint: <name>
- target behavior: <what should improve>
- current assets: <datasets, labels, traces, checkpoints, benchmarks>
- constraints: <compute, latency, timeline>
- main uncertainty: <what is unclear right now>

Return:
- best next move
- why it beats the nearest alternatives
- minimum recipe to try first
- minimum eval plan
- main risks
- next skill to call if the task needs to go deeper
```

## 好的首轮会话

- 为新领域适配选择 SFT、DPO 还是 reward-plus-RL
- 判断一个 reasoning 问题到底需要 traces、PRM、verifier ranking 还是 online RL
- 比较 candidate checkpoint 和 baseline，并明确 ship / hold gates
- 决定一篇 paper 应该做 faithful reproduction 还是便宜近似版

## 不好的首轮会话

- 不给模型、数据和约束，就直接要完整训练方案
- 一次并行调四五个 skills
- 目标行为还没定义，就先问 benchmarking
- 明明是系统变慢，却把问题全当成算法问题

## 最快路径

如果你只想最快拿到有用结果，从这些例子开始：

- [../examples/new-posttrain-plan.zh-CN.md](../examples/new-posttrain-plan.zh-CN.md)
- [../examples/synthetic-data-plan.zh-CN.md](../examples/synthetic-data-plan.zh-CN.md)
- [../examples/reasoning-improvement.zh-CN.md](../examples/reasoning-improvement.zh-CN.md)
- [../examples/regression-triage.zh-CN.md](../examples/regression-triage.zh-CN.md)
- [../examples/systems-bottleneck.zh-CN.md](../examples/systems-bottleneck.zh-CN.md)
- [../examples/paper-to-recipe.zh-CN.md](../examples/paper-to-recipe.zh-CN.md)
