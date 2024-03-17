import uvicorn
import json
from db.db_helper import db_helper
from contextlib import asynccontextmanager
from fastapi import FastAPI
from core.config import settings
from routing.routers import all_routers
from utils.produser import AIOWebProducer
from sqladmin import Admin
from db.admin import UserAdmin, SubsAdmin


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(title="API для SteamFriendsBot", lifespan=lifespan)


admin = Admin(app, db_helper.engine)
admin.add_view(UserAdmin)
admin.add_view(SubsAdmin)


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

@app.post("/run_steam_task")
async def run_steam_task_celery() -> None:
    from .celery.tasks import steam_parse_task
    steam_parse_task.delay()
    return 0

for router in all_routers:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
