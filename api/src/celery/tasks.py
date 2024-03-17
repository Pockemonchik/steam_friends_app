import os
import time
from services.subscribe_service import SubscribeService 
from .worker import worker
from celery.schedules import crontab
from repositories import UsersRepository,SubsRepository
from services.user_service import UserService
from services.subscribe_service import SubscribeService
from db.db_helper import db_helper


@worker.task(name="steam_parse_task")
def steam_parse_task():
    print("steam_parse_task start")
    time.sleep(int(1) * 3)
    subscribe_service = SubscribeService(SubsRepository(db_helper.get_scoped_session()))
    
    return True

@worker.task(name="test")
def test():
    time.sleep(int(1) * 3)
    print("Test task ")
    return True


@worker.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(3.0, steam_parse_task.s(), name="add every 10")

    # Executes every Monday morning at 7:30 a.m.
    # sender.add_periodic_task(
    #     crontab(hour=7, minute=30, day_of_week=1),
    #     test.s('Happy Mondays!'),
    # )
