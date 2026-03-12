# 运行时矩阵

这个文档按 agent runtime 列出安装命令。

目标目录优先遵循公开可见的官方或社区约定 skill 路径；没有明确公开约定的部分，则使用仓库自己的 installer preset。

## 全局安装

| Runtime | 命令 | 目标目录 |
| --- | --- | --- |
| Claude Code | `curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh \| bash -s -- --runtime claude-code --profile starter` | `~/.claude/skills` |
| Codex | `curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh \| bash -s -- --runtime codex --profile starter` | `${CODEX_HOME:-~/.codex}/skills` |
| OpenCode | `curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh \| bash -s -- --runtime opencode --profile starter` | `~/.config/opencode/skills` |
| OpenClaw | `curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh \| bash -s -- --runtime openclaw --profile starter` | `~/.openclaw/workspace/skills` |

## 项目内安装

请在目标项目根目录执行这些命令。

| Runtime | 命令 | 目标目录 |
| --- | --- | --- |
| Claude Code | `curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh \| bash -s -- --runtime claude-code-project --profile starter` | `./.claude/skills` |
| OpenCode | `curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh \| bash -s -- --runtime opencode-project --profile starter` | `./.opencode/skills` |

## 通用 repo 安装

适用于 OpenSkills 兼容环境：

```bash
npx -y openskills install -u -y https://github.com/zhangjunmengyang/llm-superpowers.git
npx -y openskills sync
```

这条路径适合：

- 基于 AGENTS 的共享环境
- 团队已经标准化到 OpenSkills
- 运行时本身还没有这个仓库的原生 preset

## 说明

- `starter` 会装最小但高价值的一组后训练 skills。
- 想装仓库当前全部 skills，就切到 `--profile all`。
- 本地 clone 的情况下，想保持单一 source of truth，可以用 `--mode symlink`。
- 如果你的运行时有固定 skill 目录但仓库还没加 preset，就用 `--target-dir /path/to/skills`。
