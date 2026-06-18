from fastapi import FastAPI
from pydantic import BaseModel
import os
from datetime import datetime

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": os.getenv("RENDER_SERVICE_NAME", "local-dev"),
    }


@app.post("/chat")
def chat(req: ChatRequest):
    return {
        "reply": f"You said: {req.message}",
        "mode": "starter",
    }
