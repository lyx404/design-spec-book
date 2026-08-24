#!/usr/bin/env python3
"""Generate and refresh the six design declaration documents.

The script intentionally makes conservative inferences. It records observable
project facts in a managed block and leaves the rest of each document alone.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Iterable


MARKER_START = "<!-- design-spec:managed:start -->"
MARKER_END = "<!-- design-spec:managed:end -->"
SKIP_DIRS = {
    ".git",
    ".next",
    ".nuxt",
    ".svelte-kit",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "out",
    "target",
    "vendor",
}
TEXT_SUFFIXES = {
    ".css",
    ".html",
    ".js",
    ".jsx",
    ".json",
    ".md",
    ".scss",
    ".ts",
    ".tsx",
    ".vue",
    ".yaml",
    ".yml",
}
DOC_TEMPLATES = {
    "spec.md": "spec.md",
    "domain.md": "domain.md",
    "craft.md": "craft.md",
    "design.md": "design.md",
    "components.md": "components.md",
    "template.md": "template.md",
}
STATE_DIR_NAME = ".design-spec"
STATE_FILE_NAME = "state.json"
DEFAULT_QUIET_MINUTES = 30.0
PENDING_EXIT_CODE = 3


def read_text(path: Path) -> str:
    try:
        if path.stat().st_size > 256 * 1024:
            return ""
        return path.read_text(encoding="utf-8", errors="ignore")
    except (OSError, UnicodeError):
        return ""


def rel(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def iter_project_files(root: Path) -> list[Path]:
    """Read only common source/config directories, with a bounded file list."""

    names = {
        "README.md",
        "README.mdx",
        "package.json",
        "index.html",
        "pubspec.yaml",
        "pyproject.toml",
    }
    files: set[Path] = {path for path in (root / name for name in names) if path.is_file()}
    for path in root.iterdir() if root.is_dir() else ():
        if path.is_file() and path.suffix.lower() in {".css", ".scss", ".html", ".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte"}:
            files.add(path)
        if path.is_file() and (
            path.name.endswith((".config.js", ".config.cjs", ".config.mjs", ".config.ts"))
            or path.name in {"vite.config.ts", "next.config.js", "tailwind.config.js"}
        ):
            files.add(path)

    for dirname in (
        "src",
        "app",
        "pages",
        "routes",
        "components",
        "lib",
        "styles",
        "public",
        "assets",
        "tests",
    ):
        directory = root / dirname
        if not directory.is_dir():
            continue
        for path in directory.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            if any(part in SKIP_DIRS for part in path.parts):
                continue
            files.add(path)
            if len(files) >= 180:
                break
        if len(files) >= 180:
            break
    return sorted(files, key=lambda item: rel(item, root))[:180]


def utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def iso_time(value: dt.datetime) -> str:
    return value.astimezone(dt.timezone.utc).isoformat()


def parse_time(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    try:
        parsed = dt.datetime.fromisoformat(value)
    except ValueError:
        return None
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=dt.timezone.utc)


def file_signature(path: Path) -> dict[str, int | str]:
    try:
        stat = path.stat()
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        return {"mtime_ns": stat.st_mtime_ns, "size": stat.st_size, "sha256": digest}
    except OSError:
        return {}


def project_snapshot(root: Path) -> dict[str, dict[str, int | str]]:
    return {
        rel(path, root): file_signature(path)
        for path in iter_project_files(root)
        if path.is_file()
    }


def state_path(root: Path, state_dir: Path) -> Path:
    return (root / state_dir / STATE_FILE_NAME).resolve()


def load_state(root: Path, state_dir: Path) -> dict:
    path = state_path(root, state_dir)
    if not path.is_file():
        return {"version": 1, "snapshot": {}, "pending": None}
    try:
        value = json.loads(read_text(path))
        return value if isinstance(value, dict) else {"version": 1, "snapshot": {}, "pending": None}
    except json.JSONDecodeError:
        return {"version": 1, "snapshot": {}, "pending": None}


def save_state(root: Path, state_dir: Path, state: dict) -> None:
    path = state_path(root, state_dir)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def affected_documents(changed_files: Iterable[str]) -> set[str]:
    affected: set[str] = set()
    for value in changed_files:
        path = Path(value)
        lower = value.lower()
        parts = {part.lower() for part in path.parts}
        suffix = path.suffix.lower()

        if path.name.lower() in {"package.json", "readme.md", "readme.mdx", "pyproject.toml", "pubspec.yaml"}:
            affected.update(DOC_TEMPLATES)
        if parts & {"app", "pages", "routes"} or path.name.lower() in {"app.tsx", "app.jsx", "main.tsx", "main.jsx", "main.ts", "main.js"}:
            affected.update({"spec.md", "template.md"})
        if "component" in parts or re.search(r"/(?:[A-Z][A-Za-z0-9_-]*\.(?:tsx|jsx|vue|svelte))$", "/" + value):
            affected.update({"components.md", "design.md", "craft.md"})
        if suffix in {".css", ".scss"} or any(marker in lower for marker in ("theme", "token", "tailwind")):
            affected.update({"design.md", "craft.md", "template.md"})
        if any(marker in lower for marker in ("schema", "model", "domain", "permission", "auth", "policy", "api")):
            affected.update({"domain.md", "spec.md"})
        if "test" in parts or suffix in {".spec", ".test"}:
            affected.add("spec.md")

    return affected or set(DOC_TEMPLATES)


def detect_pending(root: Path, state: dict, current_snapshot: dict) -> tuple[list[str], bool]:
    previous_snapshot = state.get("snapshot") or {}
    if not previous_snapshot:
        state["snapshot"] = current_snapshot
        state["initialized_at"] = iso_time(utc_now())
        return [], False

    changed = sorted(
        path for path in set(previous_snapshot) | set(current_snapshot)
        if previous_snapshot.get(path) != current_snapshot.get(path)
    )
    pending = state.get("pending") or None
    if changed:
        prior_files = pending.get("changed_files", []) if pending else []
        all_files = sorted(set(prior_files) | set(changed))
        file_times = []
        for path in all_files:
            candidate = root / path
            if candidate.exists():
                try:
                    file_times.append(dt.datetime.fromtimestamp(candidate.stat().st_mtime, tz=dt.timezone.utc))
                except OSError:
                    pass
        last_change = max(file_times, default=utc_now())
        state["pending"] = {
            "changed_files": all_files,
            "affected_documents": sorted(affected_documents(all_files)),
            "last_change_at": iso_time(last_change),
            "detected_at": iso_time(utc_now()),
        }
    state["snapshot"] = current_snapshot
    return changed, bool(state.get("pending"))


def pending_is_quiet(pending: dict | None, quiet_minutes: float) -> bool:
    if not pending:
        return False
    last_change = parse_time(pending.get("last_change_at"))
    if not last_change:
        return False
    return (utc_now() - last_change).total_seconds() >= quiet_minutes * 60


def load_package(root: Path) -> dict:
    package = root / "package.json"
    if not package.is_file():
        return {}
    try:
        value = json.loads(read_text(package))
        return value if isinstance(value, dict) else {}
    except json.JSONDecodeError:
        return {}


def first_heading(text: str) -> str | None:
    for line in text.splitlines():
        match = re.match(r"^#\s+(.+?)\s*$", line)
        if match:
            return match.group(1).strip()
    return None


def unique(values: Iterable[str], limit: int = 12) -> list[str]:
    result: list[str] = []
    for value in values:
        value = re.sub(r"\s+", " ", value.strip()).replace("`", "'")
        if value and value not in result:
            result.append(value)
        if len(result) >= limit:
            break
    return result


def display_list(values: Iterable[str], empty: str = "[待确认]") -> str:
    items = unique(values)
    return ", ".join(f"`{item}`" for item in items) if items else empty


def detect_facts(root: Path) -> dict[str, str]:
    files = iter_project_files(root)
    texts = {rel(path, root): read_text(path) for path in files}
    package = load_package(root)
    readme_text = texts.get("README.md", "") or texts.get("README.mdx", "")

    name = str(package.get("name") or root.name)
    description = str(package.get("description") or "")
    headings = [first_heading(readme_text)] if first_heading(readme_text) else []
    clues = unique([name, description, *headings], limit=5)

    dependencies = {
        **(package.get("dependencies") or {}),
        **(package.get("devDependencies") or {}),
    }
    dependency_names = list(dependencies)
    framework_markers = {
        "react": "React",
        "next": "Next.js",
        "vue": "Vue",
        "nuxt": "Nuxt",
        "svelte": "Svelte",
        "@angular/core": "Angular",
        "vite": "Vite",
        "tailwindcss": "Tailwind CSS",
        "antd": "Ant Design",
        "@mui/material": "MUI",
        "@radix-ui/react": "Radix UI",
        "lucide-react": "Lucide",
        "framer-motion": "Framer Motion",
        "motion": "Motion",
        "gsap": "GSAP",
    }
    frameworks = [label for key, label in framework_markers.items() if any(dep == key or dep.startswith(key + "/") for dep in dependency_names)]
    if (root / "pubspec.yaml").is_file():
        frameworks.append("Flutter")

    scripts = package.get("scripts") or {}
    commands = [f"{key}: {value}" for key, value in scripts.items() if key in {"dev", "start", "build", "test", "lint"}]

    route_paths = [
        path for path in texts
        if any(part in {"app", "pages", "routes"} for part in Path(path).parts)
        or Path(path).name.lower() in {"app.tsx", "app.jsx", "main.tsx", "main.jsx", "main.ts", "main.js"}
    ]
    component_paths = [
        path for path in texts
        if "component" in {part.lower() for part in Path(path).parts}
        or re.search(r"/(?:[A-Z][A-Za-z0-9_-]*\.(?:tsx|jsx|vue|svelte))$", "/" + path)
    ]

    token_paths: list[str] = []
    token_names: list[str] = []
    token_count = 0
    literal_count = 0
    responsive_paths: list[str] = []
    motion_paths: list[str] = []
    status_hits: list[str] = []
    sensitive_hits: list[str] = []
    for path, text in texts.items():
        lower = text.lower()
        token_matches = re.findall(r"--[a-zA-Z][\w-]*", text)
        if token_matches or Path(path).suffix.lower() in {".css", ".scss"} or "token" in path.lower() or "theme" in path.lower():
            token_paths.append(path)
            token_names.extend(token_matches)
            token_count += len(set(token_matches))
        literal_count += len(re.findall(r"#[0-9a-fA-F]{3,8}\b|\b\d+(?:\.\d+)?px\b|\b\d+(?:\.\d+)?ms\b", text))
        if re.search(r"@media\b|\b(sm|md|lg|xl):|breakpoint|viewport", lower):
            responsive_paths.append(path)
        if re.search(r"animation|transition|motion|gsap|framer|keyframes", lower):
            motion_paths.append(path)
        if re.search(r"loading|empty|error|success|warning|danger|failed|running|pending|timeout|permission|queued|completed|加载|空态|错误|成功|警告|权限|超时", lower):
            status_hits.append(path)
        if re.search(r"password|secret|access.?key|api.?key|credit|身份证|手机号|邮箱|主机.?ip", lower):
            sensitive_hits.append(path)

    entrypoints = [
        path for path in texts
        if Path(path).name.lower() in {"index.html", "app.tsx", "app.jsx", "main.tsx", "main.jsx", "main.ts", "main.js"}
    ]
    type_hints = []
    suffixes = {Path(path).suffix.lower() for path in texts}
    if ".tsx" in suffixes or ".jsx" in suffixes:
        type_hints.append("Web UI")
    if ".vue" in suffixes:
        type_hints.append("Vue Web UI")
    if ".svelte" in suffixes:
        type_hints.append("Svelte Web UI")
    if (root / "pubspec.yaml").is_file():
        type_hints.append("Flutter App")

    return {
        "name": name,
        "clues": display_list(clues),
        "type": display_list(type_hints),
        "frameworks": display_list(frameworks),
        "commands": display_list(commands),
        "entrypoints": display_list(entrypoints),
        "routes": display_list(route_paths),
        "components": display_list(component_paths),
        "token_paths": display_list(token_paths),
        "token_names": display_list(token_names),
        "token_count": str(token_count or 0),
        "literal_count": str(literal_count or 0),
        "responsive": display_list(responsive_paths),
        "motion": display_list(motion_paths),
        "statuses": display_list(status_hits),
        "sensitive": display_list(sensitive_hits),
    }


def managed_block(title: str, lines: Iterable[str]) -> str:
    body = "\n".join([MARKER_START, f"## {title}", "", *lines, MARKER_END])
    return body.rstrip()


def blocks_for(facts: dict[str, str]) -> dict[str, str]:
    return {
        "spec.md": managed_block("项目事实（自动同步）", [
            f"- 项目名称：`{facts['name']}`",
            f"- 项目类型线索：{facts['type']}",
            f"- 入口与路由线索：{facts['routes']}",
            f"- 技术栈：{facts['frameworks']}",
            f"- 可用脚本：{facts['commands']}",
        ]),
        "domain.md": managed_block("项目事实（自动同步）", [
            f"- 可观察到的业务/产品关键词：{facts['clues']}",
            f"- 代码中出现状态/风险词的文件：{facts['statuses']}",
            f"- 可能包含敏感字段的文件：{facts['sensitive']}",
            "- 以上线索仅供核对，业务语义和责任规则需由项目维护者确认。",
        ]),
        "craft.md": managed_block("项目事实（自动同步）", [
            f"- 检测到的字体与样式入口：{facts['token_paths']}",
            f"- 检测到的动效/动画线索：{facts['motion']}",
            f"- 响应式断点线索：{facts['responsive']}",
        ]),
        "design.md": managed_block("项目事实（自动同步）", [
            f"- 检测到的 token 文件：{facts['token_paths']}",
            f"- 检测到的 token 名称：{facts['token_names']}",
            f"- 去重后的 CSS 变量数量：`{facts['token_count']}`",
            f"- 可能的视觉字面量数量（需人工判断）：`{facts['literal_count']}`",
            "- 脚本不会自动把字面量认定为错误；请结合项目规范回写 Token 缺口。",
        ]),
        "components.md": managed_block("项目事实（自动同步）", [
            f"- 组件目录与文件线索：{facts['components']}",
            f"- UI 依赖与组件库线索：{facts['frameworks']}",
            f"- 入口文件：{facts['entrypoints']}",
        ]),
        "template.md": managed_block("项目事实（自动同步）", [
            f"- 页面/路由线索：{facts['routes']}",
            f"- App shell 与布局入口：{facts['entrypoints']}",
            f"- 响应式实现线索：{facts['responsive']}",
        ]),
    }


def replace_block(content: str, block: str, adopt: bool = False) -> tuple[str, str]:
    pattern = re.compile(re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END), re.DOTALL)
    if pattern.search(content):
        return pattern.sub(block, content, count=1), "updated"
    if not adopt:
        return content, "unmanaged"
    lines = content.splitlines()
    if lines and lines[0].startswith("#"):
        adopted = "\n".join([lines[0], "", block, "", *lines[1:]])
    else:
        adopted = "\n".join([block, "", content])
    return adopted.rstrip() + "\n", "adopted"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="同步六份设计说明书文档")
    parser.add_argument("--project-root", type=Path, default=Path.cwd())
    parser.add_argument("--output-dir", type=Path, default=Path("."), help="相对项目根目录的输出目录")
    parser.add_argument("--skill-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--state-dir", type=Path, default=Path(STATE_DIR_NAME), help="相对项目根目录的状态目录")
    parser.add_argument("--mode", choices=("immediate", "passive"), default="immediate")
    parser.add_argument("--quiet-minutes", type=float, default=DEFAULT_QUIET_MINUTES)
    parser.add_argument("--only", help="只同步指定文档，逗号分隔")
    parser.add_argument("--check", action="store_true", help="只检查文档，不写入文档或状态")
    parser.add_argument("--report-only", action="store_true", help="只报告待同步状态，不写入正式文档")
    parser.add_argument("--adopt", action="store_true", help="将没有受管标记的旧文档包入受管区块")
    return parser.parse_args()


def parse_selected(raw: str | None) -> set[str] | None:
    if not raw:
        return None
    selected = {item.strip() for item in raw.split(",") if item.strip()}
    unknown = selected - set(DOC_TEMPLATES)
    if unknown:
        raise ValueError(f"未知文档：{', '.join(sorted(unknown))}")
    return selected


def sync_documents(
    root: Path,
    output_dir: Path,
    template_dir: Path,
    blocks: dict[str, str],
    selected: set[str] | None,
    check: bool,
    adopt: bool,
) -> int:
    if not check:
        output_dir.mkdir(parents=True, exist_ok=True)
    failures = 0
    for filename, template_name in DOC_TEMPLATES.items():
        if selected is not None and filename not in selected:
            continue
        target = output_dir / filename
        template = read_text(template_dir / template_name)
        if not template:
            print(f"错误：模板为空或不可读：{filename}", file=sys.stderr)
            failures += 1
            continue
        if target.exists():
            current = read_text(target)
            next_content, status = replace_block(current, blocks[filename], adopt=adopt)
            if status == "unmanaged":
                print(f"警告：保留未受管文档（未覆盖）：{target}")
                failures += 1 if check else 0
                continue
        else:
            next_content, status = replace_block(template, blocks[filename])

        if check:
            if not target.exists() or next_content != read_text(target):
                print(f"需要同步：{target}")
                failures += 1
            elif status not in {"updated", "adopted"}:
                print(f"需要受管区块：{target}")
                failures += 1
        elif next_content != read_text(target):
            was_missing = not target.exists()
            target.write_text(next_content, encoding="utf-8")
            print(f"已{('创建' if was_missing else '更新')}：{target}")
        else:
            print(f"无需变更：{target}")
    return failures


def main() -> int:
    args = parse_args()
    root = args.project_root.expanduser().resolve()
    output_dir = (root / args.output_dir).resolve()
    template_dir = args.skill_root.expanduser().resolve() / "assets" / "templates"
    if not root.is_dir():
        print(f"错误：项目根目录不存在：{root}", file=sys.stderr)
        return 2
    if not template_dir.is_dir():
        print(f"错误：模板目录不存在：{template_dir}", file=sys.stderr)
        return 2
    if args.quiet_minutes < 0:
        print("错误：--quiet-minutes 不能小于 0", file=sys.stderr)
        return 2
    try:
        selected = parse_selected(args.only)
    except ValueError as error:
        print(f"错误：{error}", file=sys.stderr)
        return 2

    facts = detect_facts(root)
    blocks = blocks_for(facts)
    state = load_state(root, args.state_dir)

    if args.mode == "immediate":
        if args.report_only:
            print("错误：--report-only 只能与 --mode passive 一起使用", file=sys.stderr)
            return 2
        failures = sync_documents(root, output_dir, template_dir, blocks, selected, args.check, args.adopt)
        if args.check:
            return 1 if failures else 0
        state["snapshot"] = project_snapshot(root)
        state["initialized_at"] = state.get("initialized_at") or iso_time(utc_now())
        state["last_sync_at"] = iso_time(utc_now())
        state["last_sync_mode"] = "immediate"
        state["pending"] = None
        save_state(root, args.state_dir, state)
        return 1 if failures else 0

    was_initialized = bool(state.get("initialized_at"))
    current_snapshot = project_snapshot(root)
    changed, has_pending = detect_pending(root, state, current_snapshot)
    if not args.check:
        save_state(root, args.state_dir, state)
    if not was_initialized:
        print("已建立设计文档变更基线；未发现可收敛的待同步工作单元。")
        return 0
    pending = state.get("pending")
    if not has_pending or not pending:
        print("没有待同步的设计文档工作单元。")
        return 0

    quiet = pending_is_quiet(pending, args.quiet_minutes)
    changed_hint = f"变更文件：{', '.join(pending.get('changed_files', []))}" if changed else "已存在待同步工作单元"
    if not quiet:
        print(f"{changed_hint}；尚未达到 {args.quiet_minutes:g} 分钟静默阈值。")
        return PENDING_EXIT_CODE if args.report_only else 0
    if args.report_only:
        print(f"发现已静默待同步工作单元，受影响文档：{', '.join(pending.get('affected_documents', []))}")
        return PENDING_EXIT_CODE
    if args.check:
        check_selected = selected or set(pending.get("affected_documents", DOC_TEMPLATES))
        failures = sync_documents(root, output_dir, template_dir, blocks, check_selected, True, args.adopt)
        return 1 if failures else 0

    sync_selected = selected or set(pending.get("affected_documents", DOC_TEMPLATES))
    failures = sync_documents(root, output_dir, template_dir, blocks, sync_selected, False, args.adopt)
    if failures:
        print("待同步工作单元未完全收敛，请修复未受管文档后重试。", file=sys.stderr)
        return 1
    state["last_sync_at"] = iso_time(utc_now())
    state["last_sync_mode"] = "passive"
    state["pending"] = None
    save_state(root, args.state_dir, state)
    print("已将静默工作单元收敛到受影响的设计文档。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
