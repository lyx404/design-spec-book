# Design Spec Book

** [中文](#zh) · [English](#en)

<a id="zh"></a>

## 中文

### 安装

```bash
npx skills add lyx404/design-spec-book -s design-spec-book -g -y
```

安装完成后，开启新的 Codex 对话并输入：

```text
$design-spec-book
```

### 功能

- 生成并维护六份设计声明：`spec.md`、`domain.md`、`craft.md`、`design.md`、`components.md`、`template.md`。
- 分离功能行为、领域语义、设计工艺、视觉 token、组件边界和页面结构。
- 自动扫描项目入口、路由、组件、样式和 token，只同步可观察的项目事实。
- 通过受管区块保护人工填写的设计判断，不覆盖用户修改。
- 支持即时同步、被动同步、变更检测和可选 Git 提交前检查。

### 六份文档

| 文档 | 作用 |
| --- | --- |
| `spec.md` | 功能目标、信息架构、状态流转和验收标准 |
| `domain.md` | 业务对象、术语、风险和责任规则 |
| `craft.md` | 排版、信息密度、状态反馈和动效工艺 |
| `design.md` | 颜色、字体、间距、状态 token 和视觉规则 |
| `components.md` | 组件职责、语义边界和可访问性 |
| `template.md` | 页面类型、App shell、页面骨架和响应式起点 |

### 使用

直接调用：

```text
$design-spec-book
```

或者告诉 Codex：

```text
用设计说明书 skill 为当前项目初始化并同步六份设计文档。
```

### 链接

- [介绍页](https://lyx404.github.io/design-spec-book/)
- [GitHub 仓库](https://github.com/lyx404/design-spec-book)

<a id="en"></a>

## English

### Install

```bash
npx skills add lyx404/design-spec-book -s design-spec-book -g -y
```

After installation, start a new Codex conversation and enter:

```text
$design-spec-book
```

### Features

- Creates and maintains six design declarations: `spec.md`, `domain.md`, `craft.md`, `design.md`, `components.md`, and `template.md`.
- Separates behavior, domain language, design craft, visual tokens, component boundaries, and page structure.
- Scans project entry points, routes, components, styles, and tokens, then syncs only observable facts.
- Preserves human-authored decisions outside the managed block.
- Supports immediate sync, passive sync, change detection, and an optional Git pre-commit check.

### Six declarations

| File | Purpose |
| --- | --- |
| `spec.md` | Feature intent, information architecture, state flow, and acceptance criteria |
| `domain.md` | Business objects, terminology, risk, and responsibility rules |
| `craft.md` | Typography, information density, state feedback, and motion craft |
| `design.md` | Colors, typography, spacing, state tokens, and visual rules |
| `components.md` | Component responsibilities, semantic boundaries, and accessibility |
| `template.md` | Page types, app shell, page skeleton, and responsive starting points |

### Usage

Invoke the skill directly:

```text
$design-spec-book
```

Or ask Codex:

```text
Use the design-spec-book skill to initialize and sync the six design documents for this project.
```

### Links

- [Introduction site](https://lyx404.github.io/design-spec-book/)
- [GitHub repository](https://github.com/lyx404/design-spec-book)

MIT License.
