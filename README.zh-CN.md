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
