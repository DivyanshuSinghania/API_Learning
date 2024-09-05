from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}   # FastAPI now Auto updates 
                                # hence we dont need to write commands 
                                # or any thing for it niether we need to restart the servers

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}