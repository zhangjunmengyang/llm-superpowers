# Post-Training Algorithm Heuristics

Use this file when designing the next run, not when writing a survey.

## Start With The Smallest Credible Move

- If the behavior is absent, start with SFT.
- If the behavior exists but the ranking is wrong, try preference optimization.
- If a reusable scalar is needed across many candidates, build a reward model.
- If search is cheap and judging is reliable, try rejection sampling before RL.
- Use online RL only when exploration or trajectory-level credit assignment really matters.

## Default First-Run Bars

These are starting defaults, not laws. Use them when the project does not already have a stronger house standard.

| Signal type | Default bar before scale-up | Investigate or rerun instead when |
| --- | --- | --- |
| Exact match, accuracy, pass rate | at least 1 absolute point or more than 2x observed rerun noise | the delta sits inside the repeatability band |
| Pairwise win rate | roughly 3 to 5 absolute points on a stable slice and no hard blocker regression | judge disagreement is high or coverage is thin |
| Reward-model ranking quality | clear held-out separation between good and bad outputs | reward and human preference disagree in audit samples |
| Safety blocker | no material regression tolerated | any blocker drift appears |
| Cost or latency tradeoff | explain any 15 to 20 percent regression explicitly | quality gains are still inside noise while cost already rose |

## Stage-Specific Stop Rules

- Continued pretraining:
  - stop scaling if a small supervised probe or downstream slice is still flat after the corpus and tokenizer assumptions were checked
- SFT:
  - stop before scale if formatting, instruction following, or domain behavior do not move on a 50 to 100 example held-out slice
- Preference optimization:
  - stop and fix the data if a 50 pair audit shows many ambiguous, contradictory, or low-signal pairs
- Reward modeling:
  - do not feed RL with a reward that visibly disagrees with human ranking on held-out audits
- Rejection sampling or best-of-n:
  - do not scale if wins appear only at very large `n`; that usually means the base model or judge is still too weak
- Online RL:
  - stop and audit reward, rollout, or KL settings if reward rises while the external eval board stays flat for two checkpoints

## Use Continued Pretraining When

- broad domain coverage is missing
- vocabulary or style drift is structural
- instruction tuning alone would be too shallow

## Use SFT When

- the task format is missing
- the model lacks the target interaction pattern
- you need a clean base before preference or RL stages

## Use Preference Optimization When

- chosen and rejected data already exists
- the main issue is preference ranking, not exploration
- a simpler stack than reward-plus-RL is desired

## Use Reward Modeling When

- the signal should be reused across many candidates or stages
- checkpoint ranking or best-of-n matters
- online RL is a serious possibility

## Use Online RL When

- offline methods no longer answer the question
- delayed reward matters
- the task genuinely benefits from exploration

## Use Rejection Sampling Or Best-of-N When

- many candidates can be sampled cheaply
- a reliable judge or verifier exists
- RL would add too much stack complexity for the expected gain

## Use Distillation When

- a stronger teacher or search policy already exists
- latency or cost matters
- deployment simplicity matters more than discovery

## High-Value Failure Signatures

- Nicer style, worse correctness:
  - usually preference or reward over-optimizing style signals
- Win rate up, worst slice down:
  - usually judge bias, pair-rubric mismatch, or reward shortcut
- Only self-generated eval improves:
  - usually contamination or distribution overfit
- Formatting suddenly worsens after preference tuning:
  - often prompt-boundary or truncation bugs, not algorithm choice
- Gains only on easy slices:
  - usually data coverage holes, not a fundamentally stronger recipe
- Reward rises while humans dislike outputs:
  - reward model shortcut or rollout exploit

## Cheap Audits Before Large Runs

- Review 20 to 50 real examples before a large preference or reward run.
- Freeze one tiny smoke set that gets rerun after every systems change.
- Write the smallest meaningful delta before launching the first serious run.
- If the baseline itself is weak or unstable, fix that first instead of adding another stage.

## Anti-Patterns

- using RL to fix formatting or templating
- changing algorithm and dataset at the same time in the same first run
- using DPO-like methods on contradictory preference labels
- trusting reward models without held-out validation
- evaluating only on synthetic prompts from the same generator
