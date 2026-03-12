# Codex 安装

[English](INSTALL.md) | 简体中文

把 `llm-superpowers` 安装到本地 Codex skills 目录。

## 默认安装

执行：

```bash
curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh | bash -s -- --runtime codex --profile starter
```

## 完整安装

执行：

```bash
curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh | bash -s -- --runtime codex --profile all
```

## 验证

安装后确认这个目录存在：

```text
${CODEX_HOME:-$HOME/.codex}/skills
```

`starter` profile 默认会装这些：

- `llm-posttrain-pipeline`
- `llm-eval-loop`
- `llm-reasoning-posttrain`
- `sft-recipe-design`
- `preference-optimization`
- `training-systems-debug`

然后直接从这个 prompt 开始：

```text
Use $llm-posttrain-pipeline to decide the next post-training stage for this model, recommend the best open-source framework, and define the minimum dataset and eval plan.
```
