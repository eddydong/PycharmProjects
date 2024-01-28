from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# param in-taking example: IP:8000/items/123?q=456&t=789
@app.get("/items/{item_id}")
def read_item(item_id: int, q: int, t: int):
    return {"item_id": item_id, "res": q * t}

# to start the server:
# go to current project folder
# run uvicorn fastapi_test_1:app --reload in system or pycharm terminal
