import uvicorn
import json
from contextlib import asynccontextmanager
from fastapi import FastAPI
from core.config import settings
from routing.routers import all_routers
from utils.produser import AIOWebProducer
from aiokafka import AIOKafkaProducer

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(title="API для SteamFriendsBot", lifespan=lifespan)


@app.post("/send_notify")
async def send_notify() -> None:
    message_to_produce = json.dumps(
        {"telegram_id": "483123399", "message": "message_to_produce"}
    ).encode(encoding="utf-8")
    producer = AIOWebProducer(topic=settings.kafka_notify_topic)
    await producer.send(value=message_to_produce)


@app.post("/send_steam_task")
async def send_steam_task() -> None:
    message_to_produce = json.dumps(
        {
            "telegram_id": "483123399",
            "message": "message_to_produce",
            "steam_id": "76561198381522154",
        }
    ).encode(encoding="utf-8")
    producer = AIOWebProducer(topic=settings.kafka_steam_topic)
    await producer.send(value=message_to_produce)


for router in all_routers:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
