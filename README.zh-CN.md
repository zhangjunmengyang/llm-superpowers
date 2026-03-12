# LLM 算法工程师 Superpowers

[English](README.md) | 简体中文

面向 LLM 算法工程师的开源技能包。

这个仓库聚焦 LLM 工程里最核心的训练侧工作：后训练、微调、对齐、推理增强、评测、数据与训练系统。它刻意不做 AI 应用工作流，也不做产品 agent 工具箱。

## 为什么做这个

高价值的算法工程知识仍然分散在很多地方：

- 论文
- 训练仓库
- notebook
- benchmark 脚本
- issue 讨论串
- 团队内部口口相传的经验

`llm-superpowers` 的目标，是把这些知识压缩成可复用的 skills，让另一个 coding agent 能直接调用。

这个仓库不是：

- 又一个超长 awesome list
- 某个框架的二次封装
- benchmark 排行榜
- AI 应用或产品 agent 工具箱

它想做的是 LLM 算法工程的操作层。

## 适合谁

这个仓库面向这些工作：

- continued pretraining
- SFT
- preference optimization
- reward modeling
- online RL for LLMs
- reasoning post-training
- synthetic training data
- evaluation 与 regression detection
- 分布式训练与推理系统
- paper-to-recipe translation

典型用户包括：

- post-training 工程师
- alignment / reasoning 工程师
- training systems 工程师
- 把论文转成生产实验的 research engineer

## 按运行时安装

按你使用的 agent 运行对应命令。

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

也可以让 Codex 直接抓这个文件：

```text
https://github.com/zhangjunmengyang/llm-superpowers/blob/main/.codex/INSTALL.md
```

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

适合共享 AGENTS 体系或 OpenSkills 兼容运行时：

```bash
npx -y openskills install -u -y https://github.com/zhangjunmengyang/llm-superpowers.git
npx -y openskills sync
```

### 其他运行时

如果你的工具有已知 skills 目录，但仓库里还没有 preset：

```bash
curl -fsSL https://raw.githubusercontent.com/zhangjunmengyang/llm-superpowers/main/scripts/install.sh | bash -s -- --target-dir /path/to/your/runtime/skills --profile all
```

安装完成后：

1. 阅读 [docs/installation.zh-CN.md](docs/installation.zh-CN.md)。
2. 先用一个 umbrella skill：
   - `llm-posttrain-pipeline` 负责通用 recipe 规划
   - `llm-reasoning-posttrain` 负责 reasoning 类工作
   - `llm-eval-loop` 负责 checkpoint 比较
   - `llm-training-systems` 负责系统瓶颈
3. 只有在 lead skill 把问题框住以后，再拉一个 specialist module 进来。
4. 用 [examples/README.zh-CN.md](examples/README.zh-CN.md) 里的例子复制起始 prompt。
5. 如果你的运行时还不支持 skill discovery，就按 [docs/runtime-patterns.zh-CN.md](docs/runtime-patterns.zh-CN.md) 里的 fallback 方式用。

如果你只想先拿一个第一条 prompt，直接从这个开始：

```text
Use $llm-posttrain-pipeline to decide the next post-training stage for this model, recommend the best open-source framework, and define the minimum dataset and eval plan.
```

如果你想让第一次会话更稳，先看：

- [docs/first-session.zh-CN.md](docs/first-session.zh-CN.md)
- [docs/runtime-patterns.zh-CN.md](docs/runtime-patterns.zh-CN.md)
- [examples/README.zh-CN.md](examples/README.zh-CN.md)

## 分发模型

这个仓库现在支持三种开源分发方式：

- `superpowers` 风格的 bootstrap：见 [.codex/INSTALL.md](.codex/INSTALL.md)
- 直接一条命令安装：见 [scripts/install.sh](scripts/install.sh)
- 通过 OpenSkills 做通用 repo 安装

这让它既能服务 Codex 这类原生工作流，也能覆盖更广的跨工具 skill loader。

## 运行时矩阵

每个 agent 的安装命令、目标目录和备注，见 [docs/runtime-matrix.zh-CN.md](docs/runtime-matrix.zh-CN.md)。

## 顶层设计

这个仓库假设，算法工程师日常大致只会落在四种工作模式里：

1. 决定下一步该跑什么。
2. 设计数据或 recipe。
3. 判断改动是否真的有效。
4. 排查失败原因。

仓库结构就是围绕这四种模式设计的。

### Skill 分层

- Strategy skills
  - 负责阶段、算法、框架与实验计划
- Execution skills
  - 负责数据、reasoning recipe 与复现计划
- Judgment skills
  - 负责评测门槛与 baseline 对比
- Systems skills
  - 负责内存、吞吐、稳定性与服务瓶颈

