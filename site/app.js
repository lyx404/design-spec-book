const copyButton = document.querySelector("[data-copy]");

if (copyButton) {
  copyButton.addEventListener("click", async () => {
    const command = copyButton.dataset.copy;
    const label = copyButton.querySelector(".copy-label");
    try {
      await navigator.clipboard.writeText(command);
      label.textContent = "Copied";
      copyButton.setAttribute("aria-label", "安装命令已复制");
    } catch {
      label.textContent = "Select";
      copyButton.setAttribute("aria-label", "无法自动复制，请选择命令");
    }
    window.setTimeout(() => {
      label.textContent = "Copy";
      copyButton.setAttribute("aria-label", "复制安装命令");
    }, 2200);
  });
}
