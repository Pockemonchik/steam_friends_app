from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from keyboards.subs_kb import subs_menu
class Sub(StatesGroup):
    choosing_gamer_nickname = State()
    choosing_game_name = State()
    choosing_period = State()


router = Router()

@router.callback_query(F.data == "subs_menu")
async def subs_menu_handler(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        f"📩 Работа с подписками", reply_markup=subs_menu
    )

@router.callback_query(F.data == "create_sub")
async def input_gamer_nickname(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Sub.choosing_gamer_nickname)
    await callback.message.answer("Выберете ник игрока")



@router.message(Sub.choosing_gamer_nickname)
async def input_game_name(message: Message, state: FSMContext):
    await state.update_data(gamer_nickname=message.text.lower())
    print("state.get_data()")
    print(await state.get_data())
    await state.set_state(Sub.choosing_game_name)
    await message.answer("Выберете игру")

@router.message(Sub.choosing_game_name)
async def input_game_name(message: Message, state: FSMContext):

    await state.update_data(game_name=message.text.lower())
    print("state.get_data()")
    print(await state.get_data())
    await state.set_state(Sub.choosing_period)
    await message.answer("Выберете период")


@router.message(Sub.choosing_period)
async def input_game_name(message: Message, state: FSMContext):
    await state.update_data(period=message.text.lower())
    print("state.get_data()")
    print(await state.get_data())
    await message.answer("Подписка создается ...")