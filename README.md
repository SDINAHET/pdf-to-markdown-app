# pdf-to-markdown-app
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
* RNCP dossiers
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

GitHub:
https://github.com/SDINAHET

LinkedIn:
https://www.linkedin.com/in/st%C3%A9phane-dinahet-3b363189/

Portfolio:
https://sdinahet.github.io/SDINAHET/

---

## License

This project is released under the MIT License.

Feel free to use, modify and distribute it.


Frontend : http://localhost:8080
Backend  : http://localhost:8000/docs
