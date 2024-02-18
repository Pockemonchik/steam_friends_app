from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from users.views import router as user_router
from models import Base, db_helper

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(lifespan=lifespan)
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