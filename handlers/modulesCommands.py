from aiogram import types
from aiogram.types import *
from loader import dp

from handlers.registrationCommands import current_user

from utils_data.modules_data import *
from random import shuffle
from utils_data.module_body import open_photo, generate_answers_markup
from keyboard.modules_kb import modules_kb, generate_again_kb
from utils_data.grades_data import grades_stickers
from utils import update_changes

current_module = None
current_question = 1
current_points = 0
current_module_name = ''

@dp.callback_query_handler(text='domesticated_animals')
async def start_domestic_animals(call: types.CallbackQuery):
    global current_module, current_question, current_module_name
    current_module = domesticated_animals
    shuffle(current_module)
    await call.message.answer_photo(open_photo(current_module[current_question - 1]['path']), reply_markup=generate_answers_markup(current_module, current_module[current_question - 1]['name']))
    current_question = current_question + 1
    current_module_name = 'domesticated animals'

@dp.callback_query_handler(text='wild_animals')
async def start_wild_animals(call: types.CallbackQuery):
    global current_module, current_question, current_module_name
    current_module = wild_animals
    shuffle(current_module)
    await call.message.answer_photo(open_photo(current_module[current_question - 1]['path']), reply_markup=generate_answers_markup(current_module, current_module[current_question - 1]['name']))
    current_question = current_question + 1
    current_module_name = 'wild animals'

@dp.callback_query_handler(text='pets')
async def start_pets(call: types.CallbackQuery):
    global current_module, current_question, current_module_name
    current_module = pets
    shuffle(current_module)
    await call.message.answer_photo(open_photo(current_module[current_question - 1]['path']), reply_markup=generate_answers_markup(current_module, current_module[current_question - 1]['name']))
    current_question = current_question + 1
    current_module_name = 'pets'

@dp.callback_query_handler(text='jobs')
async def start_jobs(call: types.CallbackQuery):
    global current_module, current_question, current_module_name
    current_module = jobs
    shuffle(current_module)
    await call.message.answer_photo(open_photo(current_module[current_question - 1]['path']), reply_markup=generate_answers_markup(current_module, current_module[current_question - 1]['name']))
    current_question = current_question + 1
    current_module_name = 'jobs'

@dp.callback_query_handler(text='fruits')
async def start_fruits(call: types.CallbackQuery):
    global current_module, current_question, current_module_name
    current_module = fruits
    shuffle(current_module)
    await call.message.answer_photo(open_photo(current_module[current_question - 1]['path']), reply_markup=generate_answers_markup(current_module, current_module[current_question - 1]['name']))
    current_question = current_question + 1
    current_module_name = 'fruits'

@dp.callback_query_handler(text='vegetables')
async def start_vegetables(call: types.CallbackQuery):
    global current_module, current_question, current_module_name
    current_module = vegetables
    shuffle(current_module)
    await call.message.answer_photo(open_photo(current_module[current_question - 1]['path']), reply_markup=generate_answers_markup(current_module, current_module[current_question - 1]['name']))
    current_question = current_question + 1
    current_module_name = 'vegetables'

@dp.callback_query_handler(text_contains='wrong_')
async def reply_wrong_answer(call: types.CallbackQuery):
    global current_module, current_question, current_points, current_module_name
    if current_question == 11:
        await call.message.answer(f'It is the end of the module. Your points are {current_points}')
        await call.message.answer_sticker(grades_stickers[current_points])
        if current_points > 4:
            await call.message.answer('Choose the next module', reply_markup=modules_kb)
        else:
            await call.message.answer('Try again', reply_markup=generate_again_kb(current_module_name))
        update_changes(current_user.get('login'), current_module_name, current_points)
        current_module_name = ''
        current_points = 0
        current_question = 1
        current_module = None
    else:
        await call.message.answer_sticker('CAACAgIAAxkBAAIBAWQ8Lj_VnjsQBO3CtuhH03sgUAeMAAJaAgACVp29ClvFwUJa4dm6LwQ')
        await call.message.answer_photo(open_photo(current_module[current_question - 1]['path']), reply_markup=generate_answers_markup(current_module, current_module[current_question - 1]['name']))
        current_question = current_question + 1

@dp.callback_query_handler(text_contains='correct_')
async def reply_correct_answer(call: types.CallbackQuery):
    global current_module, current_question, current_points, current_module_name
    current_points = current_points + 1
    if current_question == 11:
        await call.message.answer(f'It is the end of the module. Your points are {current_points}')
        await call.message.answer_sticker(grades_stickers[current_points])
        if current_points > 4:
            await call.message.answer('Choose the next module', reply_markup=modules_kb)
        else:
            await call.message.answer('Try again', reply_markup=generate_again_kb(current_module_name))
        update_changes(current_user.get('login'), current_module_name, current_points)
        current_module_name = ''
        current_points = 0
        current_question = 1
        current_module = None
    else:
        await call.message.answer_sticker('CAACAgIAAxkBAAPuZDvwj55ADV4_8jN97YFR-utbR0oAAiwAA_cCyA-8QeDI--FA0y8E')
        await call.message.answer_photo(open_photo(current_module[current_question - 1]['path']), reply_markup=generate_answers_markup(current_module, current_module[current_question - 1]['name']))
        current_question = current_question + 1

        
# CAACAgIAAxkBAAIBAWQ8Lj_VnjsQBO3CtuhH03sgUAeMAAJaAgACVp29ClvFwUJa4dm6LwQ -
# CAACAgIAAxkBAAPuZDvwj55ADV4_8jN97YFR-utbR0oAAiwAA_cCyA-8QeDI--FA0y8E +
    


# await message.answer_photo(open_photo(key))