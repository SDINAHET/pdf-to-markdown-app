let markdownContent = "";

document.getElementById("convert-btn").addEventListener("click", async () => {
  const fileInput = document.getElementById("pdf-file");
  const file = fileInput.files[0];

  if (!file) {
    alert("Choisis un PDF.");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch("http://localhost:8000/api/convert", {
    method: "POST",
    body: formData
  });

  markdownContent = await response.text();
  document.getElementById("markdown-output").value = markdownContent;
});

document.getElementById("download-btn").addEventListener("click", () => {
  const blob = new Blob([markdownContent], { type: "text/markdown" });
  const url = URL.createObjectURL(blob);

  const a = document.createElement("a");
  a.href = url;
  a.download = "document_converti.md";
  a.click();

  URL.revokeObjectURL(url);
});
