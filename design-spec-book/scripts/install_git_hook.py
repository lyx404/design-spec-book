#!/usr/bin/env python3
"""Install an optional pre-commit bridge for design-spec-book."""

from __future__ import annotations

import argparse
import shlex
import subprocess
import sys
from pathlib import Path


MARKER = "# design-spec-book:pre-commit"


def git_dir(project_root: Path) -> Path:
    result = subprocess.run(
        ["git", "-C", str(project_root), "rev-parse", "--git-dir"],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        raise RuntimeError("目标目录不是 Git 仓库")
    value = Path(result.stdout.strip())
    return value if value.is_absolute() else (project_root / value).resolve()


def hook_block(project_root: Path, policy: str) -> str:
    script = Path(__file__).resolve().with_name("sync_design_docs.py")
    command = [
        sys.executable,
        str(script),
        "--project-root",
        str(project_root),
        "--mode",
        "passive",
        "--quiet-minutes",
        "0",
    ]
    if policy == "warn":
        command.append("--report-only")
    rendered = " ".join(shlex.quote(item) for item in command)
    lines = [
        MARKER,
        f"{rendered}",
        "status=$?",
        'if [ "$status" -eq 3 ]; then',
        '  echo "设计说明书待同步：请先收敛设计文档，或使用 design-spec-book 手动同步。" >&2',
        "  exit 1",
        "fi",
        'if [ "$status" -ne 0 ]; then exit "$status"; fi',
        "# design-spec-book:end",
    ]
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="安装 design-spec-book 的可选 Git pre-commit 钩子")
    parser.add_argument("--project-root", type=Path, default=Path.cwd())
    parser.add_argument("--policy", choices=("warn", "auto"), default="warn")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    project_root = args.project_root.expanduser().resolve()
    if not project_root.is_dir():
        print(f"错误：项目根目录不存在：{project_root}", file=sys.stderr)
        return 2
    try:
        hook_path = git_dir(project_root) / "hooks" / "pre-commit"
    except RuntimeError as error:
        print(f"错误：{error}", file=sys.stderr)
        return 2

    hook_path.parent.mkdir(parents=True, exist_ok=True)
    existing = hook_path.read_text(encoding="utf-8", errors="ignore") if hook_path.exists() else "#!/bin/sh\n"
    if MARKER in existing:
        print(f"已存在 design-spec-book 钩子：{hook_path}")
        return 0
    separator = "" if existing.endswith("\n") else "\n"
    hook_path.write_text(existing + separator + hook_block(project_root, args.policy), encoding="utf-8")
    hook_path.chmod(hook_path.stat().st_mode | 0o111)
    print(f"已安装 Git pre-commit 钩子（{args.policy}）：{hook_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
