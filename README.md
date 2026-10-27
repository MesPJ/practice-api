# practice-api

Small FastAPI practice app: health check + in-memory items CRUD.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install fastapi uvicorn pytest httpx

(Or pip install -r requirements.txt if you have one.)

## Run the API

uvicorn main:app --reload

Health: /health
Docs: /docs

## Run tests

pytest

## API overview

Method	Path	    What it does
GET     /health	    {"status": "ok"}
GET	    /items	    list items
POST	/items	    create item (JSON body)
GET	    /items/{id}	get one item by index