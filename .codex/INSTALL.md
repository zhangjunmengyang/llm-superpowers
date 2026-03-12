# Codex Install

Install `llm-superpowers` into the local Codex skills directory.

## Default Install

Run:

```bash
curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh | bash -s -- --runtime codex --profile starter
```

## Full Install

Run:

```bash
curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh | bash -s -- --runtime codex --profile all
```

## Verify

After install, confirm the following directory exists:

```text
${CODEX_HOME:-$HOME/.codex}/skills
```

The starter profile should install:

- `llm-posttrain-pipeline`
- `llm-eval-loop`
- `llm-reasoning-posttrain`
- `sft-recipe-design`
- `preference-optimization`
- `training-systems-debug`

Then start with:

```text
Use $llm-posttrain-pipeline to decide the next post-training stage for this model, recommend the best open-source framework, and define the minimum dataset and eval plan.
```
