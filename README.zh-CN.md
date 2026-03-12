# LLM 算法工程师 Superpowers

[English](README.md) | 简体中文

除根 README 外，仓库其余文档和 skills 以英文为准，不再维护中文版，避免内容漂移。

`llm-superpowers` 现在不再以泛 skill 分类为中心。

它的核心单元是 **program**：

- 一条具体操作回路
- 明确的 artifacts
- 命名清楚的指标
- keep 或 discard 决策
- 升级到 eval、systems 或 research review 的路径

Skills 仍然保留，但它们现在是局部原语。
Sequence 由 programs 负责。

## 这个仓库是什么

这个仓库聚焦 LLM 工程里最核心的训练侧工作：

- 后训练
- 数据设计
- 评测与 regression review
- 系统排障
- 研究复现

它不是：

- AI 应用框架
- awesome list
- benchmark 排行榜
- 一堆宽而空的算法分类卡片

## 范式

这个仓库现在有三层：

1. **Programs**
   - 长时间运行的操作回路，例如实验管理、评测评审和 systems triage
2. **Skills**
   - 锋利的局部过程，例如实验设计、eval board 构建、数据产品设计和 run ledger discipline
3. **Templates**
   - 可落地 artifact，例如 `results.tsv`、experiment cards、eval boards 和 triage logs

规则很简单：

- programs 负责 orchestration
- skills 只把一个局部工作做深
- templates 让实验结果可追溯

## Programs

先从这里开始：

- [programs/README.md](programs/README.md)
- [programs/experiment-loop.md](programs/experiment-loop.md)
- [programs/eval-board.md](programs/eval-board.md)
- [programs/systems-war-room.md](programs/systems-war-room.md)
- [programs/research-to-experiment.md](programs/research-to-experiment.md)

这些才是仓库当前真正的 operating modes。

## 当前高价值 Skills

现在最有价值的 skills 是：

- `llm-posttrain-pipeline`
  - 设计下一轮真实实验
- `llm-synthetic-data`
  - 设计可审计的数据产品
- `llm-eval-loop`
  - 构建真正的评测看板
- `llm-training-systems`
  - 做有测量依据的 systems triage
- `llm-research-to-recipe`
  - 抽取 irreducibles 和第一轮 runnable experiment
- `run-ledger-and-keep-discard`
  - 决定一轮实验是否推进 baseline
- `checkpoint-regression-triage`
  - 把坏切片转成下一轮 isolating run
- `throughput-and-oom-triage`
  - 一次只改一个轴地修复失效运行

## 它到底改变什么

`superpowers` 之所以有力量，是因为它会把 coding agent 拉进一条更紧的开发闭环。

`llm-superpowers` 想做的是训练侧的对应物：

- scale-up 之前先写 experiment card
- promotion 之前先过 eval board
- 每一轮严肃实验后都要 keep / discard
- systems 调参前先做最小可复现

如果这套仓库在下面这些场景里不能明显改变 agent 的行为，那它就还不够好，还得继续迭代。

### 场景 1：启动一轮 SFT

如果没有 `llm-superpowers`，一个强 agent 往往也能给出看起来合理的 recipe，但常见结果是：

- data、template、finetuning method 一起改
- 没有 smallest meaningful delta
- 没有 kill condition 和 rollback point
- 最终给的是建议，不是可执行工件

如果用了 `llm-superpowers`，期望路径应该是：

- 从 [programs/experiment-loop.md](programs/experiment-loop.md) 开始
- 调 `$llm-posttrain-pipeline`
- 先写一张只有一个 change surface 的 experiment card
- 在开跑前就定义 smoke set、success bar 和 kill bar
- 跑完以后明确记录 keep / discard / crash / investigate

### 场景 2：一轮 DPO demo 看起来更好，但总觉得不对

如果没有 `llm-superpowers`，常见失败方式是：

- 只追全局均值
- 最坏切片被一笔带过
- 太早把问题归因给“算法不行”
- 一次给出三个下一轮实验，而不是一个 isolating run

如果用了 `llm-superpowers`，期望路径应该是：

- 从 [programs/eval-board.md](programs/eval-board.md) 开始
- 调 `$llm-eval-loop`
- 先看 worst failures，不先看 best wins
- 再用 `$checkpoint-regression-triage` 做 failure clustering
- 最后给出一个被失败簇约束过的下一轮实验

### 场景 3：训练 OOM 或吞吐崩掉

如果没有 `llm-superpowers`，agent 很容易：

- sequence、batch、kernel、framework 一起改
- 只在 full scale 上瞎调
- 看到 throughput 变好就宣布成功
- 最后把 comparability 也调没了

