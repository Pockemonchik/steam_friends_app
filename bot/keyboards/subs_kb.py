from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

subs_menu = [
    [InlineKeyboardButton(text="Мои подписки", callback_data="register")],
     [InlineKeyboardButton(text="Добавить подписку", callback_data="create_sub"),
    InlineKeyboardButton(text="Удалить подписку", callback_data="help")]

]
subs_menu = InlineKeyboardMarkup(inline_keyboard=subs_menu)
