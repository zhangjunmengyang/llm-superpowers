# Design Principles

This document explains the operating philosophy of `llm-superpowers`.

## Core Claim

The repository should compress experiment discipline, not topic coverage.

If a file does not help an agent:

- decide the next run
- measure a candidate against a baseline
- triage an operational failure
- translate research into a runnable recipe
- record a keep or discard decision

then it probably does not belong in the critical path.

## Repository Architecture

The repository has three layers:

1. Programs
   - operating loops with start gates, artifacts, escalation paths, and success conditions
2. Skills
   - sharp local procedures that solve one decision problem well
3. Templates
   - durable artifacts such as experiment cards, eval boards, triage boards, and ledgers

Programs own orchestration.
Skills do not.

## What A Good Skill Must Do

A strong skill makes all of these explicit:

- when it should trigger
- when it should not lead
- what inputs matter first
- what artifact it should produce
- what hard rules must not be broken
- what decision standard applies

If a skill reads like a category card, it is too weak.
If it owns a whole workflow, it is too broad.

## What A Good Program Must Do

A strong program defines:

- required artifacts before the loop starts
- the canonical loop itself
- escalation points into other programs
- what healthy output looks like

Programs are where the repository should feel opinionated.

## Non-Negotiable Experiment Rules

- every serious run has a named baseline
- every first isolating run changes one coherent surface only
- every comparison freezes prompts, datasets, and decoding
- every candidate leaves behind a durable artifact trail
- every promotion decision is one of: keep, discard, crash, investigate
- every keep decision reviews failures, not averages only
- every systems fix gets a quality comparability check
- every paper reproduction names irreducibles, approximation, and kill criteria

## Design Direction

Future additions should mostly be:

- sharper modules around real failure modes
- better artifact contracts
- better review checklists
- better operating boards

Future additions should not mostly be:

- more labels
- more taxonomies
- bigger benchmark lists
- more framework name-dropping without decision logic
