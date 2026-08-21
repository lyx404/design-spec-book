const translations = {
  "zh-CN": {
    documentTitle: "Design Spec Book / 安装",
    documentDescription: "Design Spec Book：为 Codex 保存可持续使用的产品设计上下文。",
    brandAria: "Design Spec Book 首页",
    topnavAria: "页面工具",
    languageAria: "选择语言",
    themeAria: "切换到深色模式",
    themeLight: "浅色",
    themeDark: "深色",
    themeToLight: "切换到浅色模式",
    themeToDark: "切换到深色模式",
    github: "GITHUB",
    featureExpandAria: "展开详情",
    featureCollapseAria: "收起详情",
    titlePrimary: "设计",
    titleSecondary: "说明书",
    leadPrefix: "把产品意图、业务语义和视觉规则保存成一套可以被 Agent 继续读取的",
    leadHighlight: "设计上下文",
    leadSuffix: "。",
    installationLabel: "01 / 快捷安装",
    installationTitle: "安装",
    copyAria: "复制安装命令",
    copyCommand: "复制",
    copyPromptAria: "复制提示词",
    copyPrompt: "复制",
    copied: "已复制",
    copyFailed: "复制失败",
    copiedAria: "安装命令已复制",
    copyFailedAria: "复制安装命令失败",
    promptCopied: "已复制",
    promptCopyFailed: "复制失败",
    promptCopiedAria: "提示词已复制",
    promptCopyFailedAria: "复制提示词失败",
    footerBuildBy: "Build by ",
    footerSupportPrefix: "，如果对你有帮助，也欢迎请我",
    coffeeAction: "喝杯咖啡",
    coffeeOpenAria: "打开喝杯咖啡窗口",
    coffeeDialogAria: "请我喝杯咖啡",
    coffeeCloseAria: "关闭喝杯咖啡窗口",
    coffeeImageAlt: "支付宝喝杯咖啡图片",
    usageLabel: "02 / 使用说明",
    usageTitle: "这样使用",
    usage1Title: "第一次使用",
    usage1Copy: "为当前项目生成设计说明书。",
    usage1Prompt: "使用 $design-spec-book，为当前项目生成设计说明书。",
    usage2Title: "同步项目变化",
    usage2Copy: "代码改完后，让说明书一起更新。",
    usage2Prompt: "使用 $design-spec-book，读取当前项目的最新代码，同步更新相关的设计说明书。",
    usage3Title: "调整设计规则",
    usage3Copy: "想改哪个页面，就直接告诉它。",
    usage3Prompt: "使用 $design-spec-book，按照当前最新的视觉与交互规则，更新设计说明书。",
    featuresLabel: "03 / 它能做什么",
    featuresTitle: "为项目建立设计上下文",
    feature1Title: "基于你的项目生成设计说明书",
    feature1Copy: "按功能、业务、视觉、组件与页面模板分别整理。",
    feature2Title: "说明书更新机制",
    feature2Copy: "根据代码变更，自动或手动同步相关设计说明书。",
    mechanismDetect: "→ 自动更新",
    mechanismDetectCopy: "代码变更静默期结束后，自动同步受影响的设计说明书",
    mechanismMap: "→ 手动更新",
    mechanismMapCopy: "用户发起同步请求后，立即检查代码变更并更新相关内容",
    mechanismPreserve: "→ 中间工作状态",
    mechanismPreserveCopy: "持续修改期间，仅记录待同步变更，不改写正式设计说明书",
    declarationSpec: "功能目标、状态流转和验收标准",
    declarationDomain: "业务对象、术语、风险和责任规则",
    declarationCraft: "排版、信息密度、反馈和动效工艺",
    declarationDesign: "颜色、字体、间距、状态 token 和视觉规则",
    declarationComponents: "组件职责、语义边界和可访问性",
    declarationTemplate: "页面类型、App shell 和响应式起点"
  },
  en: {
    documentTitle: "Design Spec Book / Installation",
    documentDescription: "Design Spec Book: persistent product-design context for Codex.",
    brandAria: "Design Spec Book home",
    topnavAria: "Page tools",
    languageAria: "Choose language",
    themeAria: "Switch to dark mode",
    themeLight: "LIGHT",
    themeDark: "DARK",
    themeToLight: "Switch to light mode",
    themeToDark: "Switch to dark mode",
    github: "GITHUB",
    featureExpandAria: "Expand details",
    featureCollapseAria: "Collapse details",
    titlePrimary: "Design Spec",
    titleSecondary: "Book",
    leadPrefix: "Keep product intent, domain language, and visual rules in a ",
    leadHighlight: "design context",
    leadSuffix: " an Agent can read and continue using.",
    installationLabel: "01 / QUICK INSTALL",
    installationTitle: "Install",
    copyAria: "Copy installation command",
    copyCommand: "COPY",
    copyPromptAria: "Copy prompt",
    copyPrompt: "COPY",
    copied: "COPIED",
    copyFailed: "COPY FAILED",
    copiedAria: "Installation command copied",
    copyFailedAria: "Failed to copy installation command",
    promptCopied: "COPIED",
    promptCopyFailed: "COPY FAILED",
    promptCopiedAria: "Prompt copied",
    promptCopyFailedAria: "Failed to copy prompt",
    footerBuildBy: "Build by ",
    footerSupportPrefix: ". If this helped, you're welcome to share a ",
    coffeeAction: "coffee",
    coffeeOpenAria: "Open coffee support dialog",
    coffeeDialogAria: "Support with coffee",
    coffeeCloseAria: "Close coffee support dialog",
    coffeeImageAlt: "Alipay coffee support QR code",
    usageLabel: "02 / USAGE",
    usageTitle: "How to use it",
    usage1Title: "Start a project",
    usage1Copy: "Create a design spec book for the current project.",
    usage1Prompt: "Use $design-spec-book to create a design spec book for this project.",
    usage2Title: "Sync project changes",
    usage2Copy: "After changing code, update the design notes too.",
    usage2Prompt: "Use $design-spec-book to read the latest code in this project and update the related design spec book.",
    usage3Title: "Update design rules",
    usage3Copy: "Tell it which page you want to change.",
    usage3Prompt: "Use $design-spec-book to update the design spec book according to the latest visual and interaction rules.",
    featuresLabel: "03 / WHAT IT DOES",
    featuresTitle: "Build design context for a project",
    feature1Title: "Creates a design spec book for your project",
    feature1Copy: "Organizes product behavior, domain, visual rules, components, and page templates.",
    feature2Title: "Documentation update rules",
    feature2Copy: "Sync related design documents automatically or manually based on code changes.",
    mechanismDetect: "-> Automatic updates",
    mechanismDetectCopy: "After the code-change quiet period ends, sync the affected design documents automatically.",
    mechanismMap: "-> Manual updates",
    mechanismMapCopy: "When the user requests a sync, inspect code changes and update the related content immediately.",
    mechanismPreserve: "-> In-progress state",
    mechanismPreserveCopy: "During active changes, record pending updates without rewriting the formal design documents.",
    declarationSpec: "Feature goals, state flow, and acceptance criteria",
    declarationDomain: "Business objects, terminology, risks, and ownership rules",
    declarationCraft: "Typography, density, feedback, and motion craft",
    declarationDesign: "Color, type, spacing, state tokens, and visual rules",
    declarationComponents: "Component responsibilities, semantic boundaries, and accessibility",
    declarationTemplate: "Page types, app shell, and responsive starting points"
  }
};

