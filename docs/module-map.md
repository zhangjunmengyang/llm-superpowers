# Module Map

This document maps programs to the skills and artifacts that actually support them.

## Program To Skill Map

| Program | Lead skills | Must leave behind |
| --- | --- | --- |
| `experiment-loop` | `llm-posttrain-pipeline`, `llm-synthetic-data`, `llm-eval-loop`, `run-ledger-and-keep-discard` | experiment card, `results.tsv`, explicit keep/discard decision |
| `eval-board` | `llm-eval-loop`, `checkpoint-regression-triage` | eval board, failure slices, promotion decision |
| `systems-war-room` | `llm-training-systems`, `throughput-and-oom-triage`, `llm-eval-loop` | systems triage board, one-axis intervention plan, quality recheck |
| `research-to-experiment` | `llm-research-to-recipe`, `llm-posttrain-pipeline` | reproduction plan, irreducibles, first runnable experiment |

## Optional Deepening Modules

Use these only when the main loop has already exposed the narrower problem:

- `llm-reasoning-posttrain`
- `sft-recipe-design`
- `preference-optimization`
- `reward-modeling`
- `online-rl-posttraining`
- `reasoning-prm-verifier`
- `data-curation-and-filtering`
- `eval-and-regression-gates`
- `training-systems-debug`

## Rule

If the question is about sequence, escalation, or artifact flow, it belongs to a program.

If the question is about one sharp decision problem, it belongs to a skill.
