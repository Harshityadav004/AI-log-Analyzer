# AI Log Analyzer 🌐🤖

An AI-powered DevOps tool that automatically parses server network logs using regular expressions (Regex) and evaluates security vulnerabilities, anomalies, or system errors using the Google Gemini API.

## 🚀 Features
* **Regex Log Parsing:** Efficiently scans and extracts structured data from messy, high-volume server logs.
* **AI-Powered Diagnostics:** Leverages the **Google Gemini API** to analyze system issues and explain them in plain language.
* **Security Evaluation:** Instantly flags potential vulnerabilities (e.g., brute-force attempts, unauthorized access).
* **Actionable Recommendations:** Provides DevOps-focused steps to resolve identified system issues.

## 🛠️ Tech Stack
* **Language:** Python
* **Frontend/Interface:** HTML5 / CSS3 *(if applicable, or remove this line)*
* **AI Model:** Google Gemini API

## 📋 Prerequisites
Before running this project, ensure you have the following installed:
* Python 3.8 or higher
* A Gemini API key from Google AI Studio

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd AI-log-Analyzer
   ```

2. **Install required dependencies:**
   ```bash
   pip install google-generativeai
   ```
   *(Note: Add any other dependencies you used, like Flask or custom libraries)*

3. **Configure Environment Variables:**
   Create a `.env` file in the root directory of your project on your local machine (**Do not commit this file to GitHub!**):
   ```env
   GEMINI_API_KEY=your_actual_api_key_here
   ```

## 💻 How to Use

1. Place your target server log file (e.g., `server.log`) in the project directory.
2. Run the main analysis script:
   ```bash
   python main.py
   ```
3. Check the console output or the generated report file for the AI-generated DevOps summary and vulnerability analysis.

## 🔒 Security & Privacy
This repository strictly ignores local `.env` configuration files to ensure secret API keys remain secure and are never exposed publicly.
