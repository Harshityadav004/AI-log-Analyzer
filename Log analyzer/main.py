import os
import re
from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv

# 1. Load environment variables before executing anything else
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path=env_path)

from google import genai

# Fallback setup to guarantee the server never crashes on launch due to a missing key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    client = genai.Client(api_key="PLACEHOLDER_KEY") 
else:
    client = genai.Client()

app = FastAPI()

# 2. Configure paths for the templates folder
templates_path = os.path.join(BASE_DIR, "templates")
templates = Jinja2Templates(directory=templates_path)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Renders the main dashboard upload screen."""
    # PYTHON 3.14 FIX: Explicitly name keyword arguments to match new Starlette parameters
    return templates.TemplateResponse(
        request=request, 
        name="index.html"
    )

@app.post("/analyze-log", response_class=HTMLResponse)
async def analyze_log(request: Request, file: UploadFile = File(...)):
    """Reads the uploaded log file, filters key content, and gets AI feedback."""
    current_key = os.getenv("GEMINI_API_KEY")
    if not current_key or "your_actual_copied_api_key_here" in current_key:
        return HTMLResponse(content="<h1 style='color:red; font-family:sans-serif; text-align:center; margin-top:50px;'>Error: Please paste your real Gemini API Key inside the .env file!</h1>")

    try:
        contents = await file.read()
        log_text = contents.decode("utf-8")
        
        error_lines = []
        for line in log_text.splitlines():
            if re.search(r'(ERROR|CRITICAL|FAILED|500|404|unauthorized|warning)', line, re.IGNORECASE):
                error_lines.append(line)
        
        filtered_logs = "\n".join(error_lines[:40])
        if not filtered_logs:
            filtered_logs = log_text[:1000]

        analysis_prompt = f"""
        You are an expert DevOps and Network Security Engineer reviewing server log outputs.
        Review the following filtered log entries:
        {filtered_logs}
        
        Please provide a highly structured analysis in clean HTML format (using basic paragraph, heading, and list tags). Cover:
        1. Identification of major issues.
        2. Root cause determination.
        3. Step-by-step resolution path.
        """

        response = client.models.generate_content(
            model='gemini-3.8-flash',
            contents=analysis_prompt,
        )
        ai_report = response.text

    except Exception as e:
        ai_report = f"<p style='color:red; font-weight:bold;'>Error executing analysis engine: {str(e)}</p>"

    # PYTHON 3.14 FIX: Explicitly name keyword arguments to match new Starlette parameters
    return templates.TemplateResponse(
        request=request, 
        name="report.html", 
        context={
            "filename": str(file.filename), 
            "report_content": str(ai_report)
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
