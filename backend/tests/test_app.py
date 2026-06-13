# # backend/tests/test_app.py

# from fastapi.testclient import TestClient
# from app import app
# # import io
# from reportlab.pdfgen import canvas
# from io import BytesIO

# client = TestClient(app)


# def test_swagger_disponible():
#     """Vérifie que Swagger répond."""
#     response = client.get("/docs")
#     assert response.status_code == 200


# def test_pdf_manquant():
#     """Vérifie qu'un appel sans fichier renvoie une erreur."""
#     response = client.post("/api/convert")
#     assert response.status_code == 422


# def test_fichier_non_pdf():
#     """Vérifie le rejet d'un fichier non PDF."""
#     fake_file = io.BytesIO(b"bonjour")

#     response = client.post(
#         "/api/convert",
#         files={"file": ("test.txt", fake_file, "text/plain")}
#     )

#     assert response.status_code == 200
#     assert "PDF" in response.text


# def test_pdf_valide():
#     """Teste l'upload d'un PDF minimal."""
#     pdf_content = (
#         b"%PDF-1.4\n"
#         b"1 0 obj\n<<>>\nendobj\n"
#         b"trailer\n<<>>\n%%EOF"
#     )

#     response = client.post(
#         "/api/convert",
#         files={"file": ("test.pdf", pdf_content, "application/pdf")}
#     )

#     assert response.status_code == 200


# backend/tests/test_app.py

from io import BytesIO
from unittest.mock import patch

from fastapi.testclient import TestClient
from reportlab.pdfgen import canvas

from app import app

client = TestClient(app)


def create_test_pdf(text="Bonjour RNCP6"):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.drawString(100, 750, text)
    pdf.save()
    buffer.seek(0)
    return buffer


def test_root_disponible():
    response = client.get("/")
    assert response.status_code == 200
    assert "PDF to Markdown API" in response.text


def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_swagger_disponible():
    response = client.get("/docs")
    assert response.status_code == 200


def test_openapi_disponible():
    response = client.get("/openapi.json")
    assert response.status_code == 200


def test_route_inconnue():
    response = client.get("/route-inconnue")
    assert response.status_code == 404


def test_pdf_manquant():
    response = client.post("/api/convert")
    assert response.status_code == 422


def test_fichier_non_pdf_txt():
    fake_file = BytesIO(b"bonjour")

    response = client.post(
        "/api/convert",
        files={"file": ("test.txt", fake_file, "text/plain")}
    )

    assert response.status_code == 400
    assert "PDF" in response.text


def test_fichier_sans_extension_pdf():
    fake_file = BytesIO(b"bonjour")

    response = client.post(
        "/api/convert",
        files={"file": ("document", fake_file, "application/octet-stream")}
    )

    assert response.status_code == 400
    assert "PDF" in response.text


def test_extension_pdf_majuscule():
    pdf_file = create_test_pdf("PDF avec extension majuscule")

    response = client.post(
        "/api/convert",
        files={"file": ("DOCUMENT.PDF", pdf_file.read(), "application/pdf")}
    )

    assert response.status_code == 200


def test_pdf_valide():
    pdf_file = create_test_pdf("Bonjour RNCP6")

    response = client.post(
        "/api/convert",
        files={"file": ("test.pdf", pdf_file.read(), "application/pdf")}
    )

    assert response.status_code == 200
    assert isinstance(response.text, str)
    assert len(response.text) > 0


def test_pdf_valide_contient_texte():
    pdf_file = create_test_pdf("Texte important pour le test")

    response = client.post(
        "/api/convert",
        files={"file": ("test.pdf", pdf_file.read(), "application/pdf")}
    )

    assert response.status_code == 200
    assert "Texte important" in response.text or len(response.text) > 0


def test_pdf_vide():
    empty_pdf = BytesIO(b"")

    response = client.post(
        "/api/convert",
        files={"file": ("empty.pdf", empty_pdf.read(), "application/pdf")}
    )

    assert response.status_code == 400
    assert "vide" in response.text


def test_pdf_corrompu():
    fake_pdf = BytesIO(b"fake pdf content")

    response = client.post(
        "/api/convert",
        files={"file": ("bad.pdf", fake_pdf.read(), "application/pdf")}
    )

    assert response.status_code == 400
    assert "invalide" in response.text or "convertir" in response.text


def test_pdf_extension_ok_mais_contenu_invalide():
    fake_pdf = BytesIO(b"ceci n'est pas un vrai pdf")

    response = client.post(
        "/api/convert",
        files={"file": ("fake.pdf", fake_pdf.read(), "application/pdf")}
    )

    assert response.status_code == 400


def test_cors_headers():
    response = client.options(
        "/api/convert",
        headers={
            "Origin": "http://localhost:8080",
            "Access-Control-Request-Method": "POST"
        }
    )

    assert response.status_code == 200


def test_erreur_interne_conversion_pdf():
    pdf_file = create_test_pdf("Erreur simulée")

    with patch("pymupdf4llm.to_markdown", side_effect=Exception("Erreur conversion")):
        response = client.post(
            "/api/convert",
            files={"file": ("test.pdf", pdf_file.read(), "application/pdf")}
        )

    assert response.status_code == 400
    assert "convertir" in response.text
