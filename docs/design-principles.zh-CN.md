# 设计原则

这个文档说明 `llm-superpowers` 应该如何使用，以及未来的 skills 应该如何设计。

## 核心假设

LLM 算法工程师通常不是在要泛泛的帮助。

他们通常只是在解决少数几类很具体的工作：

- 选择正确的训练阶段
- 构建或修复数据集
- 提升 reasoning 行为
- 评估一次模型改动
- 排查一次失败运行
- 把研究结果转成实验

仓库应该为这些工作优化，而不是为了主题覆盖面优化。

## 什么是 skill

在这个仓库里，skill 不是：

- 教程
- 长篇综述
- 框架封装
- 产品工作流

skill 是一种面向特定算法工程工作的操作型决策辅助。

它应当帮助另一个 coding agent 回答：

1. 现在是不是该由这个 skill 来 lead？
2. 第一优先级该先决定什么？
3. 应该产出什么结果？
4. 下一步应该 hand off 给哪个邻近 skill？

## 仓库架构

当前架构分成四层。

### 1. Strategy

当问题是“下一步该跑什么”时使用。

Skills：

- `llm-posttrain-pipeline`
- `llm-research-to-recipe`

### 2. Execution

当问题是“需要什么数据或 recipe”时使用。

Skills：

- `llm-synthetic-data`
- `llm-reasoning-posttrain`

### 3. Judgment

当问题是“它到底有没有效果”时使用。

Skills：

- `llm-eval-loop`

### 4. Systems

当问题是“为什么这次运行失败或变慢”时使用。

Skills：

- `llm-training-systems`

## Skill 边界规则

- `llm-posttrain-pipeline` 负责选阶段和算法，不应该变成深度数据设计 skill。
- `llm-synthetic-data` 负责数据 schema 和生成路径，不应该变成框架选型 skill。
- `llm-reasoning-posttrain` 只负责 reasoning 专项改进循环。
- `llm-eval-loop` 负责证据和 acceptance gates，不应该变成庞大的 benchmark 百科。
- `llm-training-systems` 负责系统瓶颈，而不是算法选择。
- `llm-research-to-recipe` 负责把论文和仓库转成可执行产物，而不是执行整条实验。

## 组合规则

优先用一个 lead skill，外加一到两个 supporting skills。

好的组合：

- `llm-posttrain-pipeline` -> `llm-synthetic-data` -> `llm-eval-loop`
- `llm-research-to-recipe` -> `llm-posttrain-pipeline`
- `llm-reasoning-posttrain` -> `llm-eval-loop`
- `llm-training-systems` -> `llm-eval-loop`

不好的组合：

- 四五个 skills 平铺同时调用，没有 lead
- 还没确定 recipe 对不对，就先上 `llm-training-systems`
- baseline 和目标行为都没定义，就先上 `llm-eval-loop`

## 好 skill 的质量线

一个强 skill 至少要讲清：

- 什么时候该触发
- 什么时候不该 lead
- 应该产出什么结果
- 应该 hand off 给哪些邻近 skills

如果一个 skill 读起来更像分类标签，而不是操作原语，那它就太宽了。

## 设计方向

长期方向，是从宽 umbrella 继续往锋利的算法模块收缩。

这意味着未来的工作应该主要放在：

- 拆分宽 skill
- 强化边界
- 补足场景覆盖
- 改善默认输出

而不应该主要放在：

- 继续堆更多主题名词
- 追逐每个新 benchmark
- 把产品工程和训练工程混在一起

## Umbrella 与 Specialist

现在仓库里有两种 skill。

Umbrellas：

- 负责一个宽工作模式
- 负责阶段选择、skill 组合和 hand-off

Specialists：

- 深入某一个更窄的算法子问题
- 通常应该在 umbrella 已经把问题框住以后再调用

specialist 越锋利，仓库就越强。
umbrella 和 specialist 越互相吞并，仓库就越差。
