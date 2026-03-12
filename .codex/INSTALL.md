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

The starter profile should install the core operating set:

- `llm-posttrain-pipeline`
- `llm-synthetic-data`
- `llm-eval-loop`
- `llm-training-systems`
- `llm-research-to-recipe`
- `run-ledger-and-keep-discard`
- `checkpoint-regression-triage`
- `throughput-and-oom-triage`

If you need reasoning-specific skills too, add:

```bash
curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh | bash -s -- --runtime codex --skill llm-reasoning-posttrain --skill reasoning-prm-verifier
```

Then start with:

```text
Open programs/experiment-loop.md, then use $llm-posttrain-pipeline to turn this objective into one experiment card with a named baseline, one change surface, a success condition, a kill condition, and a rollback point.
```