### 双层架构

- umbrella skills
  - 负责宽工作模式的主导
  - 负责方向、阶段与 skill 组合
- specialist modules
  - 负责更窄的算法子问题
  - 把某个环节做实

### 组合原则

优先用一个 lead skill，外加最多一到两个 support skills。

例如：

- 新的 alignment 方案：
  - lead: `llm-posttrain-pipeline`
  - support: `llm-synthetic-data`, `llm-eval-loop`
- reasoning 增强：
  - lead: `llm-reasoning-posttrain`
  - support: `llm-synthetic-data`, `llm-eval-loop`
- 论文复现：
  - lead: `llm-research-to-recipe`
  - support: `llm-posttrain-pipeline`, `llm-training-systems`
- 扩展到大规模后出问题：
  - lead: `llm-training-systems`
  - support: `llm-eval-loop`

## 当前 skills

| Skill | 核心职责 | 什么时候先用 | 常见 hand-off |
| --- | --- | --- | --- |
| `llm-posttrain-pipeline` | 选择阶段、算法与框架 | 你还没决定该跑哪条 recipe | `llm-synthetic-data`, `llm-eval-loop` |
| `llm-synthetic-data` | 设计可复用训练数据 | 瓶颈在数据质量、schema 或 preference 构造 | `llm-posttrain-pipeline`, `llm-reasoning-posttrain` |
| `llm-reasoning-posttrain` | 设计 reasoning、verifier、PRM 与 RL recipe | 目标是 reasoning correctness，而不是通用对齐 | `llm-synthetic-data`, `llm-eval-loop` |
| `llm-eval-loop` | 定义 benchmark 方案与 acceptance gate | 你需要比较 baseline vs candidate，或定义能不能过线 | `llm-posttrain-pipeline`, `llm-training-systems` |
| `llm-training-systems` | 排查规模、内存、吞吐与稳定性问题 | 问题主要是系统行为而不是算法选择 | `llm-eval-loop` |
| `llm-research-to-recipe` | 把论文和 repo 转成可运行 recipe | 你要从研究里抽出真正能落地的工程方案 | `llm-posttrain-pipeline`, `llm-training-systems` |

## Specialist Modules

第一批 V1 specialist modules：

| Module | 核心职责 | 常见 umbrella lead |
| --- | --- | --- |
| `sft-recipe-design` | 设计强 SFT recipe | `llm-posttrain-pipeline` |
| `preference-optimization` | 选择和设计离线 preference 方法 | `llm-posttrain-pipeline` |
| `reward-modeling` | 构建和校验 reward signal | `llm-posttrain-pipeline` |
| `online-rl-posttraining` | 设计 rollout 型 RL recipe | `llm-posttrain-pipeline` |
| `reasoning-prm-verifier` | 构建 reasoning 的 process supervision | `llm-reasoning-posttrain` |
| `data-curation-and-filtering` | 做训练数据清洗与过滤 | `llm-synthetic-data` |
| `eval-and-regression-gates` | 把评测转成发布或回滚决策 | `llm-eval-loop` |
| `training-systems-debug` | 安全地排查具体系统故障 | `llm-training-systems` |

## 工作场景

这个仓库主要针对这些高频问题：

- “我们想让底模适配一个新领域，第一步该做 CPT、SFT 还是 DPO？”
- “DPO demo 看起来变好了，但 safety 和 reasoning 回退了。”
- “我们要做 math 或 code 的 reasoning 数据，是不是需要 PRM、verifier 或 best-of-n？”
- “这篇 paper 很强，但最小 faithful reproduction 是什么？便宜版近似怎么做？”
- “训练 OOM 或吞吐掉得很厉害，这是系统问题还是 recipe 问题？”
- “我们有多个 checkpoint，应该怎么设计可信的评测闭环？”

详细映射见：

- [docs/work-scenarios.zh-CN.md](docs/work-scenarios.zh-CN.md)
- [docs/default-workflows.zh-CN.md](docs/default-workflows.zh-CN.md)
- [docs/design-principles.zh-CN.md](docs/design-principles.zh-CN.md)
- [docs/module-map.zh-CN.md](docs/module-map.zh-CN.md)
- [docs/installation.zh-CN.md](docs/installation.zh-CN.md)
- [docs/runtime-patterns.zh-CN.md](docs/runtime-patterns.zh-CN.md)
- [docs/first-session.zh-CN.md](docs/first-session.zh-CN.md)
- [examples/README.zh-CN.md](examples/README.zh-CN.md)

## 仓库结构

