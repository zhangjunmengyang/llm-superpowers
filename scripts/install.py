#!/usr/bin/env python3

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / "skills"

STARTER_PROFILE = [
    "llm-posttrain-pipeline",
    "llm-synthetic-data",
    "llm-eval-loop",
    "llm-training-systems",
    "llm-research-to-recipe",
    "run-ledger-and-keep-discard",
    "checkpoint-regression-triage",
    "throughput-and-oom-triage",
]

RUNTIME_DIRS = {
    "claude-code": lambda: Path.home() / ".claude" / "skills",
    "claude-code-project": lambda: Path.cwd() / ".claude" / "skills",
    "codex": lambda: Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))) / "skills",
    "opencode": lambda: Path.home() / ".config" / "opencode" / "skills",
    "opencode-project": lambda: Path.cwd() / ".opencode" / "skills",
    "openclaw": lambda: Path.home() / ".openclaw" / "workspace" / "skills",
}


def find_skill_dirs() -> dict[str, Path]:
    skills: dict[str, Path] = {}
    for entry in sorted(SKILLS_ROOT.iterdir()):
        if entry.is_dir() and (entry / "SKILL.md").exists():
            skills[entry.name] = entry
    return skills


def resolve_runtime_dir(runtime: str | None) -> Path | None:
    if runtime is None:
        return None
    if runtime in RUNTIME_DIRS:
        return RUNTIME_DIRS[runtime]()
    raise ValueError(f"unsupported runtime preset: {runtime}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install llm-superpowers skills into a runtime skills directory."
    )
    parser.add_argument(
        "--runtime",
        choices=sorted(RUNTIME_DIRS),
        help="Known runtime preset. Use --target-dir for any other tool.",
    )
    parser.add_argument(
        "--target-dir",
        type=Path,
        help="Explicit skills directory for runtimes without a preset.",
    )
    parser.add_argument(
        "--profile",
        choices=["starter", "all"],
        default="starter",
        help="Install a curated starter pack or the full repository.",
    )
    parser.add_argument(
        "--skill",
        action="append",
        default=[],
        help="Install only these skills. Can be repeated.",
    )
    parser.add_argument(
        "--mode",
        choices=["auto", "symlink", "copy"],
        default="auto",
        help="Install mode. auto tries symlink first, then falls back to copy.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace existing installations for the selected skills.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the plan without changing anything.",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available skills and exit.",
    )
    return parser.parse_args()


def plan_skill_names(args: argparse.Namespace, available: dict[str, Path]) -> list[str]:
    if args.skill:
        names = args.skill
    elif args.profile == "all":
        names = sorted(available)
    else:
        names = STARTER_PROFILE

    missing = [name for name in names if name not in available]
    if missing:
        raise SystemExit(f"unknown skills: {', '.join(missing)}")
    return names


def ensure_target_dir(args: argparse.Namespace) -> Path:
    if args.target_dir and args.runtime:
        raise SystemExit("use either --runtime or --target-dir, not both")

    target_dir = args.target_dir or resolve_runtime_dir(args.runtime)
    if target_dir is None:
        raise SystemExit(
            "choose --runtime "
            + "|".join(sorted(RUNTIME_DIRS))
            + " or pass --target-dir"
        )
    return target_dir.expanduser().resolve()


def remove_existing(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
        return
    shutil.rmtree(path)


def copy_skill(src: Path, dest: Path) -> str:
    shutil.copytree(src, dest, symlinks=True)
    return "copy"


def symlink_skill(src: Path, dest: Path) -> str:
    dest.symlink_to(src, target_is_directory=True)
    return "symlink"


def install_one(src: Path, dest: Path, mode: str) -> str:
    if mode == "copy":
        return copy_skill(src, dest)
    if mode == "symlink":
        return symlink_skill(src, dest)
    try:
        return symlink_skill(src, dest)
    except OSError:
        return copy_skill(src, dest)


def main() -> int:
    args = parse_args()
    available = find_skill_dirs()

    if args.list:
        for name in available:
            print(name)
        return 0

    skill_names = plan_skill_names(args, available)
    target_dir = ensure_target_dir(args)

    print(f"Repository: {REPO_ROOT}")
    print(f"Target dir: {target_dir}")
    print(f"Requested skills ({len(skill_names)}): {', '.join(skill_names)}")
    print(f"Install mode: {args.mode}")

    if args.dry_run:
        return 0

    target_dir.mkdir(parents=True, exist_ok=True)

    installed: list[tuple[str, str, str]] = []
    for name in skill_names:
        src = available[name]
        dest = target_dir / name
        if dest.exists() or dest.is_symlink():
            if not args.force:
                print(f"skip {name}: already exists at {dest}")
                continue
            remove_existing(dest)

        actual_mode = install_one(src, dest, args.mode)
        installed.append((name, actual_mode, str(dest)))
        print(f"installed {name} via {actual_mode} -> {dest}")

    if not installed:
        print("nothing changed")
        return 0

    print("")
    print("Next step:")
    print("- restart or reload your runtime if it caches skill directories")
    print("- open programs/README.md and choose one operating loop")
    print("- start with $llm-posttrain-pipeline or $llm-eval-loop")
    return 0


if __name__ == "__main__":
    sys.exit(main())
