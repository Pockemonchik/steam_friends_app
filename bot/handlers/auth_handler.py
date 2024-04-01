from re import Match

from aiogram import F
from aiogram import Router
from aiogram import types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils import markdown

import api_client

router = Router()

ID_REGEX = r"\d{17}$"


@router.message(F.text.regexp(ID_REGEX).as_("digits"))
async def id_handler(message: types.Message, digits: Match[str]):
    """Привязка steam id к ползователю"""
    print("found id")
    print(message.from_user.username, message.chat.id, message.text)
    response = await api_client.register(
        username=message.from_user.username,
        chat_id=str(message.chat.id),
        steam_id=message.text,
    )
    await message.answer(text=response, parse_mode="HTML")
    # await message.delete()


@router.message(Command("register"))
@router.callback_query(F.data == "register")
async def register_handler(message: Message) -> None:
    text = markdown.text(
        markdown.markdown_decoration.quote(
            "Бот предназначен для отслеживания\nактивности друзей в Steam\n"
        ),
        markdown.text(
            markdown.bold(
                "Что зарегистрировать\nсвой steam id \n отправлете его мне, пример -> \n"
            ),
            markdown.underline("76561198381522154"),
            sep="\n",
        ),
        sep="\n",
    )

    await message.answer(
        text=text,
        parse_mode=ParseMode.MARKDOWN_V2,
    )
