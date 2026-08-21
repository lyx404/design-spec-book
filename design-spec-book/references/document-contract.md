# 文档契约

这套 skill 将设计声明与项目事实分开。模板只描述应填写什么；同步脚本才把目标项目中已经存在的事实放入受管区块。任何无法从代码、配置、README 或用户明确说明中证实的内容都必须标为 `[待确认]`。

## 受管区块

每份文档使用以下标记，标记外的正文由项目维护者负责：

```markdown
<!-- design-spec:managed:start -->
## 项目事实（自动同步）
...
<!-- design-spec:managed:end -->
```

同步可以重复运行。它只替换两条标记之间的内容，不删除用户补充的设计判断。

## 同步状态

正式文档与工作状态分开：

- 即时模式（`--mode immediate`）用于用户主动发起同步，立即更新正式文档。
- 被动模式（`--mode passive`）用于 AI 再进入项目时检查变更。它默认等待 30 分钟静默，只在工作单元达到阈值后收敛受影响文档。
- `.design-spec/state.json` 记录文件快照、工作单元、受影响文档和最近变更时间；它不是设计规范，不应替代六份正式文档。
- `--report-only` 只报告待同步状态，退出码 `3` 表示存在达到静默阈值的工作单元，适合 Git hook 的 warn 策略。

静默期间不把中间方案写入正式文档。用户明确要求同步时，即使静默时间未达到，也应使用即时模式收敛当前最终结论。

## 六份文档

### `spec.md`

用 L1-L6 说明一个功能或页面怎样成立：定位与意图、信息架构、核心链路、组件功能细节、边界条件、验收标准。L1 还要写清始终自动执行、询问后执行、永不执行的行为边界；L5 至少覆盖空、加载、错误和权限降级；L6 使用 Given / When / Then 或等价可验证条件。

### `domain.md`

记录业务对象、状态、风险等级、术语、敏感数据和不可逆操作。状态色和风险表达应引用项目的语义 token，而不是在这里随意发明色值。默认脱敏、显式查看、审计记录等责任规则只在项目确有此类数据时填写。

### `craft.md`

记录跨业务可复用的工艺判断：字体与文字层级、布局密度、内容节奏、状态反馈、动效目的、材质和反 AI 模板化检查。它不替代领域规则，也不承担 token 的单一事实源。

### `design.md`

作为视觉事实源。推荐按以下层级维护：文档元数据与提取置信度、Identity、Structure、Color（Palette、Modes、Semantic mapping、Component surfaces）、Typography（Fonts、Scale、Text rules）、Spacing & Layout（Base unit、Spacing scale、Border radius、Responsive layout）、Depth & Motion（Elevation、Motion tokens、Motion rules）、Components（视觉模式和可选的数据可视化规则）、States、Rules、Extending this system、Machine-readable tokens。

它不仅登记 token 名称与来源，也要记录 token 的角色、使用范围、主题映射、状态派生、响应式约束、动效目的和系统缺口。视觉值优先通过 `var(--*)` 或项目已有 token API 引用；缺口要记录，不要偷偷写 hex、孤立 px 或孤立时长。机器可读区块必须是合法 JSON，并与上面的表格保持一致。

### `components`

登记项目可用组件和语义边界，明确何时使用、何时不用、默认/加载/禁用/错误状态，以及易混组件对（例如状态与分类、确认与详情）。组件名称以项目真实代码或依赖为证据。

### `template`

描述页面类型、App shell、主区/次区/操作区、信息密度、响应式策略和禁用边界。它提供结构起点，不应把某一张示例页面硬编码成所有项目的骨架。

## 更新归属

| 变化 | 应回写 |
| --- | --- |
| 新增状态、分支、空态或验收条件 | `spec.md` |
| 新业务对象、风险或敏感字段 | `domain.md` |
| 字体、层级、动效或密度调整 | `craft.md` |
| token、视觉语义或派生状态调整 | `design.md` |
| 新组件、组件替换或语义误用修正 | `components` |
| 页面壳层、布局方向或页面类型变化 | `template` |
