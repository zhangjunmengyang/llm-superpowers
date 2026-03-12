# 示例：合成数据方案

## 什么时候使用

当算法阶段大体已经确定，但真正瓶颈在训练数据本身，例如 coverage、schema、filtering、preference 构造或 trace 质量时，用这个模式。

## Lead Skill

- `llm-synthetic-data`

## Support Skills

- `data-curation-and-filtering`
- `sft-recipe-design`

## Starter Prompt

```text
Use $llm-synthetic-data to design the best training-data plan for this model update.

Context:
- task family: <general assistant / coding / math / domain-specific>
- training objective: <SFT / preference optimization / reward model / reasoning traces>
- current source material: <raw corpus, prompts, demos, pairwise labels, traces>
- known data problems: <coverage gaps, label noise, verbosity bias, contamination risk>
- constraints: <data budget, labeling budget, turnaround time>

Return:
- recommended dataset type and schema
- generation or collection path
- filtering and curation rules
- minimum quality checks
- what should not be synthesized
```

## 期望输出

- 数据集目标
- schema
- 生成路径
- 过滤策略
- 质量检查
- 升级风险

## 下一步

如果数据集主要是给 SFT 用的，hand off 给 `sft-recipe-design`。

如果核心问题是 filtering、去重或数据质量，hand off 给 `data-curation-and-filtering`。

如果数据集需要 reasoning traces 或 verifier signals，hand off 给 `llm-reasoning-posttrain`。
