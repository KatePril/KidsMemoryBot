from aiogram import types
from aiogram.types import *

from loader import dp
from keyboard.modules_kb import modules_kb
from keyboard.main_kb import main_kb
from utils_data.progress_sort import give_sorted_progress
from utils_data.rating_body import get_users_rating

from states.MenuForm import MenuForm
from states.playFrom import PlayFrom
from aiogram.dispatcher import FSMContext

@dp.callback_query_handler(text = 'modules', state = MenuForm)
async def get_modules(call: types.CallbackQuery, state: FSMContext):
    login = (await state.get_data()).get("login")
    await PlayFrom.module_name.set()
    await state.update_data(login = login)
    await call.message.answer('Choose one of the modules from the categories below', reply_markup=modules_kb)
    
@dp.callback_query_handler(text='progress', state = MenuForm)
async def get_process(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await call.message.answer(f'Your progress:\n{give_sorted_progress(data.get("login"))}')

@dp.callback_query_handler(text='rating', state = MenuForm)
async def get_rating(call: types.CallbackQuery, state: FSMContext):
    login = (await state.get_data()).get("login")
    await call.message.answer(get_users_rating(login))

@dp.callback_query_handler(text='log_out', state = MenuForm)
async def get_log_out(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer('Please log in or sign in', reply_markup=main_kb)