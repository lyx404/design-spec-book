# DESIGN.md

<!-- version: [major.minor] -->
<!-- updated: [YYYY-MM-DD] -->

<!-- extraction-meta
source: [设计稿、代码或设计系统来源]
scope: [覆盖的页面、节点或组件范围]
date: [YYYY-MM-DD]
nodes-scanned: [数量或未知]
confidence: { extracted: [百分比], inferred: [百分比], known: [百分比] }
-->

> 这是视觉设计系统的单一事实源。只记录已确认的项目视觉事实、可复用规则和有依据的推断；无法确认的内容标记为 `[待确认]`。

## 1. Identity

**一句话定义：** [产品/项目的视觉身份、字体方向和主要视觉特征]

**视觉签名：**

- [特征 1：例如布局、形状或材质]
- [特征 2]
- [特征 3]

**适用范围：** [页面、平台、主题或组件覆盖范围]

**不属于本系统的内容：** [不应从本文件推断的业务、交互或实现细节]

## 2. Structure

记录设计稿或已实现页面的高层结构，帮助后续页面继承真实的布局关系，而不是从零猜页面骨架。

### 页面/画板：[页面名称]

_[页面数量、视口尺寸或来源说明]_

- **[区域/页面名称]** · `[类型]` · `[宽]×[高]`
  - **[子区域]** · `[布局方向]` · `gap: [值]` · `padding: [值]`
  - **[组件/内容]** · `[职责]` · `[尺寸或约束]`

### Layout primitives

| Primitive | Token/规则 | 用途 | 约束 |
| --- | --- | --- | --- |
| 页面容器 | `[token]` | [用途] | [最大宽度、边距或流式规则] |
| 内容列 | `[token]` | [用途] | [列数、比例或最小宽度] |
| 栅格/间距 | `[token]` | [用途] | [允许的间距关系] |
| 侧栏/顶部栏 | `[token]` | [用途] | [固定、可折叠或响应式规则] |

## 3. Color

颜色必须按语义命名。表格可以记录实际值，但代码应优先引用 token；同一语义在不同主题中保持角色一致。

### Palette

| Token | Value | Role | Usage | Similar/alias | Source | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| `[token]` | `[value]` | [语义角色] | [使用范围] | [相近 token 或 —] | [来源] | [confirmed/inferred] |

### Modes

#### [主题模式名称]

| Token | Value | Intent | Primary usage |
| --- | --- | --- | --- |
| `[token]` | `[value]` | [意图] | [主要使用位置] |

### Semantic mapping

| Context | Required mapping |
| --- | --- |
| 页面背景 | `[canvas token]` |
| 卡片、弹层和菜单 | `[surface token]` |
| 选中项/悬停项 | `[selection token]` |
| 正向状态 | `[success token]` |
| 风险/错误状态 | `[danger token]` |
| 信息/中性状态 | `[info/muted token]` |

### Component surfaces

| Container/component | Background | Border | Interaction |
| --- | --- | --- | --- |
| [组件或容器] | `[surface token]` | `[border token]` | [hover/selected/focus 规则] |

## 4. Typography

### Fonts

```css
--font-heading: [heading font stack];
--font-body: [body font stack];
--font-mono: [mono font stack];
```

| Role | Token | Size | Weight | Line Height | Letter Spacing | Font | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Display/H1/Body/Caption] | `[token]` | `[value]` | `[value]` | `[value]` | `[value]` | `[font token]` | [来源] |

### Text rules

- [中文、英文、数字和等宽数字的排版规则]
- [长标题、截断、换行和辅助文案规则]
- [最小可读字号、对比度或阅读宽度要求]

## 5. Spacing & Layout

### Base unit

Allowed values: `[space-1]`, `[space-2]`, `[space-3]`, `[space-4]` …

### Spacing scale

| Token | Value | Typical usage |
| --- | --- | --- |
| `[space-token]` | `[value]` | [用途] |

### Border radius

| Token | Value | Usage |
| --- | --- | --- |
| `[radius-token]` | `[value]` | [用途] |

### Responsive layout

| Breakpoint | Layout change | Content constraint |
| --- | --- | --- |
| `[breakpoint]` | [变化] | [不变的内容、排序或语义] |

## 6. Depth & Motion

### Elevation

| Token | Shadow/Effect | Source | Usage |
| --- | --- | --- | --- |
| `[elevation-token]` | `[shadow or effect]` | [来源] | [层级用途] |

### Motion tokens

| Token | Duration | Easing | Trigger | Purpose |
| --- | --- | --- | --- | --- |
| `[motion-token]` | `[value]` | `[value]` | [触发条件] | [层级、反馈或状态变化目的] |

### Motion rules

- 动效必须服务层级、反馈、状态变化或空间关系，不为装饰而持续运动。
- 优先动画 `transform` 和 `opacity`；避免引起布局抖动的属性动画。
- 启用 reduced motion 时移除非必要动画，并保留状态变化的可理解反馈。

