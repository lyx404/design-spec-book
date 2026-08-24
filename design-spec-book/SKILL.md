---
name: design-spec-book
description: "为网页、App 和其他产品设计项目生成并维护六份设计声明文档：spec.md、domain.md、craft.md、design.md、components.md、template.md；在明确使用设计说明书 skill 或持续修改设计项目时调用。"
---

# 设计说明书

这个 skill 把产品设计判断沉淀成六份可被 Agent 读取的 Markdown 声明。它参考 Vibe Design Playbook 的分工：声明回答“什么算对”，skill/evaluator 等执行契约负责“怎么做”和“怎么验收”，不要把后者伪装成这六份模板的内容。

参考原文：[Alibaba Cloud Vibe Design Playbook](https://alibaba-cloud-design.github.io/vibe-designing-playbook/)。

## 触发与目标

- 用户明确说“用设计说明书 skill”或 `$design-spec-book` 时，必须执行一次同步。
- 目标项目默认为当前工作目录；用户指定项目路径时以指定路径为准。
- 用户主动发起“同步设计说明书”“确认方案”或明确要求收敛时，使用即时模式更新正式文档。
- 用户没有主动发起同步时，AI 再进入同一项目要先运行被动检查：读取 `.design-spec/state.json`，判断是否存在已静默的待同步工作单元；达到阈值后只收敛受影响文档。
- 默认在目标项目根目录生成：`spec.md`、`domain.md`、`craft.md`、`design.md`、`components.md`、`template.md`。

## 工作流

1. 先做有边界的项目盘点：只读 `package.json`、README、入口/路由、组件目录、样式与 token 文件、测试配置和与当前任务直接相关的文件。跳过 `node_modules`、构建产物、缓存和二进制资源。
2. 进入项目时先执行被动检查：`python3 <design-spec-book>/scripts/sync_design_docs.py --project-root <项目根目录> --mode passive`。它只更新状态文件，不会在静默阈值前改六份正式文档。
3. 用户明确要求同步时执行即时模式：`python3 <design-spec-book>/scripts/sync_design_docs.py --project-root <项目根目录> --mode immediate`。
4. 阅读六份声明，再实现设计任务；需求、截图或参考网站中的示例是来源材料，不是当前项目的事实，不得把示例里的 Agent 看板、CloudAI 语义或颜色直接复制进项目。
5. 首次生成后，把已有项目事实和用户明确的设计意图填入六份文档的手写区块；脚本无法从代码可靠推断的业务判断必须标 `[待确认]`，不能凭空补全。
6. 修改期间只记录工作单元状态和候选受影响文档到 `.design-spec/state.json`，不要把每个中间方案写进正式文档。
7. 修改完成、验证通过且达到静默阈值后，被动模式只同步受影响文档。对不确定的信息写 `[待确认]`；`design.md` 中找不到的 token 记录到“Token 缺口”区块，禁止用字面量掩盖缺口。

### 静默与工作单元

- 默认静默阈值为 30 分钟，可用 `--quiet-minutes` 调整。
- 工作单元由最近变更的页面/组件/样式文件组成；脚本根据路径和文件类型映射受影响文档。
- 静默期间只写 `.design-spec/state.json`，该文件不是正式设计声明，也不需要被 Agent 当作设计规范读取。
- skill 不启动后台计时器；被动检查发生在下一次 AI 进入项目时。若用户在同一项目继续修改，静默计时会重新开始。
- `.design-spec/` 是运行状态目录，建议加入项目的 `.gitignore`，不要把中间工作状态提交到仓库。

### Git 提交兜底

可选安装提交前钩子：

```bash
python3 <design-spec-book>/scripts/install_git_hook.py \
  --project-root <项目根目录> --policy warn
```

`warn` 只提示待同步并阻止提交；`auto` 在提交前自动收敛静默工作单元：

```bash
python3 <design-spec-book>/scripts/install_git_hook.py \
  --project-root <项目根目录> --policy auto
```

## 六份声明的边界

| 文件 | 负责回答 | 不负责回答 |
| --- | --- | --- |
| `spec.md` | 功能为谁做、信息如何组织、状态如何流转、什么算验收 | 视觉风格、具体组件库、实现代码 |
| `domain.md` | 业务对象、状态、风险、敏感数据和操作责任如何表达 | 通用排版、token 命名、页面布局 |
| `craft.md` | 排版层级、密度、动效、材质和反模板化工艺 | 项目业务术语和品牌 token 事实源 |
| `design.md` | token、视觉语义、状态派生、系统缺口 | 功能流程和组件语义选择 |
| `components.md` | 可用组件、语义边界、易混组件和状态 | 页面整体骨架和业务规则 |
| `template.md` | 页面类型、App shell、信息架构起点和密度 | 单个组件实现细节 |

六份模板的完整字段见 [references/document-contract.md](references/document-contract.md)。模板资源位于 `assets/templates/`，不包含任何项目具体内容。

## 保留用户修改

每份生成文档都有一对 `design-spec:managed` 标记。同步只替换标记之间的项目事实；标记外的内容属于用户维护区，不能整文件覆盖。发现同名但没有标记的旧文档时，默认保留并报告警告，先人工合并，不进行静默改写。

## 验证

- 先运行 `python3 <design-spec-book>/scripts/sync_design_docs.py --project-root <项目根目录> --check` 检查六份文件是否存在且受管区块完整。
- 被动状态检查可用 `--mode passive --report-only`，退出码 `3` 表示存在已达到静默阈值的待同步工作单元。
- 再运行 skill creator 的 `quick_validate.py` 检查 skill 包结构和 frontmatter。
- 只做与本次变更直接相关的验证；不要因为生成文档而运行整个业务项目的全量测试。