const html = document.documentElement;
const metaDescription = document.querySelector('meta[name="description"]');
const metaTheme = document.querySelector('meta[name="theme-color"]');
const languageOptions = document.querySelectorAll("[data-language]");
const themeToggle = document.querySelector("[data-theme-toggle]");
const themeLabel = themeToggle?.querySelector(".theme-label");
const copyButtons = document.querySelectorAll("[data-copy]");
const coffeeDialog = document.querySelector("[data-coffee-dialog]");
const coffeeOpenButton = document.querySelector("[data-coffee-open]");
const coffeeCloseButtons = document.querySelectorAll("[data-coffee-close]");
const featureToggles = document.querySelectorAll("[data-feature-toggle]");

let language = localStorage.getItem("design-spec-book-language") || "zh-CN";
let theme = localStorage.getItem("design-spec-book-theme") || "light";

function t(key) {
  return translations[language][key] || translations["zh-CN"][key] || key;
}

function applyLanguage(nextLanguage) {
  language = translations[nextLanguage] ? nextLanguage : "zh-CN";
  localStorage.setItem("design-spec-book-language", language);
  html.lang = language;

  document.querySelectorAll("[data-i18n]").forEach((element) => {
    element.textContent = t(element.dataset.i18n);
  });
  document.querySelectorAll("[data-i18n-aria]").forEach((element) => {
    element.setAttribute("aria-label", t(element.dataset.i18nAria));
  });
  document.querySelectorAll("[data-i18n-title]").forEach((element) => {
    element.title = t(element.dataset.i18nTitle);
  });
  document.querySelectorAll("[data-i18n-alt]").forEach((element) => {
    element.alt = t(element.dataset.i18nAlt);
  });
  document.querySelectorAll("[data-copy-key]").forEach((element) => {
    element.dataset.copy = t(element.dataset.copyKey);
  });
  if (metaDescription) metaDescription.content = t("documentDescription");
  document.title = t("documentTitle");

  languageOptions.forEach((option) => {
    const active = option.dataset.language === language;
    option.classList.toggle("is-active", active);
    option.setAttribute("aria-pressed", String(active));
  });
  featureToggles.forEach(updateFeatureToggle);
  updateThemeControl();
}

