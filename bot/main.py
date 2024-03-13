import logging
import sys
import asyncio
import os
import json
from re import Match
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from config import settings
from aiogram import F
import steam_service
from aiokafka import AIOKafkaConsumer
from message_temlates import *
import api_client

dp = Dispatcher()
bot = Bot(
    token=os.environ.get("BOT_TOKEN", "6858161506:AAHGav0STjNJFDl6vqXe8oY9IZowHSwtIL8"),
    # token=settings.bot_token,
    parse_mode=ParseMode.MARKDOWN_V2,
)

kafka_server: str = os.environ.get("KAFKA_SERVER", "broker:29092")
kafka_topic: str = os.environ.get("KAFKA_TOPIC", "notify_friends")
kafka_client_id: str = os.environ.get("KAFKA_CLEIENT_ID", "python-producer")


async def consume() -> None:
    consumer = AIOKafkaConsumer(
        kafka_topic,
        bootstrap_servers=kafka_server,
    )
    try:
        await consumer.start()
        try:
            async for msg in consumer:
                serialized = json.loads(msg.value)
                await bot.send_message(
                    chat_id=serialized.get("telegram_id"),
                    text=serialized.get("message"),
                )
        except Exception as e:
            print(e)
            await consumer.stop()
        finally:
            await consumer.stop()
    except Exception as e:
        await consumer.stop()
        print(e)


ID_REGEX = r"\d{17}$"


@dp.message(CommandStart())
async def start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    kb = [
        [types.KeyboardButton(text="/help")],
        [types.KeyboardButton(text="/description")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb, resize_keyboard=True, input_field_placeholder="Что будем делать?"
    )
    await message.answer(
        f"Hello, {(message.from_user.full_name)}", reply_markup=keyboard
    )


@dp.message(Command("help"))
async def help_handler(message: types.Message):
    print("message.chat.id", message.chat.id)
    await message.answer(text=HELP_COMMAND, parse_mode="HTML")
    # await message.delete()


@dp.message(Command("description"))
async def description_handler(message: Message) -> None:
    text = markdown.text(
        markdown.markdown_decoration.quote(
            "Бот предназначен для отслеживания\nактивности друзей в Steam\n"
        ),
        markdown.text(
            markdown.bold("Для начала необходимо зарегистрировать\nсвой steam id \n"),
            markdown.underline("Зарегистрировать"),
            sep="\n",
        ),
        sep="\n",
    )

    await message.answer(
        text=text,
        #  parse_mode=None,
        parse_mode=ParseMode.MARKDOWN_V2,
    )


@dp.message(Command("friends"))
async def friends_handler(message: types.Message):
    steam_data = steam_service.get_steam_user_friends_info("76561198381522154")
    import json

    gaming_friends = list(filter(lambda x: "gameextrainfo" in x, steam_data["friends"]))
    # print(type(steam_data["fiends"]))
    print(json.dumps(gaming_friends))
    friend_list = []
    for friend in gaming_friends:
        friend_list.append(
            "<b>{}</b> - <em>{}</em>".format(
                friend["personaname"], friend["gameextrainfo"]
            )
        )
    print("friend_list", friend_list)
    await message.answer(text="\n".join(friend_list), parse_mode="HTML")
    # await message.delete()


@dp.message(F.text.regexp(ID_REGEX).as_("digits"))
async def id_handler(message: types.Message, digits: Match[str]):
    """Привязка steam id к ползователю"""
    print("found id")
    print(message.from_user.username, message.chat.id, message.text)
    response = await api_client.register(
        message.from_user.username,
        str(message.chat.id),
        message.text,
    )
    await message.answer(text=response, parse_mode="HTML")
    # await message.delete()


@dp.message()
async def not_hadle__handler(message: types.Message):
    """если не отловлено"""
    await message.answer(text=message.text, parse_mode="HTML")
    # await message.delete()


async def main() -> None:
    polling = asyncio.create_task(dp.start_polling(bot, skip_updates=True))
    consuming = asyncio.create_task(consume())
    await asyncio.gather(polling, consuming)
    print("Bot has successfully started polling")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
