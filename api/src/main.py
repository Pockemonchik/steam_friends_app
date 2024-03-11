import uvicorn
import json
from contextlib import asynccontextmanager
from fastapi import FastAPI
from routing.routers import all_routers
from utils.produser import AIOWebProducer


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(title="API для SteamFriendsBot", lifespan=lifespan)


@app.post("/send")
async def send() -> None:
    message_to_produce = json.dumps(
        {"telegram_id": "483123399", "message": "message_to_produce"}
    ).encode(encoding="utf-8")
    producer = AIOWebProducer()
    await producer.send(value=message_to_produce)


for router in all_routers:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
