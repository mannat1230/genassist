from fastapi import FastAPI, Form
from pydantic import BaseModel
from app.summarizer import generate_summary

app = FastAPI()

class SummarizeRequest(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "GenAssist API is live"}

@app.post("/summarize/")
def summarize(request: SummarizeRequest):
    summary = generate_summary(request.text)
    return {"summary": summary}