# Runtime Integration Patterns

This repository is intentionally runtime-agnostic.

The goal is to make the skill pack usable across different coding-agent environments without tying it to one product UI or one vendor-specific setup flow.

## The Stable Contract

Every runtime integration should preserve the same basic contract:

- each skill lives in its own folder under `skills/`
- each skill exposes `SKILL.md`
- each skill exposes `agents/openai.yaml`
- each skill can load extra material from `references/`

If a runtime can discover folders that follow that contract, it can usually consume this repository with little extra glue.

## Recommended Integration Patterns

If you want a single install command instead of manual setup, use [../scripts/install.sh](../scripts/install.sh).
If your environment supports OpenSkills, use `npx -y openskills install -u -y https://github.com/zhangjunmengyang/llm-superpowers.git`.
If you just want the runtime-specific commands, see [runtime-matrix.md](runtime-matrix.md).

### 1. Direct Folder Discovery

Use this when your runtime can read skills from any local directory.

Point the runtime at:

```text
<repo-root>/skills
```

This is the cleanest option because:

- upstream updates stay intact
- no files need to be copied
- skill boundaries stay visible

If the runtime already exposes a stable local skill directory, the installer can target it directly with a preset such as `--runtime codex`.
The current presets are `claude-code`, `claude-code-project`, `codex`, `opencode`, `opencode-project`, and `openclaw`.

### 2. Selective Symlink Install

Use this when your runtime expects skills in a dedicated home directory.

Keep the repository cloned once, then symlink only the skills you actually want:

```bash
SKILLS_HOME="${SKILLS_HOME:-$HOME/.codex/skills}"
mkdir -p "$SKILLS_HOME"

ln -s /path/to/llm-superpowers/skills/llm-posttrain-pipeline "$SKILLS_HOME/llm-posttrain-pipeline"
ln -s /path/to/llm-superpowers/skills/llm-eval-loop "$SKILLS_HOME/llm-eval-loop"
ln -s /path/to/llm-superpowers/skills/sft-recipe-design "$SKILLS_HOME/sft-recipe-design"
```

Why this is usually better than copying:

- updates are easier
- local customizations are explicit
- the repository stays the single source of truth

The installer can do this for you:

```bash
./scripts/install.sh --target-dir /path/to/runtime/skills --profile starter --mode symlink
```

### 3. Vendored Internal Dependency

Use this when a team wants to consume the pack from an internal monorepo.

Typical approaches:

- add the repository as a submodule
- mirror the `skills/` directory into an internal repo
- pin a specific commit in internal tooling

This is the right pattern when:

- reproducibility matters
- multiple engineers should share the same skill revision
- internal wrappers or governance need a frozen dependency

### 3.5. Universal Repo Installer

Use this when your environment already supports OpenSkills-style distribution.

Install with:

```bash
npx -y openskills install -u -y https://github.com/zhangjunmengyang/llm-superpowers.git
npx -y openskills sync
```

This works well when:

- the runtime reads `.agent/skills`
- you want GitHub-repo installation instead of custom shell scripts
- you want a package-manager-like install story for skills

### 4. Prompt-Only Fallback

Use this when your runtime does not support skill discovery yet.

In that case:

1. open the relevant skill folder
2. read `SKILL.md`
3. copy one of the starter prompts from [../examples/README.md](../examples/README.md)
4. use the expected output shape from the example as your response contract

This is weaker than native skill loading, but still enough to make the repository useful.

## First Install Recommendation

For a new user, start with only these skills:

- `llm-posttrain-pipeline`
- `llm-eval-loop`
- `llm-reasoning-posttrain`
- `sft-recipe-design`
- `preference-optimization`
- `training-systems-debug`

That set covers most early post-training work without overloading the runtime with too many neighbors.

## Upgrade Discipline

When updating the repository in a real workflow:

1. pin a commit before large experiments
2. pull upstream changes into a clean branch
3. smoke-test one known prompt from [../examples/README.md](../examples/README.md)
4. add new skills gradually instead of exposing everything at once

## What Not To Do

- do not flatten all skills into one giant file
- do not rename skill folders casually after downstream adoption
- do not load many umbrella skills as peers in the same prompt
- do not treat the examples as framework-specific recipes
