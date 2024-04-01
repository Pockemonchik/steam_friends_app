from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

menu = [
    [InlineKeyboardButton(text=" Регистрация", callback_data="register"),
     InlineKeyboardButton(text="🤼‍♂️ Друзья в сети", callback_data="friends")],
    [InlineKeyboardButton(text="📩 Подписки", callback_data="subs_menu"),
     InlineKeyboardButton(text="💰 Баланс", callback_data="help")],
    [InlineKeyboardButton(text="📝 Описание", callback_data="help"),
     InlineKeyboardButton(text="🔎 Помощь", callback_data="help"),
     ]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])
