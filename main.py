from fastapi import FastAPI
from pydantic import BaseModel
import os
import google.generativeai as genai

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

app = FastAPI()

class Req(BaseModel):
    prompt: str

@app.post("/ask")
def ask(req: Req):
    model = genai.GenerativeModel("gemini-pro")
    r = model.generate_content(req.prompt)
    return {"answer": r.text}
