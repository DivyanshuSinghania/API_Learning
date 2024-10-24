from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}   # FastAPI now Auto updates 
                                # hence we dont need to write commands 
                                # or any thing for it niether we need to restart the servers

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

@app.get("/")
def get_posts():
    return {"Imposter": "Sus"}  # This does not run as api hit this path in above function, 
                                # hence fastAPI stopped and return that function

@app.post("/createposts")
def create_posts():
    return{"message": "sucessfully created Posts"}