## 7. Components

只记录与视觉系统直接相关的组件表现、图表编码和可复用模式；组件语义边界的完整登记仍属于 `components.md` 文档。

### Component visual patterns

| Component | Visual role | Surface | Typography | States | Notes |
| --- | --- | --- | --- | --- | --- |
| [组件] | [视觉角色] | `[token]` | `[token]` | [状态规则] | [约束] |

### Data visualization (optional)

如果项目包含图表，按数据关系记录选型规则，禁止把颜色当作唯一编码通道。

| Data relationship | Preferred chart | Rule | Accessibility/QA |
| --- | --- | --- | --- |
| [时间趋势/比较/排名/相关性] | [图表类型] | [选型规则] | [可访问性和验收要求] |

#### Chart anatomy and interaction

- 标题、操作区、图例、图形区的顺序：
- 图形区的最小高度/宽高比：
- 图例、tooltip、筛选器和键盘交互：
- 数值精度、单位、排序和基线规则：
- Loading、Empty、Error、Partial data 的图表表现：

### Component QA checklist

- [ ] 组件使用现有 token，不散落视觉字面量。
- [ ] 状态不只依赖颜色表达。
- [ ] 桌面、平板、移动端没有裁切或不可读内容。
- [ ] 交互状态、焦点和 reduced motion 有对应表现。

## 8. States

State tokens should be derived from the base palette above.

| State | Treatment |
| --- | --- |
| Hover | [从基础 token 派生的悬停表现] |
| Active/Selected | [选中/激活表现] |
| Focus | [可见焦点环和键盘规则] |
| Disabled | [禁用透明度、边界和交互规则] |
| Loading | [骨架/占位/进度表现] |
| Empty | [空状态容器和行动入口] |
| Error | [错误边界、文案和恢复入口] |

## 9. Rules

### Do

- 使用本文件定义的 token、类型层级、间距、圆角和阴影。
- 新页面先复用现有结构、语义角色和状态处理。
- 让新增值有明确角色、来源、适用范围和置信度。

### Don't

- 不在页面或组件中随意新增未登记的颜色、字号、间距、圆角或动效值。
- 不混用没有角色说明的字体、主题或视觉语言。
- 不让渐变、阴影、装饰插画或动效遮挡主要信息和任务路径。

## 10. Extending this system

### How to reuse this DESIGN.md

1. 将本文件作为视觉事实源提交到项目根目录。
2. 新页面先继承 Identity、Structure、token 和 States，再添加局部规则。
3. 设计稿或代码发生实质变化时更新本文件，并与对应实现一起审查。
4. 将已确认的 token 同步到 CSS 变量、主题配置或设计系统 API；代码引用名称，不复制字面量。

### Adding a new screen

- 从现有页面结构和布局 primitive 中选择起点。
- 先确认页面类型、内容密度、响应式变化和状态范围。
- 只有当现有 token 无法表达新的稳定语义时，才新增 token。

### When to add a new token vs reuse

| Situation | Action |
| --- | --- |
| 需要已有颜色的明暗或透明变化 | 复用基础 token 并派生，不新增孤立值 |
| 需要两个字号之间的临时字号 | 优先选择邻近层级，不填补偶然缺口 |
| 需要一次性间距 | 先归入现有间距尺度，并记录例外原因 |
| 出现稳定的新语义角色 | 新增 token，并写明角色、来源、范围和置信度 |
| 新组件模式重复出现 | 提升到 Components 或本节的可复用模式 |

### Versioning

- 调色板、字体层级、间距尺度或主题语义发生破坏性变化时，提升 `version`。
- 新增组件模式、阴影层级或非破坏性 token 时，记录 minor 变更。
- 设计文件与实现代码应在同一变更中更新，避免视觉事实源与代码漂移。

## 11. Machine-readable tokens

以下区块是可选的机器可读 token 映射。必须是合法 JSON，不得混入注释或项目外的示例值。

```json design-tokens
{
  "$schema": "design-tokens.v1",
  "meta": {
    "source": "[设计来源]",
    "updated": "[YYYY-MM-DD]"
  },
  "color": {},
  "colorModes": {},
  "typography": {},
  "spacing": {},
  "radius": {},
  "shadow": {},
  "motion": {},
  "layout": {},
  "components": {}
}
```

<!-- design-spec:managed:start -->
## 项目事实（自动同步）

- 检测到的 token 文件：[待确认]
- 检测到的 token 名称：[待确认]
- 去重后的 CSS 变量数量：`0`
- 可能的视觉字面量数量（需人工判断）：`0`
- 脚本不会自动把字面量认定为错误；请结合项目规范回写 Token 缺口。
<!-- design-spec:managed:end -->
