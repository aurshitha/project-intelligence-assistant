from fastapi import FastAPI
from pydantic import BaseModel

from app.rag.rag_pipeline import RAGPipeline

app = FastAPI()

rag = RAGPipeline()

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
def ask(req: QueryRequest):

    answer = rag.answer(
        req.question
    )

    return {
        "answer": answer
    }