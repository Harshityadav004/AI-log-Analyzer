# AI Log Analyzer 🌐🤖

An advanced, asynchronous AI-powered DevOps and Network Security tool built with **FastAPI**. This application automatically ingests raw server network logs, extracts anomalous activity using optimized regular expressions (Regex), and interfaces with the **Google Gemini 3.8 Flash API** to generate automated diagnostic reports, root-cause assessments, and step-by-step system remediation paths.

---

## 🚀 Core Features

* **Modern DevOps Slate UI:** A polished, fully responsive Tailwind-inspired dark-mode interface designed for infrastructure engineers.
* **Smart Extension Filtering:** Frontend-restricted inputs natively validating and allowing only standard `.log` and `.txt` file streams.
* **Regex Filtering Engine:** Automatically parses raw file streams to extract high-priority security and system markers (`ERROR`, `CRITICAL`, `FAILED`, `500`, `404`, `unauthorized`).
* **Asynchronous Processing Engine:** Leverages FastAPI and Starlette's async runtime handles for ultra-fast, non-blocking file handling.
* **Gemini 3.8 Flash Integration:** Connects directly to Google's next-generation AI model to evaluate logs and format structured, HTML-rendered diagnostics.
* **Python 3.14 Code Compliance:** Future-proofed with explicit template parameters ensuring long-term syntax stability across modern library releases.

---

## 🛠️ Tech Stack

* **Backend Engine:** FastAPI (Asynchronous Python Web Framework)
* **ASGI Server:** Uvicorn
* **AI Integration:** Google GenAI SDK (`gemini-3.8-flash`)
* **Templating System:** Jinja2 Templates (HTML5 + Embedded Stylesheets)
* **Configuration:** Python-dotenv

---

## 📋 Prerequisites

Ensure you have the following system requirements set up on your machine before installing:
* **Python:** Version 3.8 up to 3.14 (fully verified)
* **Credentials:** A valid Gemini API Key obtained from [Google AI Studio](https://google.com)

---

## ⚙️ Installation & Local Setup

### 1. Clone the Repository
```bash
git clone https://github.com
cd AI-log-Analyzer
```

### 2. Install Project Dependencies
Run the following package command to install all framework elements:
```bash
pip install fastapi uvicorn jinja2 python-dotenv google-genai
```

### 3. Setup Secret Keys (`.env`)
Create a file named exactly `.env` in the root folder directory of the project. **Never commit this file to public repositories!**
```env
GEMINI_API_KEY=your_actual_copied_api_key_here
```

---

## 💻 Running the Application

1. Spin up the localized Uvicorn engine execution script:
   ```bash
   python main.py
   ```
2. Once the console launches, access the graphical interface inside your browser at:
   ```text
   http://127.0.0.1:8000
   ```
3. Click the upload block, select a target log file, and press **Execute AI Analysis** to retrieve your immediate network audit report.

---

## 🔒 Security & Privacy Policy

This project strictly enforces credential isolation. The application uses `python-dotenv` variables to look for local key chains locally. A specialized configuration system prevents mock/placeholder string evaluations inside production endpoints to completely block unauthorized service access.
