import logging
import sys
import asyncio
from re import Match
from aiogram import Bot, Dispatcher,  types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from config import settings
from aiogram import F
import steam_service



dp = Dispatcher()


HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>старт бота</em>
<b>/description</b> - <em>описание бота</em>
<b>/friends</b> - <em>друзья в  сети</em>"""

FRIEND_LIST = """
<b>Друг 1</b> - <em>в сети</em>
<b>Друг 2</b> - <em>Дота 2</em>
"""
ID_REGEX = r'\d{17}$'

@dp.message(CommandStart())
async def start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    kb = [
        [types.KeyboardButton(text="/help")],
        [types.KeyboardButton(text="/description")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True,
                                         input_field_placeholder="Что будем делать?")
    await message.answer(f"Hello, {(message.from_user.full_name)}", reply_markup=keyboard)


@dp.message(Command('help'))
async def help_handler(message: types.Message):
    await message.answer(text=HELP_COMMAND,
                         parse_mode="HTML")
    # await message.delete()


@dp.message(Command('friends'))
async def friends_handler(message: types.Message):
    steam_data = steam_service.get_steam_user_friends_info("76561198381522154")
    import json
    gaming_friends = (list(filter(lambda x: "gameextrainfo" in x,steam_data["friends"])))
    # print(type(steam_data["fiends"]))
    print(json.dumps(gaming_friends))
    friend_list = []
    for friend in gaming_friends:
        friend_list.append("<b>{}</b> - <em>{}</em>".format(friend['personaname'],friend['gameextrainfo']))
    print("friend_list",friend_list)
    await message.answer(text="\n".join(friend_list),
                         parse_mode="HTML")
    # await message.delete()




@dp.message(Command("description"))
async def description_handler(message: Message) -> None:
    text = markdown.text(
        markdown.markdown_decoration.quote(
            "Бот предназначен для отслеживания\nактивности друзей в Steam\n"),
        markdown.text(
            markdown.bold(
                "Для начала необходимо зарегистрировать\nсвой steam id \n"),
            markdown.underline("Зарегистрировать"),
            sep="\n",
        ),
        sep="\n",
    )

    await message.answer(text=text,
                         #  parse_mode=None,
                         parse_mode=ParseMode.MARKDOWN_V2,
                         )


@dp.message(F.text.regexp(ID_REGEX).as_("digits"))
async def id_handler(message: types.Message, digits: Match[str]):
    """Привязка steam id к ползователю"""
    print("found id")
    await message.answer(text=message.text,
                         parse_mode="HTML")
    # await message.delete()

@dp.message()
async def not_hadle__handler(message: types.Message):
    """если не отловлено"""
    await message.answer(text=message.text,
                         parse_mode="HTML")
    # await message.delete()

async def main() -> None:
    bot = Bot(
        token="6858161506:AAHGav0STjNJFDl6vqXe8oY9IZowHSwtIL8",
        # token=settings.bot_token,
        parse_mode=ParseMode.MARKDOWN_V2,
    )
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
