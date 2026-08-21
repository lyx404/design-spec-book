# Design Spec Book

把产品设计判断沉淀成六份可被 Agent 读取、维护和复用的设计声明。

Design Spec Book is a Codex skill for turning product intent into a durable design contract. It keeps behavior, domain language, visual tokens, component boundaries, and page structure separate, then synchronizes observable project facts without overwriting human decisions.

## Install

Install the skill from GitHub with Codex's GitHub installer:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo lyx404/design-spec-book \
  --path design-spec-book
```

After installation, start a new Codex turn and invoke it with:

```text
$design-spec-book
```

You can also ask in natural language:

```text
用设计说明书 skill 为当前项目初始化并同步六份设计文档。
```

## What it does

The skill creates and maintains six Markdown declarations at the project root:

| Document | It answers |
| --- | --- |
| `spec.md` | Who the feature is for, how information is organized, how states flow, and what counts as done |
| `domain.md` | Business objects, terms, risk, sensitive data, and responsibility rules |
| `craft.md` | Typography, density, feedback, motion, material, and anti-template craft |
| `design.md` | The visual source of truth for tokens, semantic roles, states, layout, and motion |
| `components` | Real components, semantic boundaries, confusing alternatives, and accessibility rules |
| `template` | Page types, app shell, page skeleton, density, and responsive starting points |

The last two files intentionally keep their extensionless names, while remaining Markdown.

## How synchronization works

The synchronizer scans a bounded set of project files such as `package.json`, README files, routes, components, styles, tokens, and tests. It records observable clues in a managed block:

```markdown
<!-- design-spec:managed:start -->
## 项目事实（自动同步）
...
<!-- design-spec:managed:end -->
```

Only this block is replaced. Everything outside it is the project maintainer's design decision and is preserved across runs.

### Immediate sync

Use this after a deliberate design decision or when initializing a project:

```bash
python3 /path/to/design-spec-book/scripts/sync_design_docs.py \
  --project-root /path/to/your-project \
  --mode immediate
```

### Passive sync

Use this when entering a project again. It records changed files in `.design-spec/state.json` and waits for the default 30-minute quiet period before updating only affected declarations:

```bash
python3 /path/to/design-spec-book/scripts/sync_design_docs.py \
  --project-root /path/to/your-project \
  --mode passive
```

The state directory is runtime metadata, not a design specification. Add `.design-spec/` to `.gitignore`.

## Useful options

```bash
# Check whether documents exist and their managed blocks are current
python3 /path/to/design-spec-book/scripts/sync_design_docs.py \
  --project-root /path/to/your-project --check

# Sync only selected documents
python3 /path/to/design-spec-book/scripts/sync_design_docs.py \
  --project-root /path/to/your-project \
  --mode immediate --only spec.md,design.md

# Report pending passive work without changing documents
python3 /path/to/design-spec-book/scripts/sync_design_docs.py \
  --project-root /path/to/your-project \
  --mode passive --report-only
```

## Optional Git hook

Install a pre-commit warning:

```bash
python3 /path/to/design-spec-book/scripts/install_git_hook.py \
  --project-root /path/to/your-project --policy warn
```

Use `--policy auto` to automatically converge quiet work units before a commit.

## Repository layout

```text
design-spec-book/
├── design-spec-book/       # installable Codex skill
├── site/                    # static project introduction page
├── README.md
└── LICENSE
```

## Local preview

The introduction page is a dependency-free static site. Open [`site/index.html`](site/index.html) directly, or serve it locally:

```bash
python3 -m http.server 4173 --directory site
```

Then visit `http://localhost:4173`.

The public introduction site is available at <https://lyx404.github.io/design-spec-book/>.

## License

MIT. See [`LICENSE`](LICENSE).
