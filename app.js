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
    lead: "把产品意图、业务语义和视觉规则保存成一套可以被 Agent 继续读取的设计上下文。",
    installationLabel: "01 / 安装",
    installationTitle: "安装",
    copyAria: "复制安装命令",
    copyCommand: "复制命令",
    copied: "已复制",
    copyFailed: "复制失败",
    footerBuildBy: "Build by ",
    footerSupportPrefix: "，如果对你有帮助，也欢迎请我",
    coffeeAction: "喝杯咖啡",
    coffeeOpenAria: "打开喝杯咖啡窗口",
    coffeeDialogAria: "请我喝杯咖啡",
    coffeeCloseAria: "关闭喝杯咖啡窗口",
    coffeeImageAlt: "支付宝喝杯咖啡图片",
    usagePrefix: "然后输入",
    usageSuffix: "，为当前项目生成并同步六份设计声明。",
    usageLabel: "02 / 使用说明",
    usageTitle: "这样使用",
    usage1Title: "第一次使用",
    usage1Copy: "为当前项目生成六份设计说明。",
    usage1Prompt: "使用 $design-spec-book，为当前项目生成六份设计说明。",
    usage2Title: "同步项目变化",
    usage2Copy: "读取最新代码，只更新对应的设计事实。",
    usage2Prompt: "使用 $design-spec-book，把当前代码同步到设计说明中。",
    usage3Title: "调整设计规则",
    usage3Copy: "指定页面或组件，更新它的视觉和交互规则。",
    usage3Prompt: "使用 $design-spec-book，更新结算页面的设计规则。",
    featuresLabel: "03 / 它能做什么",
    featuresTitle: "为项目建立设计上下文",
    feature1Title: "生成六份设计说明",
    feature1Copy: "按功能、业务、视觉、组件与页面模板分别整理。",
    feature2Title: "从代码中同步内容",
    feature2Copy: "读取项目入口、组件、样式和 token，更新对应文档。",
    feature3Title: "保留你的设计决定",
    feature3Copy: "只更新受管区块，你手写的内容始终保留。",
    declarationsLabel: "04 / 六份声明",
    declarationsTitle: "六份文档",
    declarationsNote: "每份回答一个问题",
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
    lead: "Keep product intent, domain language, and visual rules in a design context an Agent can read and continue using.",
    installationLabel: "01 / INSTALLATION",
    installationTitle: "Install",
    copyAria: "Copy installation command",
    copyCommand: "COPY COMMAND",
    copied: "COPIED",
    copyFailed: "COPY FAILED",
    footerBuildBy: "Build by ",
    footerSupportPrefix: ". If this helped, you're welcome to share a ",
    coffeeAction: "coffee",
    coffeeOpenAria: "Open coffee support dialog",
    coffeeDialogAria: "Support with coffee",
    coffeeCloseAria: "Close coffee support dialog",
    coffeeImageAlt: "Alipay coffee support QR code",
    usagePrefix: "Then enter",
    usageSuffix: " to generate and sync six design declarations for the current project.",
    usageLabel: "02 / USAGE",
    usageTitle: "How to use it",
    usage1Title: "Start a project",
    usage1Copy: "Create the six design documents for the current project.",
    usage1Prompt: "Use $design-spec-book to create the six design documents for this project.",
    usage2Title: "Sync project changes",
    usage2Copy: "Read the latest code and update only the relevant design facts.",
    usage2Prompt: "Use $design-spec-book to sync the current codebase into the design documents.",
    usage3Title: "Update design rules",
    usage3Copy: "Name a page or component to update its visual and interaction rules.",
    usage3Prompt: "Use $design-spec-book to update the design rules for the checkout page.",
    featuresLabel: "03 / WHAT IT DOES",
    featuresTitle: "Build design context for a project",
    feature1Title: "Creates six design documents",
    feature1Copy: "Organizes product behavior, domain, visual rules, components, and page templates.",
    feature2Title: "Syncs from your codebase",
    feature2Copy: "Reads entry points, components, styles, and tokens, then updates the relevant documents.",
    feature3Title: "Keeps your decisions intact",
    feature3Copy: "Updates managed blocks only; content you write stays where it is.",
    declarationsLabel: "04 / SIX DECLARATIONS",
    declarationsTitle: "Six documents",
    declarationsNote: "ONE QUESTION EACH",
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
const copyButton = document.querySelector("[data-copy]");
const copyLabel = copyButton?.querySelector(".copy-label");
const coffeeDialog = document.querySelector("[data-coffee-dialog]");
const coffeeOpenButton = document.querySelector("[data-coffee-open]");
const coffeeCloseButtons = document.querySelectorAll("[data-coffee-close]");

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
  if (metaDescription) metaDescription.content = t("documentDescription");
  document.title = t("documentTitle");

  languageOptions.forEach((option) => {
    const active = option.dataset.language === language;
    option.classList.toggle("is-active", active);
    option.setAttribute("aria-pressed", String(active));
  });
  updateThemeControl();
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

copyButton?.addEventListener("click", async () => {
  try {
    await navigator.clipboard.writeText(copyButton.dataset.copy);
    copyLabel.textContent = t("copied");
  } catch {
    copyLabel.textContent = t("copyFailed");
  }

  window.setTimeout(() => {
    copyLabel.textContent = t("copyCommand");
  }, 2200);
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
