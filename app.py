from fastapi import FastAPI
from pydantic import BaseModel
import json
import logging
import os
import time
from datetime import datetime, timezone

app = FastAPI()

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("app")


def log_event(event: str, **fields) -> None:
    payload = {
        "event": event,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "service": os.getenv("RENDER_SERVICE_NAME", "local-dev"),
        **fields,
    }
    logger.info(json.dumps(payload))


@app.middleware("http")
async def log_requests(request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    duration_ms = round((time.perf_counter() - start) * 1000, 2)

    log_event(
        "http_request",
        method=request.method,
        path=request.url.path,
        status_code=response.status_code,
        duration_ms=duration_ms,
    )
    return response


class ChatRequest(BaseModel):
    message: str


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "service": os.getenv("RENDER_SERVICE_NAME", "local-dev"),
    }


@app.post("/chat")
def chat(req: ChatRequest):
    log_event(
        "chat_request",
        message_length=len(req.message),
        mode="starter",
    )

    reply = f"You said: {req.message}"
    log_event(
        "chat_response",
        message_length=len(req.message),
        reply_length=len(reply),
        mode="starter",
    )

    return {
        "reply": reply,
        "mode": "starter",
    }
