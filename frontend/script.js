// let markdownContent = "";

// document.getElementById("convert-btn").addEventListener("click", async () => {
//   const fileInput = document.getElementById("pdf-file");
//   const file = fileInput.files[0];

//   if (!file) {
//     alert("Choisis un PDF.");
//     return;
//   }

//   const formData = new FormData();
//   formData.append("file", file);

//   const response = await fetch("http://localhost:8000/api/convert", {
//     method: "POST",
//     body: formData
//   });

//   markdownContent = await response.text();
//   document.getElementById("markdown-output").value = markdownContent;
// });

// document.getElementById("download-btn").addEventListener("click", () => {
//   const blob = new Blob([markdownContent], { type: "text/markdown" });
//   const url = URL.createObjectURL(blob);

//   const a = document.createElement("a");
//   a.href = url;
//   a.download = "document_converti.md";
//   a.click();

//   URL.revokeObjectURL(url);
// });

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

  try {

    const API_BASE =
      (
        location.hostname === "localhost" ||
        location.hostname === "127.0.0.1" ||
        location.hostname.startsWith("192.168.")
      )
        ? "http://localhost:8000"
        : "";

    const response = await fetch(`${API_BASE}/api/convert`, {
      method: "POST",
      body: formData
    });

    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(errorText || `Erreur HTTP ${response.status}`);
    }

    markdownContent = await response.text();

    document.getElementById("markdown-output").value =
      markdownContent;

  } catch (error) {

    console.error(error);

    alert(
      "Erreur lors de la conversion du PDF :\n\n" +
      error.message
    );
  }
});

document.getElementById("download-btn").addEventListener("click", () => {

  if (!markdownContent) {
    alert("Aucun contenu à télécharger.");
    return;
  }

  const blob = new Blob(
    [markdownContent],
    { type: "text/markdown;charset=utf-8" }
  );

  const url = URL.createObjectURL(blob);

  const a = document.createElement("a");
  a.href = url;
  a.download = "document_converti.md";

  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);

  URL.revokeObjectURL(url);
});
