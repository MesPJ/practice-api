# practice-api

Small FastAPI practice app: health check + in-memory items CRUD.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install fastapi uvicorn pytest httpx
```

## Run the API

```powershell
uvicorn main:app --reload
```

- Health: http://127.0.0.1:8000/health
- Docs: http://127.0.0.1:8000/health

## Run tests

```powershell
pytest
```

## API overview

| Method | Path | What it does |
|--------|------|----------------|
| GET | `/health` | `{"status": "ok"}` |
| GET | `/items` | list items |
| POST | `/items` | create item (JSON body) |
| GET | `/items/{id}` | get one item by index |