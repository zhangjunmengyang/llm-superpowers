# Design Principles

This document explains how `llm-superpowers` is supposed to be used and how future skills should be designed.

## Core Assumption

An LLM algorithm engineer is usually not asking for generic help.

They are usually trying to do one of a small number of concrete jobs:

- choose the right training stage
- build or fix a dataset
- improve reasoning behavior
- evaluate a model change
- debug a failed run
- turn research into an experiment

The repository should be optimized for those jobs, not for broad topic coverage.

## What A Skill Is

A skill in this repository is not:

- a tutorial
- a long survey
- a framework wrapper
- a product workflow

A skill is an operational decision aid for a specific type of algorithm-engineering work.

It should help another coding agent answer:

1. Is this the right skill to lead with?
2. What should be decided first?
3. What should be produced as output?
4. Which neighboring skill should take over next?

## Repository Architecture

The current architecture has four layers.

### 1. Strategy

Used when the problem is “what should we run?”

Skills:

- `llm-posttrain-pipeline`
- `llm-research-to-recipe`

### 2. Execution

Used when the problem is “what data or recipe do we need?”

Skills:

- `llm-synthetic-data`
- `llm-reasoning-posttrain`

### 3. Judgment

Used when the problem is “did it work?”

Skills:

- `llm-eval-loop`

### 4. Systems

Used when the problem is “why did the run fail or slow down?”

Skills:

- `llm-training-systems`

## Skill Boundary Rules

- `llm-posttrain-pipeline` chooses stage and algorithm. It should not become a deep data-crafting skill.
- `llm-synthetic-data` designs data schemas and generation paths. It should not become a framework-selection skill.
- `llm-reasoning-posttrain` is only for reasoning-specific improvement loops.
- `llm-eval-loop` defines evidence and acceptance gates. It should not turn into a broad benchmarking encyclopedia.
- `llm-training-systems` handles systems bottlenecks, not algorithm choice.
- `llm-research-to-recipe` translates papers and repos into runnable artifacts, not full experiment execution.

## Composition Rules

Prefer one lead skill and one or two supporting skills.

Good:

- `llm-posttrain-pipeline` -> `llm-synthetic-data` -> `llm-eval-loop`
- `llm-research-to-recipe` -> `llm-posttrain-pipeline`
- `llm-reasoning-posttrain` -> `llm-eval-loop`
- `llm-training-systems` -> `llm-eval-loop`

Bad:

- invoking four or five skills as peers without a lead
- using `llm-training-systems` before deciding whether the recipe is even correct
- using `llm-eval-loop` before defining the baseline and target behavior

## Quality Bar For A Good Skill

A strong skill should make the following clear:

- when it should trigger
- when it should not lead
- what output it should produce
- what neighboring skills it hands off to

If a skill reads like a category label instead of an operating primitive, it is too broad.

## Design Direction

The long-term direction is to move from broad umbrellas to sharper algorithm modules.

That means future work should mostly be:

- splitting broad skills
- improving boundaries
- adding scenario coverage
- adding better default outputs

It should not mostly be:

- adding more topic names
- chasing every new benchmark
- mixing product engineering and training engineering
