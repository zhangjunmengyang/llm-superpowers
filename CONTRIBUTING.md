# Contributing

## Goal

Contributions should make `llm-superpowers` more useful for real LLM algorithm-engineering work.

Good contributions usually do one of these:

- sharpen an existing skill boundary
- improve scenario coverage
- add a specialist module with a clear job
- improve references or hand-off logic
- improve installation or runtime compatibility

## What To Avoid

- adding broad category names with no operational content
- mixing product-agent workflows into algorithm-training skills
- adding large surveys where a skill should stay sharp
- copying framework docs into the repository

## Skill Quality Standard

Every skill should make these points clear:

- when it should trigger
- when it should not lead
- what output it should produce
- which neighboring skills it should hand off to

## Preferred Contribution Process

1. Open an issue or draft a PR explaining the job the new skill solves.
2. Show which existing skill is too broad or missing.
3. Keep the skill narrow.
4. Add or update references only when they improve actionability.
5. Run validation on the changed skills.

## Validation

Use the validator from the Codex skill toolkit on any changed skill folder:

```bash
python /path/to/quick_validate.py /path/to/skill-folder
```

## Naming

- use lowercase letters, digits, and hyphens only
- prefer names that describe an actual job
- prefer specialist modules over vague umbrellas unless a true umbrella is needed
