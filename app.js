const copyButton = document.querySelector("[data-copy]");
const status = document.querySelector(".command-status");

if (copyButton && status) {
  copyButton.addEventListener("click", async () => {
    const label = copyButton.querySelector(".copy-label");

    try {
      await navigator.clipboard.writeText(copyButton.dataset.copy);
      label.textContent = "COPIED";
      status.textContent = "COPIED";
      status.style.color = "var(--accent)";
    } catch {
      label.textContent = "SELECT";
      status.textContent = "COPY FAILED";
      status.style.color = "var(--accent)";
    }

    window.setTimeout(() => {
      label.textContent = "COPY COMMAND";
      status.textContent = "READY";
      status.style.color = "";
    }, 2200);
  });
}
