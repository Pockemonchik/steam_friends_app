import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from consumers import notify_consumer
from handlers import friends_handler, subs_handler, base_handlers, auth_handler

dp = Dispatcher()
bot = Bot(
    token=os.environ.get("BOT_TOKEN", "6858161506:AAHGav0STjNJFDl6vqXe8oY9IZowHSwtIL8"),
    parse_mode=ParseMode.HTML,
)
dp.include_routers(friends_handler.router,
                   subs_handler.router,
                   base_handlers.router,
                   auth_handler.router, )

kafka_server: str = os.environ.get("KAFKA_SERVER", "broker:29092")
kafka_topic: str = os.environ.get("KAFKA_TOPIC", "notify_friends")
kafka_client_id: str = os.environ.get("KAFKA_CLEIENT_ID", "python-producer")


async def main() -> None:
    polling = asyncio.create_task(dp.start_polling(bot, skip_updates=True))
    consuming = asyncio.create_task(
        notify_consumer.consume(kafka_topic=kafka_topic, kafka_server=kafka_server, bot=bot))
    await asyncio.gather(polling, consuming)
    print("Bot has successfully started polling")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
