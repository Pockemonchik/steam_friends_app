import json
import time
import asyncio
from utils.produser import AIOWebProducer
from services.subscribe_service import SubscribeService 
from .worker import worker
from celery.schedules import crontab
from repositories import UsersRepository,SubsRepository
from services.user_service import UserService
from services.subscribe_service import SubscribeService
from db.db_helper import db_helper
from core.config import settings

async def steam_parse_message():
    """Отправка в кафу запрос на парсинг данных по подписке"""
    print("steam_parse_task start")
    subscribe_service = SubscribeService(SubsRepository(db_helper.get_scoped_session()))
    subs = await subscribe_service.get_subs_with_users()
    print("start loop")
    for sub in subs:       
        message_to_produce = json.dumps(
            {
                "telegram_id": sub.user.chat_id,
                "message": "message_to_produce",
                "steam_id": sub.user.steam_id,
                "game": sub.game,
                "gamer_name": sub.gamer_name,
            }
        ).encode(encoding="utf-8")
        producer = AIOWebProducer(topic=settings.kafka_steam_topic)
        await producer.send(value=message_to_produce)
    return True

@worker.task(name="steam_parse_task")
def steam_parse_task():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(steam_parse_message())
    # return True

@worker.task(name="test")
def test():
    time.sleep(int(1) * 3)
    print("Test task ")
    return True


# @worker.on_after_finalize.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(3.0, steam_parse_task.s(), name="add every 10")

    # Executes every Monday morning at 7:30 a.m.
    # sender.add_periodic_task(
    #     crontab(hour=7, minute=30, day_of_week=1),
    #     test.s('Happy Mondays!'),
    # )
