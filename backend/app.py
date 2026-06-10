# from fastapi import FastAPI, UploadFile, File
# from fastapi.responses import PlainTextResponse
# from fastapi.middleware.cors import CORSMiddleware
# import pymupdf4llm
# import tempfile
# import os

# app = FastAPI(title="PDF to Markdown API")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.post("/api/convert", response_class=PlainTextResponse)
# async def convert_pdf(file: UploadFile = File(...)):
#     if not file.filename.endswith(".pdf"):
#         return "Erreur : le fichier doit être un PDF."

#     content = await file.read()

#     with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
#         tmp.write(content)
#         tmp_path = tmp.name

#     try:
#         markdown = pymupdf4llm.to_markdown(tmp_path)
#         return markdown
#     finally:
#         os.remove(tmp_path)


from fastapi import FastAPI, UploadFile, File, HTTPException
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


@app.get("/")
def root():
    return {"message": "PDF to Markdown API is running"}


@app.get("/api/health")
def health_check():
    return {"status": "ok"}


@app.post("/api/convert", response_class=PlainTextResponse)
async def convert_pdf(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="Nom de fichier manquant")

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Le fichier doit être un PDF"
        )

    content = await file.read()

    if not content:
        raise HTTPException(
            status_code=400,
            detail="Le fichier PDF est vide"
        )

    tmp_path = None

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(content)
            tmp_path = tmp.name

        markdown = pymupdf4llm.to_markdown(tmp_path)

        if not markdown.strip():
            raise HTTPException(
                status_code=422,
                detail="Aucun texte exploitable trouvé dans le PDF"
            )

        return markdown

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="PDF invalide ou impossible à convertir"
        )

    finally:
        if tmp_path and os.path.exists(tmp_path):
            os.remove(tmp_path)
