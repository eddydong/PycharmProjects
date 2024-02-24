from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

#param intaking emample: IP:8000/items/123?q=456&t=789
@app.get("/items/{item_id}")
def read_item(item_id: int, q: int, t: int):
    return {"id": item_id, "res": q*t}