# 贡献指南

[English](CONTRIBUTING.md) | 简体中文

## 目标

所有贡献都应该让 `llm-superpowers` 更贴近真实的 LLM 算法工程工作。

好的贡献通常会做这些事之一：

- 把已有 skill 的边界切得更准
- 提升场景覆盖
- 新增一个职责明确的 specialist module
- 改进 references 或 hand-off 逻辑
- 提升安装体验或运行时兼容性

## 需要避免的事

- 只加大类名字，不加可执行内容
- 把 AI 应用 / 产品 agent 工作流混进算法训练 skills
- skill 应该很锋利，却塞进一大堆综述
- 把框架官方文档整段搬进仓库

## Skill 质量标准

每个 skill 都应把这些点讲清楚：

- 什么时候该触发
- 什么时候不该 lead
- 应该产出什么结果
- 应该 hand off 给哪些邻近 skills

## 建议的贡献流程

1. 先开 issue 或 draft PR，说明这个新 skill 解决的具体工作是什么。
2. 说明现有哪个 skill 太宽，或者哪里还缺失。
3. 保持 skill 足够窄。
4. 只有在能提升行动性的情况下再补 references。
5. 对改过的 skill 跑验证。

## 验证

对任何改过的 skill 目录，都用 Codex skill toolkit 里的 validator 跑一遍：

```bash
python /path/to/quick_validate.py /path/to/skill-folder
```

## 命名

- 只用小写字母、数字和连字符
- 名字要描述真实工作，而不是抽象主题
- 除非确实需要 umbrella，否则优先新增 specialist module
