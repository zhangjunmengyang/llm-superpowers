# Work Scenarios

This document maps common LLM algorithm-engineering situations to the right operating loop.

## Scenario Matrix

| Scenario | Program | Lead skill | Must produce | Escalate if needed |
| --- | --- | --- | --- | --- |
| New domain adaptation run | `experiment-loop` | `llm-posttrain-pipeline` | experiment card | `llm-synthetic-data`, `llm-eval-loop` |
| Building a synthetic SFT, DPO, or RM dataset | `experiment-loop` | `llm-synthetic-data` | data product spec | `data-curation-and-filtering` |
| Comparing baseline vs candidate | `eval-board` | `llm-eval-loop` | eval board | `checkpoint-regression-triage` |
| Safety or quality regression after alignment | `eval-board` | `llm-eval-loop` | failure slices plus decision | `checkpoint-regression-triage`, `llm-posttrain-pipeline` |
| OOM or throughput collapse | `systems-war-room` | `llm-training-systems` | systems triage board | `throughput-and-oom-triage` |
| Divergence or instability at scale | `systems-war-room` | `llm-training-systems` | one-axis intervention plan | `throughput-and-oom-triage`, `llm-eval-loop` |
| Translating a paper into the first run | `research-to-experiment` | `llm-research-to-recipe` | reproduction plan | `llm-posttrain-pipeline` |
| Reasoning improvement | `experiment-loop` | `llm-reasoning-posttrain` | reasoning experiment card | `reasoning-prm-verifier`, `llm-eval-loop` |

## Rule Of Thumb

- if the task starts with “what should we run next,” start from `experiment-loop`
- if the task starts with “did this checkpoint actually improve,” start from `eval-board`
- if the task starts with “this run is invalid,” start from `systems-war-room`
- if the task starts with “what is the real recipe in this paper,” start from `research-to-experiment`
