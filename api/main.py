from fastapi import FastAPI,Body
import uvicorn
from pydantic import BaseModel

class CreateUser(BaseModel):
    email: str

app = FastAPI()

@app.get("/")
def hello_index():
    return {
        "message": "hellow"
    }


@app.get("/items/")
def list_items():
    return [
        "t1",
        "t2",
        "t2",
    ]

@app.get("/hello/")
def get_hello(name:str):
    return {"message": f"Hello {name}"}

@app.post("/user/")
def create_user(email: CreateUser):
    return {"message": f"Hello {email}"}

@app.get("/items/{item_id}")
def get_item_by_id(item_id:int):
    return {item_id}

if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)