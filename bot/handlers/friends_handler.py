from aiogram import Router
from aiogram import types
from aiogram.filters import Command

from utils import api_client

router = Router()


@router.message(Command("friends"))
async def friends_handler(message: types.Message):
    print("fetch friends id")
    print(message.from_user.username, message.chat.id, message.text)
    response = await api_client.fetch_friends(
        message.from_user.username,
        str(message.chat.id),
    )
    await message.answer(text=response, parse_mode="HTML")