```text
llm-superpowers/
├── README.md
├── README.zh-CN.md
├── .codex/
│   ├── INSTALL.md
│   └── INSTALL.zh-CN.md
├── scripts/
│   ├── install.py
│   └── install.sh
├── docs/
│   ├── design-principles.md
│   ├── design-principles.zh-CN.md
│   ├── work-scenarios.md
│   ├── work-scenarios.zh-CN.md
│   ├── default-workflows.md
│   ├── default-workflows.zh-CN.md
│   ├── first-session.md
│   ├── first-session.zh-CN.md
│   ├── module-map.md
│   ├── module-map.zh-CN.md
│   ├── installation.md
│   ├── installation.zh-CN.md
│   ├── runtime-matrix.md
│   ├── runtime-matrix.zh-CN.md
│   ├── runtime-patterns.md
│   └── runtime-patterns.zh-CN.md
├── examples/
│   ├── README.md
│   ├── README.zh-CN.md
│   ├── new-posttrain-plan.md
│   ├── new-posttrain-plan.zh-CN.md
│   ├── synthetic-data-plan.md
│   ├── synthetic-data-plan.zh-CN.md
│   ├── reasoning-improvement.md
│   ├── reasoning-improvement.zh-CN.md
│   ├── regression-triage.md
│   ├── regression-triage.zh-CN.md
│   ├── systems-bottleneck.md
│   ├── systems-bottleneck.zh-CN.md
│   ├── paper-to-recipe.md
│   └── paper-to-recipe.zh-CN.md
└── skills/
    ├── data-curation-and-filtering/
    ├── eval-and-regression-gates/
    ├── llm-posttrain-pipeline/
    ├── llm-synthetic-data/
    ├── llm-reasoning-posttrain/
    ├── llm-eval-loop/
    ├── llm-training-systems/
    ├── llm-research-to-recipe/
    ├── online-rl-posttraining/
    ├── preference-optimization/
    ├── reasoning-prm-verifier/
    ├── reward-modeling/
    ├── sft-recipe-design/
    └── training-systems-debug/
```

每个 skill 目录里都包含：

- `SKILL.md`
- `agents/openai.yaml`
- `references/`

## 设计原则

- framework-agnostic
- open-source first
- operational over academic
- narrow but high-leverage
- reusable across repositories
- optimized for training and post-training work
- explicit about boundaries between skills

## 公开基础

这个包主要参考了这些强公开项目：

- [anthropics/skills](https://github.com/anthropics/skills)
- [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs)
- [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills)
- [huggingface/trl](https://github.com/huggingface/trl)
- [OpenRLHF/OpenRLHF](https://github.com/OpenRLHF/OpenRLHF)
- [volcengine/verl](https://github.com/volcengine/verl)
- [huggingface/open-r1](https://github.com/huggingface/open-r1)
- [allenai/open-instruct](https://github.com/allenai/open-instruct)
- [pytorch/torchtune](https://github.com/pytorch/torchtune)
- [OpenAccess-AI-Collective/axolotl](https://github.com/OpenAccess-AI-Collective/axolotl)

## 路线图

### V0

搭出最小可用核心：

- post-training pipeline selection
- synthetic data patterns
- reasoning 与 PRM recipes
- evaluation loops
- training systems debugging
- paper-to-recipe extraction

### V1

补齐更锋利的算法模块：

- `sft-recipe-design`
- `preference-optimization`
- `reward-modeling`
- `online-rl-posttraining`
- `reasoning-prm-verifier`
- `data-curation-and-filtering`
- `eval-and-regression-gates`
- `training-systems-debug`

### V2

继续往更深的算法工程覆盖扩展：

- data mixture design
- decontamination 与 leakage checks
- long-context post-training
- distillation 与 model merging
- rejection sampling 与 best-of-n pipelines
- curriculum 与 staged post-training
- reward shaping 与 judge design
- scaling-law-aware recipe selection

### V3

把这个仓库打磨成真正成熟的独立项目：

- 更完整的运行时安装文档
- 更清晰的 skill packaging conventions
- cross-framework examples
- skill 质量测试与验证
- papers / GitHub / datasets / experiments 的可选 MCP 集成

## 近期新增方向

下一批最值得补的 skills：

- `long-context-posttraining`
- `distillation-and-merging`
- `data-mixture-design`
- `judge-and-reward-shaping`

## 非目标

- 绑定某一个框架
- 绑定某一个代码库
- 把算法训练 skills 和产品 agent skills 混在一起
- 取代框架官方文档或学术论文

## 当前状态

这已经是一个早期但真实可用的起点。

下一次真正的质量跃迁，不是继续扩类别，而是继续强化边界、场景覆盖和 skill 间的工作流组合。

## 开源基础

仓库当前已经包含：

- [LICENSE](LICENSE)
- [CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md)
- [docs/installation.zh-CN.md](docs/installation.zh-CN.md)
