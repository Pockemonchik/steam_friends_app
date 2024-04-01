from aiogram import Router
from aiogram import types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils import markdown

from message_temlates import *

router = Router()


@router.message(CommandStart())
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


@router.message(Command("help"))
async def help_handler(message: types.Message):
    print("message.chat.id", message.chat.id)
    await message.answer(text=HELP_COMMAND, parse_mode="HTML")
    await message.delete()


@router.message(Command("description"))
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
        parse_mode=ParseMode.MARKDOWN_V2,
    )


@router.message()
async def not_handle__handler(message: types.Message):
    """если не отловлено"""
    await message.answer(text=message.text, parse_mode="HTML")
