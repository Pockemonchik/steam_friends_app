from aiogram import Router
from aiogram import types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils import markdown
from aiogram import F 

from message_temlates import *
from keyboards.main_kb import menu
router = Router()


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """

    await message.answer(
        f"Hello, {message.from_user.full_name}", reply_markup=menu
    )



@router.callback_query(F.data == "help")
async def help_handler(callback: CallbackQuery):
    await callback.message.answer(text=HELP_COMMAND, parse_mode="HTML")

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
