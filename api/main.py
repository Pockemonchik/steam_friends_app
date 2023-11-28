from fastapi import FastAPI
import uvicorn
from users.views import router as user_router



app = FastAPI()
app.include_router(user_router)

@app.get("/")
def hello_index():
    return {
        "message": "hellow"
    }


@app.get("/hello/")
def get_hello(name:str):
    return {"message": f"Hello {name}"}



if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)