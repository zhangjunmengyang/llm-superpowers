# Runtime Matrix

This document lists the installation commands by agent runtime.

The target directories follow the runtime's documented or de facto skill locations where those are publicly available, and the repository's own installer presets otherwise.

## Global Installs

| Runtime | Command | Target |
| --- | --- | --- |
| Claude Code | `curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh \| bash -s -- --runtime claude-code --profile starter` | `~/.claude/skills` |
| Codex | `curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh \| bash -s -- --runtime codex --profile starter` | `${CODEX_HOME:-~/.codex}/skills` |
| OpenCode | `curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh \| bash -s -- --runtime opencode --profile starter` | `~/.config/opencode/skills` |
| OpenClaw | `curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh \| bash -s -- --runtime openclaw --profile starter` | `~/.openclaw/workspace/skills` |

## Project-Local Installs

Run these from the project root where you want the skills to live.

| Runtime | Command | Target |
| --- | --- | --- |
| Claude Code | `curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh \| bash -s -- --runtime claude-code-project --profile starter` | `./.claude/skills` |
| OpenCode | `curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh \| bash -s -- --runtime opencode-project --profile starter` | `./.opencode/skills` |

## Universal Repo Install

For OpenSkills-compatible environments:

```bash
npx -y openskills install -u -y https://github.com/zhangjunmengyang/llm-superpowers.git
npx -y openskills sync
```

This path is useful for:

- shared AGENTS-based setups
- teams standardizing on OpenSkills
- agent environments without a native runtime preset in this repository

## Notes

- `starter` installs the smallest high-value set for post-training work.
- switch to `--profile all` when you want every current skill in the repository.
- use `--mode symlink` for a source-of-truth install from a local clone.
- use `--target-dir /path/to/skills` when your runtime has a known directory but no preset yet.
