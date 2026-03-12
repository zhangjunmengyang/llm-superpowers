# 工作场景

这个文档把常见的 LLM 算法工程场景映射到正确的 lead skill。

## 场景矩阵

| 场景 | Lead skill | Support skills | 期望输出 |
| --- | --- | --- | --- |
| 新领域适配方案 | `llm-posttrain-pipeline` | `sft-recipe-design`, `llm-eval-loop` | 阶段选择、recipe、指标 |
| 已有模型上做 DPO 还是 RL | `llm-posttrain-pipeline` | `preference-optimization`, `reward-modeling`, `online-rl-posttraining` | 算法选择与 scale-up 路线 |
| 构建 preference 数据集 | `llm-synthetic-data` | `data-curation-and-filtering`, `preference-optimization` | schema、生成路径、filters |
| 构建 reasoning traces 或 PRM labels | `llm-reasoning-posttrain` | `reasoning-prm-verifier`, `llm-synthetic-data`, `llm-eval-loop` | trace schema、reward 或 verifier 方案 |
| 复现 R1 风格或 reasoning 论文 | `llm-research-to-recipe` | `llm-reasoning-posttrain`, `reasoning-prm-verifier`, `llm-posttrain-pipeline` | faithful recipe 与便宜近似版 |
| 比较多个 checkpoints | `llm-eval-loop` | `llm-posttrain-pipeline` | benchmark 方案、pass/fail 标准 |
| 对齐后出现 safety regression | `llm-eval-loop` | `llm-posttrain-pipeline`, `preference-optimization`, `reward-modeling` | regression 诊断与下一轮实验 |
| OOM、发散或吞吐崩掉 | `llm-training-systems` | `llm-eval-loop` | bottleneck 假设与修复顺序 |
| 扩大一个 proof-of-life 实验 | `llm-training-systems` | `llm-posttrain-pipeline`, `sft-recipe-design` 或 `online-rl-posttraining` | 系统方案与可回滚 scale-up 路线 |
| 把新论文转成内部实验 | `llm-research-to-recipe` | `llm-posttrain-pipeline`、一个 specialist module、`llm-eval-loop` | 可执行 recipe 与验证计划 |

## 场景说明

### 1. 选择第一条 recipe

当问题还停留在 strategy 层时，先用 `llm-posttrain-pipeline`。

典型问题：

- 第一阶段是 SFT 还是 DPO
- 需不需要 reward model
- rejection sampling 够不够
- TRL、veRL、OpenRLHF 该先选哪个

### 2. 修数据

当瓶颈明确是数据质量、schema 不匹配、负样本质量或 reasoning labels 质量时，先用 `llm-synthetic-data`。

典型问题：

- 怎么做高质量 DPO pairs
- reward model 数据集应该长什么样
- synthetic reasoning traces 应该怎么组织

然后再引入：

- `data-curation-and-filtering`：当难点在 filtering、dedup 或 contamination
- `preference-optimization`：当 pair 质量本身成了关键问题

### 3. 提升 reasoning

当目标是 reasoning correctness、step 质量、verifier 设计或 R1 风格增强时，先用 `llm-reasoning-posttrain`。

典型问题：

- 需不需要 PRM 或 verifier supervision
- 该用 best-of-n 还是 RL
- reasoning trace schema 应该是什么样

然后再引入：

- `reasoning-prm-verifier`：做 PRM vs verifier 决策
- `online-rl-posttraining`：当 reasoning loop 进入 rollout 阶段时

### 4. 判断改动有没有生效

当仓库里已经有 candidate outputs 或 checkpoints，而主要问题是证据时，先用 `llm-eval-loop`。

典型问题：

- 哪个 benchmark 才可信
- baseline 和 candidate 应该怎么比较
- ship gates 应该怎么定

### 5. 排查系统问题

当主要瓶颈是内存、速度、稳定性或 serving 行为时，先用 `llm-training-systems`。

典型问题：

- 为什么会 OOM
- 为什么吞吐掉了
- 为什么只有放大后才发散
- 要不要切到 FSDP、ZeRO、vLLM 或 SGLang

### 6. 用工程化方式读研究

当主要问题是把研究转成实验计划时，先用 `llm-research-to-recipe`。

典型问题：

- 这篇工作真正的贡献是什么
- faithful reproduction 的最小必要条件是什么
- 本周能跑的便宜近似版是什么

然后再 hand off 给：

- `sft-recipe-design`
- `preference-optimization`
- `reward-modeling`
- `online-rl-posttraining`
- `reasoning-prm-verifier`

具体取决于抽出的 recipe 里真正包含什么。
