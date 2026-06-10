from fastapi import FastAPI, UploadFile, File
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
import pymupdf4llm
import tempfile
import os

app = FastAPI(title="PDF to Markdown API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/convert", response_class=PlainTextResponse)
async def convert_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        return "Erreur : le fichier doit être un PDF."

    content = await file.read()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(content)
        tmp_path = tmp.name

    try:
        markdown = pymupdf4llm.to_markdown(tmp_path)
        return markdown
    finally:
        os.remove(tmp_path)
