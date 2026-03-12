# 模块映射

这个文档说明 umbrella skills 和 specialist modules 的关系。

## 双层模型

`llm-superpowers` 当前有两层：

### 1. Umbrella Skills

负责更宽的工作模式。

- `llm-posttrain-pipeline`
- `llm-synthetic-data`
- `llm-reasoning-posttrain`
- `llm-eval-loop`
- `llm-training-systems`
- `llm-research-to-recipe`

### 2. Specialist Modules

负责更窄工作切片里的深执行。

- `sft-recipe-design`
- `preference-optimization`
- `reward-modeling`
- `online-rl-posttraining`
- `reasoning-prm-verifier`
- `data-curation-and-filtering`

## 映射关系

| Umbrella skill | 常见 hand-off 的 specialist modules |
| --- | --- |
| `llm-posttrain-pipeline` | `sft-recipe-design`, `preference-optimization`, `reward-modeling`, `online-rl-posttraining` |
| `llm-synthetic-data` | `data-curation-and-filtering` |
| `llm-reasoning-posttrain` | `reasoning-prm-verifier` |
| `llm-eval-loop` | 当前还没有；未来应由 `eval-and-regression-gates` 进一步加强这一层 |
| `llm-training-systems` | 当前还没有；未来应由 `training-systems-debug` 把这一层切得更细 |
| `llm-research-to-recipe` | 抽取完成后，可以 hand off 给任意 umbrella 或 specialist module |

## 设计规则

先用 umbrella 决定方向。

再用 specialist 把方向做实。

如果一个 specialist 开始吸收过多广义编排逻辑，那它大概率应该回到 umbrella 层。
