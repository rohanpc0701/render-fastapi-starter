# FastAPI Render Starter

Minimal FastAPI app for deploying to [Render](https://render.com).

## Local setup

```bash
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
uvicorn app:app --reload
```

Test:

- http://127.0.0.1:8000/health
- http://127.0.0.1:8000/docs

## GitHub

```bash
git init
git add .
git commit -m "Initial FastAPI Render starter"
git remote add origin <your-repo-url>
git push -u origin main
```

## Render Web Service settings

| Field | Value |
|-------|-------|
| **Runtime** | Python |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn --bind 0.0.0.0:$PORT --workers 2 --timeout 120 --worker-class uvicorn.workers.UvicornWorker app:app` |
| **Health Check Path** | `/health` |

After deploy, test `/health`, `/docs`, and `/chat` on your Render service URL.
