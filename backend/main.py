from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

import fitz

from analyzer import calculate_match, extract_skills


app = FastAPI(
    title="AI Resume Analyzer",
    description="Analyze resumes and compare them with job descriptions
