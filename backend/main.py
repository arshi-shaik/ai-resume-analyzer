from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

import fitz

from analyzer import calculate_match, extract_skills


app = FastAPI(
    title="AI Resume Analyzer",
    description="Analyze resumes and compare them with job descriptions",
    version="1.0.0"
)


# Allow requests from our React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def home():
    return {
        "message": "AI Resume Analyzer API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "OK"
    }


def extract_pdf_text(file_bytes):
    """
    Extract text from an uploaded PDF file.
    """

    document = fitz.open(
        stream=file_bytes,
        filetype="pdf"
    )

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text


@app.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    """
    Analyze an uploaded resume against
    a given job description.
    """

    # Read the uploaded PDF
    file_bytes = await resume.read()

    # Extract text from PDF
    resume_text = extract_pdf_text(
        file_bytes
    )

    # Find skills in resume
    resume_skills = extract_skills(
        resume_text
    )

    # Compare resume with job description
    result = calculate_match(
        resume_text,
        job_description
    )

    return {
        "filename": resume.filename,

        "resume_skills": resume_skills,

        "match_percentage":
            result["match_percentage"],

        "matched_skills":
            result["matched_skills"],

        "missing_skills":
            result["missing_skills"]
    }
