# 示例

[English](README.md) | 简体中文

这个目录给想快速上手的用户用。

每个 example 都会说明：

- 什么时候该用这个 skill
- 一条可直接复制的 starter prompt
- 期望输出长什么样
- 下一步应该接哪个 support skill

## 从这里开始

- [new-posttrain-plan.zh-CN.md](new-posttrain-plan.zh-CN.md)
  - 适合决定下一步后训练阶段
- [synthetic-data-plan.zh-CN.md](synthetic-data-plan.zh-CN.md)
  - 适合做 SFT、preference、trace 数据设计
- [reasoning-improvement.zh-CN.md](reasoning-improvement.zh-CN.md)
  - 适合 reasoning、PRM、verifier 和 RL 类工作
- [regression-triage.zh-CN.md](regression-triage.zh-CN.md)
  - 适合 baseline vs candidate 对比与发布决策
- [systems-bottleneck.zh-CN.md](systems-bottleneck.zh-CN.md)
  - 适合内存、吞吐和稳定性排障
- [paper-to-recipe.zh-CN.md](paper-to-recipe.zh-CN.md)
  - 适合把论文或公开仓库转成可跑实验计划

## 用法

1. 选一个最接近你当前问题的 example。
2. 把里面的 starter prompt 复制进你的 coding-agent runtime。
3. 把模型、数据和目标行为换成你自己的上下文。
4. 保持一个 lead skill，再加最多一到两个 support skills。

## 覆盖范围

这些 examples 覆盖了仓库当前全部 6 个 umbrella skills，新用户不需要猜该从哪里起手。
