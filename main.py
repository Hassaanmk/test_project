from typing import Union
import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

list_username= []

class Blog(BaseModel):
    user_id : int
    query : str

@app.get("/start")
def read_username():
    print({"Hello": "user"})

@app.put("/username/{username}")
def put_username(username: str):
    if username:
        list_username.append(username)
    return list_username

@app.post("/users/{user_id}")
def read_item(bl:Blog):
    return {"user_id": bl.user_id, "q": bl.query, "active_users": list_username}

if __name__ == "__main__":
    uvicorn.run("main:app", host= "127.0.0.1", port= 8000, reload= True)