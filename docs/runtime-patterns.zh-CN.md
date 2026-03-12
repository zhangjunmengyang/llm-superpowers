# 运行时集成模式

这个仓库刻意保持 runtime-agnostic。

目标是让这个 skill pack 能适配不同 coding-agent 环境，而不是绑死在单一产品 UI 或某种 vendor 专属安装流程上。

## 稳定契约

任何运行时集成都应该保留下面这个基础契约：

- 每个 skill 都是 `skills/` 下的独立目录
- 每个 skill 都包含 `SKILL.md`
- 每个 skill 都包含 `agents/openai.yaml`
- 每个 skill 都可以从 `references/` 加载额外材料

只要某个 runtime 能发现并消费这种目录结构，它通常就能较低成本接入这个仓库。

## 推荐集成模式

如果你想直接用一条命令安装，用 [../scripts/install.sh](../scripts/install.sh)。
如果你的环境支持 OpenSkills，用 `npx -y openskills install -u -y https://github.com/zhangjunmengyang/llm-superpowers.git`。
如果你只想看按运行时分的命令，直接看 [runtime-matrix.zh-CN.md](runtime-matrix.zh-CN.md)。

### 1. 直接目录发现

适用场景：你的 runtime 可以读取任意本地 skills 目录。

让 runtime 指向：

```text
<repo-root>/skills
```

这是最干净的方式，因为：

- 上游更新不会被破坏
- 不需要复制文件
- skill 边界保持清晰

如果 runtime 已经暴露出稳定的本地 skill 目录，安装器就可以直接用 preset 安装，例如 `--runtime codex`。
当前可用 preset 包括 `claude-code`、`claude-code-project`、`codex`、`opencode`、`opencode-project` 和 `openclaw`。

### 2. 选择性软链接安装

适用场景：你的 runtime 需要把 skills 放进某个专门目录。

把仓库 clone 一次，然后只软链接你真正要用的 skills：

```bash
SKILLS_HOME="${SKILLS_HOME:-$HOME/.codex/skills}"
mkdir -p "$SKILLS_HOME"

ln -s /path/to/llm-superpowers/skills/llm-posttrain-pipeline "$SKILLS_HOME/llm-posttrain-pipeline"
ln -s /path/to/llm-superpowers/skills/llm-eval-loop "$SKILLS_HOME/llm-eval-loop"
ln -s /path/to/llm-superpowers/skills/sft-recipe-design "$SKILLS_HOME/sft-recipe-design"
```

这种方式通常比复制更好，因为：

- 更新更容易
- 本地定制更明确
- 仓库能保持单一 source of truth

安装器也能代替你做：

```bash
./scripts/install.sh --target-dir /path/to/runtime/skills --profile starter --mode symlink
```

### 3. 内部 vendored 依赖

适用场景：团队想把这个 skill pack 接进内部 monorepo。

常见方式：

- 以 submodule 方式接入
- 把 `skills/` 目录镜像进内部仓库
- 在内部工具里 pin 住一个具体 commit

这种方式适合：

- 可复现性重要
- 多个工程师要共享同一版本的 skills
- 内部包装层或治理流程需要冻结依赖

### 3.5. 通用 repo 安装器

适用场景：你的环境已经支持 OpenSkills 风格分发。

安装命令：

```bash
npx -y openskills install -u -y https://github.com/zhangjunmengyang/llm-superpowers.git
npx -y openskills sync
```

这种方式在这些情况下很好用：

- runtime 读取 `.agent/skills`
- 你想从 GitHub repo 直接安装，而不是依赖自定义 shell 脚本
- 你想给 skills 做出接近包管理器的安装体验

### 4. Prompt-only fallback

适用场景：你的 runtime 还不支持 skill discovery。

这时你可以：

1. 打开对应 skill 目录
2. 读 `SKILL.md`
3. 从 [../examples/README.zh-CN.md](../examples/README.zh-CN.md) 里复制一个 starter prompt
4. 把 example 里的 expected output shape 当成你的回答契约

这比原生 skill loading 弱，但已经足够让仓库发挥作用。

## 首次安装建议

对于新用户，先从这组开始：

- `llm-posttrain-pipeline`
- `llm-eval-loop`
- `llm-reasoning-posttrain`
- `sft-recipe-design`
- `preference-optimization`
- `training-systems-debug`

这组已经覆盖大多数早期后训练工作，又不会让 runtime 被太多邻近 skills 淹没。

## 升级纪律

在真实工作流里升级这个仓库时：

1. 大实验前先 pin 住一个 commit
2. 在干净分支里拉上游更新
3. 用 [../examples/README.zh-CN.md](../examples/README.zh-CN.md) 里已知 prompt 做一次 smoke test
4. 新增 skills 要逐步暴露，不要一次全开

## 不要这样做

- 不要把所有 skills 压平到一个超大文件
- 不要下游已经在用时还随意改 skill 文件夹名
- 不要在同一个 prompt 里平铺并列很多 umbrella skills
- 不要把这些 examples 当成框架专属 recipe
