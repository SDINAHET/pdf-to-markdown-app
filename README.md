<!-- [![Tests Python, Coverage and Docker](https://github.com/SDINAHET/pdf-to-markdown-app/actions/workflows/tests.yml/badge.svg)](https://github.com/SDINAHET/pdf-to-markdown-app/actions/workflows/tests.yml) -->

<!-- ![Coverage](https://img.shields.io/badge/coverage-80%25%2B-brightgreen) -->


<!-- [![Tests Python, Coverage and Docker](https://github.com/SDINAHET/pdf-to-markdown-app/actions/workflows/tests.yml/badge.svg)](https://github.com/SDINAHET/pdf-to-markdown-app/actions/workflows/tests.yml) -->

<!-- [![codecov](https://codecov.io/gh/SDINAHET/pdf-to-markdown-app/graph/badge.svg)](https://codecov.io/gh/SDINAHET/pdf-to-markdown-app) -->


# pdf-to-markdown-app

[![Tests Python, Coverage and Docker](https://github.com/SDINAHET/pdf-to-markdown-app/actions/workflows/tests.yml/badge.svg)](https://github.com/SDINAHET/pdf-to-markdown-app/actions/workflows/tests.yml)

![GitHub last commit](https://img.shields.io/github/last-commit/SDINAHET/pdf-to-markdown-app)
![GitHub repo size](https://img.shields.io/github/repo-size/SDINAHET/pdf-to-markdown-app)
![GitHub language count](https://img.shields.io/github/languages/count/SDINAHET/pdf-to-markdown-app)
![GitHub top language](https://img.shields.io/github/languages/top/SDINAHET/pdf-to-markdown-app)
![GitHub issues](https://img.shields.io/github/issues/SDINAHET/pdf-to-markdown-app)
![GitHub pull requests](https://img.shields.io/github/issues-pr/SDINAHET/pdf-to-markdown-app)
![GitHub forks](https://img.shields.io/github/forks/SDINAHET/pdf-to-markdown-app)
![GitHub stars](https://img.shields.io/github/stars/SDINAHET/pdf-to-markdown-app)
![GitHub watchers](https://img.shields.io/github/watchers/SDINAHET/pdf-to-markdown-app)
![GitHub license](https://img.shields.io/github/license/SDINAHET/pdf-to-markdown-app)

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Pytest](https://img.shields.io/badge/Pytest-Tested-brightgreen)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![Docker Compose](https://img.shields.io/badge/Docker_Compose-Ready-blue)
![Nginx](https://img.shields.io/badge/Nginx-Frontend-green)
![Coverage](https://img.shields.io/badge/Coverage-80%25%2B-brightgreen)
![Status](https://img.shields.io/badge/Status-Active-success)
![Maintenance](https://img.shields.io/badge/Maintained-Yes-success)


Application web permettant de convertir des fichiers PDF en Markdown afin de réduire le nombre de tokens utilisés par les IA. L’utilisateur dépose un PDF, le contenu est extrait et converti automatiquement en Markdown, puis affiché et téléchargeable au format .md.

# PDF to Markdown Converter

## Overview

PDF to Markdown Converter is a lightweight full-stack web application designed to convert PDF documents into clean Markdown files.

The project aims to simplify the preparation of documents for Large Language Models (LLMs) such as Claude, ChatGPT, Ollama, Mistral, Llama, and other AI systems by reducing token consumption and improving text readability.

Users can upload a PDF document through a web interface, automatically convert it into Markdown format, preview the result, and download the generated `.md` file.

---

## Features

### Current Features

* PDF upload through a web interface
* Drag and drop support
* Automatic PDF to Markdown conversion
* Markdown preview in the browser
* Markdown file download
* REST API powered by FastAPI
* Dockerized deployment
* Responsive user interface

### Planned Features

* Direct integration with Ollama
* Automatic document summarization
* Markdown cleanup and optimization
* Multi-file batch conversion
* OCR support for scanned PDFs
* AI-assisted document analysis
* Export to TXT, DOCX and HTML
* Authentication and user management

---

## Architecture

```text
┌──────────────────┐
│     Frontend     │
│ HTML / CSS / JS  │
└────────┬─────────┘
         │ HTTP
         ▼
┌──────────────────┐
│ FastAPI Backend  │
│ Python 3.12      │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ PyMuPDF4LLM      │
│ PDF Extraction   │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Markdown Output  │
└──────────────────┘
```

---

## Technology Stack

### Backend

* Python 3.12
* FastAPI
* Uvicorn
* PyMuPDF4LLM
* Python Multipart

### Frontend

* HTML5
* CSS3
* JavaScript (Vanilla JS)

### DevOps

* Docker
* Docker Compose
* Nginx

---

## Project Structure

```text
pdf-to-markdown-app/
│
├── docker-compose.yml
│
├── backend/
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   └── uploads/
│
└── frontend/
    ├── index.html
    ├── style.css
    └── script.js
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/SDINAHET/pdf-to-markdown-app.git

cd pdf-to-markdown-app
```

---

## Local Installation

### Backend

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r backend/requirements.txt
```

Run FastAPI:

```bash
cd backend

uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

Backend available at:

```text
http://localhost:8000
```

Swagger documentation:

```text
http://localhost:8000/docs
```

---

## Docker Deployment

Build and start containers:

```bash
docker compose up --build -d
```

Check running containers:

```bash
docker ps
```

Stop containers:

```bash
docker compose down
```

---

## API Endpoints

### Convert PDF

```http
POST /api/convert
```

Request:

```multipart/form-data
file=<pdf_file>
```

Response:

```text
Markdown content
```

Example:

```bash
curl -X POST \
  -F "file=@document.pdf" \
  http://localhost:8000/api/convert
```

---

## Security Considerations

The application implements several security best practices:

* File type validation
* Temporary file handling
* Automatic cleanup after conversion
* No file persistence by default
* Docker container isolation
* CORS configuration

Future improvements:

* Rate limiting
* User authentication
* Antivirus scanning
* Upload size restrictions
* Audit logging

---

## Use Cases

### AI Prompt Optimization

Convert large PDF documents into Markdown before sending them to:

* Claude
* ChatGPT
* Ollama
* Mistral
* Gemini
* Llama

Benefits:

* Lower token consumption
* Faster processing
* Better text structure
* Reduced context size

### Documentation

* Technical specifications
* Project documentation
* Reports
* Research papers
* User manuals

---

## Performance

Typical performance on a modern workstation:

| Document Size | Conversion Time |
| ------------- | --------------- |
| 1 MB          | < 1 second      |
| 10 MB         | 1-3 seconds     |
| 50 MB         | 5-10 seconds    |

Performance depends on:

* PDF complexity
* Number of pages
* Embedded images
* Available CPU and RAM

---

## Future Roadmap

### Version 1.1

* Drag and drop improvements
* Better Markdown formatting
* Error handling enhancements

### Version 1.2

* Ollama integration
* Automatic summarization
* Markdown cleanup

### Version 2.0

* OCR support
* User accounts
* Conversion history
* AI document analysis

---

## Author

**Stéphane Dinahet**

Full Stack Developer

---

## License

This project is released under the MIT License.

Feel free to use, modify and distribute it.


Frontend : http://localhost:8080
Backend  : http://localhost:8000/docs


Tests automatisés exécutables localement ou dans Docker avec objectif de couverture minimale de 80 %.
Pour lancer uniquement les tests :
```bash
docker compose --profile test run --rm pdf-to-md-tests
docker compose --profile test run --rm pdf-to-md-tests pytest --cov=app --cov-report=term-missing --cov-fail-under=80
```

Pour lancer l’app normalement :
```bash
docker compose up --build
```

```
GET  /                 → test accueil
GET  /api/health       → test santé API
POST /api/convert      → conversion PDF
PDF invalide           → 400 propre
PDF vide               → 400 propre
fichier non PDF        → 400 propre
PDF sans texte         → 422 propre
```

```bash
docker compose build --no-cache pdf-to-md-tests
docker compose --profile test run --rm pdf-to-md-tests
docker compose --profile test run --rm --build pdf-to-md-tests
```

## Project Structure

```text
pdf-to-markdown-app/
│
├── docker-compose.yml
├── README.md
│
├── backend/
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   │
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_app.py
│   │
│   ├── htmlcov/
│   │   ├── index.html
│   │   └── ...
│   │
│   └── uploads/
│
└── frontend/
    ├── index.html
    ├── style.css
    ├── script.js
    └── favicon.ico
```

### Backend

The backend is built with FastAPI and exposes REST endpoints used to convert PDF documents into Markdown format.

Responsibilities:

* File upload handling
* PDF validation
* PDF to Markdown conversion
* Error handling
* API documentation (Swagger/OpenAPI)
* Test execution and coverage reporting

### Frontend

The frontend provides a lightweight user interface allowing users to:

* Upload PDF documents
* Preview generated Markdown
* Download Markdown files
* Interact with the conversion API

### Automated Tests

The project includes automated tests using Pytest.

Test coverage currently includes:

* API availability
* Swagger documentation
* OpenAPI specification
* Health check endpoint
* Missing file validation
* Invalid file type validation
* Empty PDF handling
* Corrupted PDF handling
* Valid PDF conversion
* CORS verification
* Internal exception handling

Coverage report:

```text
Tests executed : 16
Tests passed   : 16
Coverage       : 92.11 %
Target         : 80 %
Status         : PASSED
```

Coverage reports are automatically generated inside:

```text
backend/htmlcov/
```

and can be viewed through:

```text
backend/htmlcov/index.html
```

### Docker Services

```text
pdf-to-md-api
├── FastAPI application
└── Port 8000

pdf-to-md-front
├── Nginx static frontend
└── Port 8080

pdf-to-md-tests
├── Pytest execution
├── Coverage report generation
└── Minimum coverage threshold: 80%
```

