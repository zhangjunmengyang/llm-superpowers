# 示例：从论文到 recipe

## 什么时候使用

当一篇论文或公开仓库看起来很值得做，但真正的问题是“最小 faithful reproduction 是什么”和“更便宜的工程近似版是什么”时，用这个模式。

## Lead Skill

- `llm-research-to-recipe`

## Support Skills

- `llm-posttrain-pipeline`
- `llm-training-systems`

## Starter Prompt

```text
Use $llm-research-to-recipe to turn this paper or repository into a runnable engineering plan.

Context:
- source: <paper title / arXiv link / GitHub repo>
- target capability: <what we want to reproduce or borrow>
- available hardware: <compute and serving limits>
- acceptable approximation: <how far we can simplify>
- current stack: <frameworks and infra we already trust>

Return:
- minimum faithful recipe
- irreducible components we cannot skip
- cheapest useful approximation
- evaluation plan for deciding whether reproduction worked
- major implementation traps
```

## 期望输出

- faithful recipe
- 近似版方案
- 不可省略的组件
- 评测方案
- 实现风险

## 下一步

如果 recipe 已经合理、只差阶段选择，hand off 给 `llm-posttrain-pipeline`。

如果论文方案受系统不匹配阻塞，hand off 给 `llm-training-systems`。
