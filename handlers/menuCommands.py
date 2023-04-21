from aiogram import types
from aiogram.types import *

from loader import dp
from keyboard.modules_kb import modules_kb
from keyboard.main_kb import main_kb
from handlers.registrationCommands import current_user
from progress_sort import give_sorted_progress, get_user

from states.playFrom import PlayFrom
from aiogram.dispatcher import FSMContext

# @dp.message_handler(text='Modules 📚')
# async def get_modules(message: types.Message):
#     # await message.answer('Thanks for your choice', reply_markup=ReplyKeyboardRemove)
#     await message.answer('Choose one of the modules from the categories below', reply_markup=modules_kb)

# @dp.message_handler(text='Modules 📚')
# async def get_modules(message: types.Message, state: FSMContext):
#     # await message.answer('Thanks for your choice', reply_markup=ReplyKeyboardRemove)
#     await PlayFrom.module_name.set()
#     await message.answer('Choose one of the modules from the categories below', reply_markup=modules_kb)
    
    
# @dp.message_handler(text='Progress 📊')
# async def get_process(message: types.Message):
#     # await message.answer('Thanks for your choice', reply_markup=ReplyKeyboardRemove)
#     if (current_user):
#         await message.answer(f'Your progress:\n{give_sorted_progress(current_user.get("progress"))}')
#     else:
#         await message.answer('Log in or sign in', reply_markup=main_kb)

@dp.callback_query_handler(text_contains='modules')
async def get_modules(call: types.CallbackQuery, state: FSMContext):
    # await message.answer('Thanks for your choice', reply_markup=ReplyKeyboardRemove)
    await PlayFrom.module_name.set()
    await call.message.answer('Choose one of the modules from the categories below', reply_markup=modules_kb)
    
    
@dp.callback_query_handler(text_contains='progress')
async def get_process(call: types.CallbackQuery):
    # await message.answer('Thanks for your choice', reply_markup=ReplyKeyboardRemove)
    # if (current_user):
    await call.message.answer(f'Your progress:\n{give_sorted_progress("Kate")}')
    # else:
    #     await call.message.answer('Log in or sign in', reply_markup=main_kb)