如果用了 `llm-superpowers`，期望路径应该是：

- 从 [programs/systems-war-room.md](programs/systems-war-room.md) 开始
- 调 `$llm-training-systems`
- 先做 smallest credible reproduction
- 每次只改一个轴
- 只有 `$throughput-and-oom-triage` 和质量 smoke set 都过了，才接受这个 fix

### 场景 4：复现一篇 paper 或公开 repo

如果没有 `llm-superpowers`，常见模式是：

- 过度照抄 paper stack
- 盲目继承 scale assumptions
- 在核心 claim 还没被验证前就花了太多算力
- 到很后面才发现真正起作用的 ingredient 根本没保住

如果用了 `llm-superpowers`，期望路径应该是：

- 从 [programs/research-to-experiment.md](programs/research-to-experiment.md) 开始
- 调 `$llm-research-to-recipe`
- 先把 irreducibles 和 paper-specific 细节分开
- 先写 cheaper approximation，再谈 faithful 大复现
- 在项目变成长跑之前，先写 kill criteria

这套仓库最强的时候，不是让一个 agent 变得“更会说”，而是让它从“听起来合理”变成“过程严谨、结果可比、可以连续自循环实验”。

## 快速开始

1. 先把仓库安装进你的 runtime。
   - 见 [docs/installation.md](docs/installation.md)
2. 在你的项目里创建 `runboard/` 目录。
3. 从 [programs/templates](programs/templates) 复制模板。
4. 选一个 program。
5. 每次只用一个 lead skill 跑这一轮。

如果你只想拿第一条 prompt，直接用：

```text
Use $llm-posttrain-pipeline to turn this objective into one experiment card with a named baseline, one change surface, a success condition, a kill condition, and a rollback point.
```

## 安装

### Claude Code

```bash
curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh | bash -s -- --runtime claude-code --profile starter
```

### Codex

```bash
curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh | bash -s -- --runtime codex --profile starter
```

或者直接告诉 Codex：

```text
Fetch and follow instructions from https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/.codex/INSTALL.md
```

### OpenCode

```bash
curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh | bash -s -- --runtime opencode --profile starter
```

### OpenClaw

```bash
curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh | bash -s -- --runtime openclaw --profile starter
```

### OpenSkills 兼容环境

```bash
npx -y openskills install -u -y https://github.com/zhangjunmengyang/llm-superpowers.git
npx -y openskills sync
```

完整矩阵见 [docs/runtime-matrix.md](docs/runtime-matrix.md)。

## 仓库结构

```text
llm-superpowers/
├── README.md
├── README.zh-CN.md
├── programs/
│   ├── README.md
│   ├── experiment-loop.md
│   ├── eval-board.md
│   ├── systems-war-room.md
│   ├── research-to-experiment.md
│   └── templates/
├── skills/
│   ├── llm-posttrain-pipeline/
│   ├── llm-synthetic-data/
│   ├── llm-eval-loop/
│   ├── llm-training-systems/
│   ├── llm-research-to-recipe/
│   ├── run-ledger-and-keep-discard/
│   ├── checkpoint-regression-triage/
│   └── throughput-and-oom-triage/
└── docs/
    ├── installation.md
    ├── runtime-matrix.md
    └── runtime-patterns.md
```

## 设计规则

- programs 负责 orchestration
- skills 必须可以独立使用
- 每一轮严肃实验都必须留下 durable artifacts
- 没有 named baseline，就不能 keep
- 不看 averages 之外的坏切片，就不能 sign off
- 不做 quality recheck，就不能把 systems fix 叫成功
- 没有 irreducibles、approximation 和 kill criteria，就不能叫 paper reproduction

## 公开基础

这个仓库主要受这些项目启发：

- [obra/superpowers](https://github.com/obra/superpowers)
- [karpathy/autoresearch](https://github.com/karpathy/autoresearch)
- [anthropics/skills](https://github.com/anthropics/skills)
- [huggingface/trl](https://github.com/huggingface/trl)
- [OpenRLHF/OpenRLHF](https://github.com/OpenRLHF/OpenRLHF)
- [volcengine/verl](https://github.com/volcengine/verl)
- [huggingface/open-r1](https://github.com/huggingface/open-r1)
- [allenai/open-instruct](https://github.com/allenai/open-instruct)

## 近期方向

接下来最值得补的，不是再扩更多大类，而是补更锋利的 operating modules，例如：

- data-mixture-design
- reward-hacking-audit
- long-context-posttraining
- sample-review-protocol
- judge-and-reward-shaping

## 开源基础

- [LICENSE](LICENSE)
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [docs/installation.md](docs/installation.md)
