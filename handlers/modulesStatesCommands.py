from aiogram import types
from aiogram.types import *
from loader import dp

from utils_data.modules_data import *
from utils_data.module_body import open_photo, generate_answers_markup
from utils import update_changes, save_users
from utils_data.module_buttons import update_state_data, finish_module

from states.playFrom import PlayFrom
from aiogram.dispatcher import FSMContext

@dp.callback_query_handler(text=['domesticated_animals', 'wild_animals', 'pets', 'jobs', 'fruits', 'vegetables'], state=PlayFrom.module_name)
async def start_module(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'domesticated_animals':
        await update_state_data(state, domesticated_animals, 'domesticated animals')
    elif call.data  == 'wild_animals':
        await update_state_data(state, wild_animals, 'wild animals')
    elif call.data  == 'pets':
        await update_state_data(state, pets, 'pets')    
    elif call.data  == 'jobs':
        await update_state_data(state, jobs, 'jobs')    
    elif call.data  == 'fruits':
        await update_state_data(state, fruits, 'fruits')    
    elif call.data  == 'vegetables':
       await update_state_data(state, vegetables, 'vegetables')    
    data = await state.get_data()
    await call.message.answer_photo(open_photo(data['current_module'][data['current_question'] - 1]['path']), reply_markup=generate_answers_markup(data['current_module'], data['current_module'][data['current_question'] - 1]['name']))
    await state.update_data(current_question = data['current_question'] + 1)
    await PlayFrom.next()

@dp.callback_query_handler(text_contains='wrong_', state=PlayFrom.current_question)
async def reply_wrong_answer(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if data['current_question'] == 11:
        await finish_module(state, call.message, data)
    else:
        await call.message.answer_sticker('CAACAgIAAxkBAAIBAWQ8Lj_VnjsQBO3CtuhH03sgUAeMAAJaAgACVp29ClvFwUJa4dm6LwQ')
        await call.message.answer_photo(open_photo(data['current_module'][data['current_question'] - 1]['path']), reply_markup=generate_answers_markup(data['current_module'], data['current_module'][data['current_question'] - 1]['name']))
        await state.update_data(current_question = data['current_question'] + 1)

@dp.callback_query_handler(text_contains='correct_', state=PlayFrom.current_question)
async def reply_correct_answer(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await state.update_data(current_points = data['current_points'] + 1)
    save_users(update_changes(data.get('login'), data['module_name'], data["current_points"] + 1))
    if data['current_question'] == 11:
        await finish_module(state, call.message, data)
    else:
        await call.message.answer_sticker('CAACAgIAAxkBAAPuZDvwj55ADV4_8jN97YFR-utbR0oAAiwAA_cCyA-8QeDI--FA0y8E')
        await call.message.answer_photo(open_photo(data['current_module'][data['current_question'] - 1]['path']), reply_markup=generate_answers_markup(data['current_module'], data['current_module'][data['current_question'] - 1]['name']))
        await state.update_data(current_question = data['current_question'] + 1)

