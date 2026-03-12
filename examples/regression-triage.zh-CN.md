# 示例：回归排查

## 什么时候使用

当一个新 checkpoint 在 demo 中看起来不错，但你还不知道它应该发布、继续放大还是直接回滚时，用这个模式。

## Lead Skill

- `llm-eval-loop`

## Support Skills

- `eval-and-regression-gates`
- `llm-posttrain-pipeline`

## Starter Prompt

```text
Use $llm-eval-loop to compare this candidate checkpoint against the baseline and define whether we should ship, hold, or investigate.

Context:
- baseline: <checkpoint A>
- candidate: <checkpoint B>
- target improvements: <what was supposed to get better>
- known concerns: <safety / reasoning / latency / reward / style>
- available benchmarks: <current eval assets>

Return:
- minimum benchmark plan
- key metrics that should decide this comparison
- likely blind spots
- whether we need explicit regression gates
- recommended next action
```

## 期望输出

- benchmark 方案
- 对比逻辑
- blind spots
- ship 或 hold 建议

## 下一步

如果测量方式是对的，但 signoff 逻辑还不清楚，hand off 给 `eval-and-regression-gates`。

如果结果说明 recipe 本身选错了，hand off 给 `llm-posttrain-pipeline`。
