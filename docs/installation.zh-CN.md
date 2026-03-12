# 安装与使用

这个仓库是一个 skill pack。具体安装方式取决于你的 coding-agent 运行时。

## 分发模型

当前安装层结合了三种在公开 skill 生态里已经跑通的模式：

- 供 agent 自己抓取执行的 bootstrap file
- 供用户直接复制执行的一条命令安装
- 基于 OpenSkills 的通用 repo 安装

## 按运行时安装

### Claude Code

全局安装：

```bash
curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh | bash -s -- --runtime claude-code --profile starter
```

项目内安装：

```bash
curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh | bash -s -- --runtime claude-code-project --profile starter
```

### Codex

全局安装：

```bash
curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh | bash -s -- --runtime codex --profile starter
```

Bootstrap 文件：

- [../.codex/INSTALL.zh-CN.md](../.codex/INSTALL.zh-CN.md)

### OpenCode

全局安装：

```bash
curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh | bash -s -- --runtime opencode --profile starter
```

项目内安装：

```bash
curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh | bash -s -- --runtime opencode-project --profile starter
```

### OpenClaw

全局安装：

```bash
curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh | bash -s -- --runtime openclaw --profile starter
```

### OpenSkills 兼容环境

```bash
npx -y openskills install -u -y https://github.com/zhangjunmengyang/llm-superpowers.git
npx -y openskills sync
```

简版兼容矩阵见 [runtime-matrix.zh-CN.md](runtime-matrix.zh-CN.md)。

## 一条命令安装

对于有 preset 的运行时：

```bash
curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh | bash -s -- --runtime codex --profile starter
```

对于任意有固定 skills 目录的运行时：

```bash
curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh | bash -s -- --target-dir /path/to/your/runtime/skills --profile all
```

远程安装器会把仓库临时 clone 到一个目录，再从那里完成安装。

## 通过 OpenSkills 通用安装

如果你想要一个已经能跨 OpenSkills 兼容环境工作的 repo 安装路径，用：

```bash
npx -y openskills install -u -y https://github.com/zhangjunmengyang/llm-superpowers.git
npx -y openskills sync
```

这个仓库已经验证过能被 OpenSkills 正常安装，并且能暴露当前全部 14 个 skills。

## Codex Bootstrap 文件

为了支持 `superpowers` 风格的 bootstrap 流程，这个仓库还带了：

- [../.codex/INSTALL.zh-CN.md](../.codex/INSTALL.zh-CN.md)

这个文件就是给 Codex 直接抓取执行用的。

## 本地安装

如果你想先 clone 下来再看：

```bash
git clone https://github.com/zhangjunmengyang/llm-superpowers.git
cd llm-superpowers
./scripts/install.sh --runtime codex --profile starter
```

想装全量时，把 `starter` 换成 `all` 即可。

## 仓库使用方式

从最低要求来看，另一个 agent runtime 至少要能访问：

- `skills/*/SKILL.md`
- `skills/*/agents/openai.yaml`
- `skills/*/references/*`

## 通用使用模式

1. clone 这个仓库。
2. 让你的 runtime 或 skill loader 指向 `skills/` 目录。
3. 先调用一个 umbrella skill。
4. 只在必要时再 hand off 给一到两个 specialist modules。

如果你的 runtime 还不能直接做 skill discovery，就按 [runtime-patterns.zh-CN.md](runtime-patterns.zh-CN.md) 里的 fallback 方式使用。

## 五分钟起步

如果你只想最快上手：

1. clone 仓库。
2. 让你的 runtime 能看到 `skills/` 目录。
3. 先用这个 prompt：

```text
Use $llm-posttrain-pipeline to decide the next post-training stage for this model, recommend the best open-source framework, and define the minimum dataset and eval plan.
```

4. 如果回答指向更窄的问题，再切到对应 specialist module。
5. 用 `examples/` 里的范例当模板。

如果想把第一次会话质量拉高，先读 [first-session.zh-CN.md](first-session.zh-CN.md)。

## 集成模式

这个仓库主要支持三种稳定集成方式：

1. 直接指向目录发现
2. 选择性软链接安装
3. 内部仓库 vendoring

具体见 [runtime-patterns.zh-CN.md](runtime-patterns.zh-CN.md)。

如果你还没有 runtime 集成能力，也可以按 [../examples/README.zh-CN.md](../examples/README.zh-CN.md) 里的模板，用 prompt-only 模式先跑起来。

## 安装器参数

安装器支持：

- `--runtime claude-code`
- `--runtime claude-code-project`
- `--runtime codex`
- `--runtime opencode`
- `--runtime opencode-project`
- `--runtime openclaw`
- `--target-dir <path>`
- `--profile starter`
- `--profile all`
- `--skill <name>` 可重复传入
- `--mode auto|symlink|copy`
- `--force`
- `--dry-run`
- `--list`

## 不同场景的安装方式

- 个人 Claude Code 环境：`./scripts/install.sh --runtime claude-code --profile starter`
- 最快 Codex 安装：`./scripts/install.sh --runtime codex --profile starter`
- 个人 OpenCode 环境：`./scripts/install.sh --runtime opencode --profile starter`
- 个人 OpenClaw 环境：`./scripts/install.sh --runtime openclaw --profile starter`
- 已知技能目录但无 preset 的其他工具：`./scripts/install.sh --target-dir <path> --profile all`
- 想走跨工具 repo 安装：`npx -y openskills install -u -y https://github.com/zhangjunmengyang/llm-superpowers.git`

## 推荐起手顺序

- 新 recipe 规划：先用 `llm-posttrain-pipeline`
- reasoning 专项：先用 `llm-reasoning-posttrain`
- checkpoint 比较与 signoff：先用 `llm-eval-loop` 或 `eval-and-regression-gates`
- 系统瓶颈：先用 `llm-training-systems` 或 `training-systems-debug`

## 当前结构

Umbrella skills：

- `llm-posttrain-pipeline`
- `llm-synthetic-data`
- `llm-reasoning-posttrain`
- `llm-eval-loop`
- `llm-training-systems`
- `llm-research-to-recipe`

Specialist modules：

- `sft-recipe-design`
- `preference-optimization`
- `reward-modeling`
- `online-rl-posttraining`
- `reasoning-prm-verifier`
- `data-curation-and-filtering`
- `eval-and-regression-gates`
- `training-systems-debug`

## 下一批安装层改进

接下来最值得补的是：

- 等更多运行时的 skill 目录稳定后，再补原生 preset
- 给 OpenSkills 之外的 AGENTS 型编辑器补兼容表
- 给需要内部锁版本的团队加 package-manager 风格 wrapper
