# Design Spec Book

把产品设计判断沉淀成六份可被 Agent 读取、维护和复用的设计声明。

Design Spec Book turns product intent into a durable design contract for Codex.

## 安装 / Install

```bash
npx skills add lyx404/design-spec-book -s design-spec-book -g -y
```

安装后在新的 Codex 对话中输入：

```text
$design-spec-book
```

After installation, start a new Codex conversation and enter:

```text
$design-spec-book
```

## 功能 / Features

### 中文

- 生成并维护六份设计声明：`spec.md`、`domain.md`、`craft.md`、`design.md`、`components`、`template`。
- 分离功能行为、领域语义、设计工艺、视觉 token、组件边界和页面结构。
- 自动扫描项目入口、路由、组件、样式和 token，只同步可观察的项目事实。
- 通过受管区块保护人工填写的设计判断，不覆盖用户修改。
- 支持即时同步、被动同步、变更检测和可选 Git pre-commit 检查。

### English

- Creates and maintains six design declarations: `spec.md`, `domain.md`, `craft.md`, `design.md`, `components`, and `template`.
- Separates behavior, domain language, design craft, visual tokens, component boundaries, and page structure.
- Scans project entry points, routes, components, styles, and tokens, then syncs only observable facts.
- Preserves human-authored decisions outside the managed block.
- Supports immediate sync, passive sync, change detection, and an optional Git pre-commit check.

## 六份文档 / Six declarations

| 文件 / File | 记录内容 / Covers |
| --- | --- |
| `spec.md` | 功能目标、信息架构、状态流转 / Behavior and acceptance |
| `domain.md` | 业务对象、术语、风险 / Domain language and responsibility |
| `craft.md` | 排版、密度、反馈、动效 / Typography, density, motion |
| `design.md` | 颜色、字体、间距、状态 token / Visual system and tokens |
| `components` | 组件职责、边界、可访问性 / Component semantics and accessibility |
| `template` | 页面类型、App shell、响应式骨架 / Page structure and responsive starting points |

## 使用 / Usage

```text
$design-spec-book
```

或者：

```text
用设计说明书 skill 为当前项目初始化并同步六份设计文档。
```

Or ask:

```text
Use the design-spec-book skill to initialize and sync the six design documents for this project.
```

## 链接 / Links

- [介绍页 / Introduction site](https://lyx404.github.io/design-spec-book/)
- [GitHub repository](https://github.com/lyx404/design-spec-book)

MIT License.


