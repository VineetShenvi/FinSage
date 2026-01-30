from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

from fastapi import FastAPI
from pydantic import BaseModel

from app.graph.investment_graph import build_graph

app = FastAPI()
graph = build_graph()

class Request(BaseModel):
    company: str

@app.post("/analyze")
def analyze(req: Request):
    state = {
        "company": req.company,
        "retry_count": 0,
        "max_retries": 2
    }

    result = graph.invoke(state)

    return {
        "financial_analysis": result["financial_analysis"],
        "investment_thesis": result["thesis"],
        "approved": result["approved"],
        "retries": result["retry_count"]
    }

