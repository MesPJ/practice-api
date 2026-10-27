from fastapi import FastAPI

app = FastAPI()

items = []

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/items")
def get_items():
    return items

@app.post("/items")
def create_item(item: dict):
    items.append(item)
    return item

@app.get("/items/{id}")
def get_item(id: int):
    if id < 0 or id >= len(items):
        return {"error": "Item not found"}
    return items[id]