function updateFeatureToggle(featureToggle) {
  if (!featureToggle) return;
  const expanded = featureToggle.getAttribute("aria-expanded") === "true";
  featureToggle.setAttribute("aria-label", t(expanded ? "featureCollapseAria" : "featureExpandAria"));
}

function setFeatureExpanded(featureToggle, expanded) {
  const panel = document.getElementById(featureToggle.getAttribute("aria-controls"));
  featureToggle.setAttribute("aria-expanded", String(expanded));
  if (panel) panel.hidden = !expanded;
  updateFeatureToggle(featureToggle);
}

function updateThemeControl() {
  html.dataset.theme = theme;
  if (metaTheme) metaTheme.content = theme === "dark" ? "#000000" : "#f5f5f5";
  if (!themeToggle) return;
  themeToggle.setAttribute("aria-pressed", String(theme === "dark"));
  themeToggle.setAttribute("aria-label", theme === "dark" ? t("themeToLight") : t("themeToDark"));
  themeToggle.title = theme === "dark" ? t("themeToLight") : t("themeToDark");
  if (themeLabel) themeLabel.textContent = theme === "dark" ? t("themeDark") : t("themeLight");
}

languageOptions.forEach((option) => {
  option.addEventListener("click", () => applyLanguage(option.dataset.language));
});

themeToggle?.addEventListener("click", () => {
  theme = theme === "dark" ? "light" : "dark";
  localStorage.setItem("design-spec-book-theme", theme);
  updateThemeControl();
});

featureToggles.forEach((featureToggle) => {
  featureToggle.addEventListener("click", () => {
    const expanded = featureToggle.getAttribute("aria-expanded") === "true";
    if (!expanded) {
      featureToggles.forEach((otherToggle) => {
        if (otherToggle !== featureToggle) setFeatureExpanded(otherToggle, false);
      });
    }
    setFeatureExpanded(featureToggle, !expanded);
  });
});

copyButtons.forEach((copyButton) => {
  const copyLabel = copyButton.querySelector(".copy-label");
  if (!copyLabel) return;
  const labelKey = copyButton.dataset.copyLabelKey || "copyCommand";
  const copiedLabelKey = copyButton.dataset.copiedLabelKey || "copied";
  const failedLabelKey = copyButton.dataset.copyFailedLabelKey || "copyFailed";
  const copyAriaKey = copyButton.dataset.copyAriaKey || "copyAria";
  const copiedAriaKey = copyButton.dataset.copiedAriaKey || "copiedAria";
  const failedAriaKey = copyButton.dataset.copyFailedAriaKey || "copyFailedAria";
  const setCopyState = (state) => {
    copyButton.classList.toggle("is-copied", state === "copied");
    copyButton.classList.toggle("is-error", state === "error");
    copyLabel.textContent = t(state === "copied" ? copiedLabelKey : state === "error" ? failedLabelKey : labelKey);
    copyButton.setAttribute("aria-label", t(state === "copied" ? copiedAriaKey : state === "error" ? failedAriaKey : copyAriaKey));
  };

  copyButton.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(copyButton.dataset.copy || "");
      setCopyState("copied");
    } catch {
      setCopyState("error");
    }

    window.setTimeout(() => setCopyState("idle"), 2200);
  });
});

function setCoffeeDialog(open) {
  if (!coffeeDialog) return;
  coffeeDialog.hidden = !open;
  coffeeDialog.setAttribute("aria-hidden", String(!open));
  document.body.classList.toggle("dialog-open", open);
  if (open) coffeeDialog.querySelector(".coffee-close")?.focus();
}

coffeeOpenButton?.addEventListener("click", () => setCoffeeDialog(true));
coffeeCloseButtons.forEach((button) => {
  button.addEventListener("click", () => setCoffeeDialog(false));
});
document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && coffeeDialog && !coffeeDialog.hidden) setCoffeeDialog(false);
});

applyLanguage(language);
