import logging
import sys
import asyncio
from aiogram import Bot, Dispatcher,  types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from config import settings


dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, {(message.from_user.full_name)}!")


@dp.message(Command("help"))
async def help_handler(message: Message) -> None:
    text = markdown.text(
        markdown.markdown_decoration.quote("Бот предназначен для отслеживания\nактивности друзей в Steam\n"),
        markdown.text(
            markdown.bold("Список команд\n"),
            markdown.underline("Добавить друга для отслеживания"),
            sep="\n",
        ),
        sep="\n",
    )

    await message.answer(text=text,
                        #  parse_mode=None,
                         parse_mode=ParseMode.MARKDOWN_V2,
                         )


async def main() -> None:
    bot = Bot(
        token="6858161506:AAHGav0STjNJFDl6vqXe8oY9IZowHSwtIL8",
        # token=settings.bot_token,
        parse_mode=ParseMode.MARKDOWN_V2,
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
