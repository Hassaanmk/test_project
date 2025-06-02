from typing import Union
import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

list_username= []

class Blog(BaseModel):
    user_id : int
    query : str

@app.get("/")
def read_username():
    print({"Hello": "user"})


@app.post("/users/{user_id}")
def read_item(bl:Blog):
    return {"user_id": bl.user_id, "q": bl.query}

if __name__ == "__main__":
    uvicorn.run("main:app", host= "127.0.0.1", port= 8000, reload= True)