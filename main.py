from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import google.generativeai as genai

api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is missing")

genai.configure(api_key=api_key)

app = FastAPI()

# ✅ CORS (الحل الأساسي)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Req(BaseModel):
    prompt: str

@app.post("/ask")
def ask(req: Req):
    try:
        model = genai.GenerativeModel("models/gemini-2.5-flash-lite")
        response = model.generate_content(req.prompt)
        return {"answer": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
