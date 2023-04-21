from aiogram import types
from aiogram.types import *
from loader import dp

# from handlers.registrationCommands import current_user

from modules_data import *
from random import shuffle
from module_body import open_photo, generate_answers_markup
from keyboard.modules_kb import modules_kb, generate_again_kb
from keyboard.menu_kb import menu_kb
from grades_data import grades_stickers
from utils import update_changes, load_users, save_users

from states.playFrom import PlayFrom
from aiogram.dispatcher import FSMContext

@dp.callback_query_handler(text_contains='domesticated_animals', state=PlayFrom.module_name)
async def start_domestic_animals(call: types.CallbackQuery, state: FSMContext):
    shuffle(domesticated_animals)
    await state.update_data(current_module=domesticated_animals, module_name='domesticated animals', current_question = 1, current_points = 0)
    data = await state.get_data()
    await call.message.answer_photo(open_photo(data['current_module'][data['current_question'] - 1]['path']), reply_markup=generate_answers_markup(data['current_module'], data['current_module'][data['current_question'] - 1]['name']))
    await state.update_data(current_question = data['current_question'] + 1)
    await PlayFrom.next()

@dp.callback_query_handler(text_contains='wild_animals', state=PlayFrom.module_name)
async def start_wild_animals(call: types.CallbackQuery, state: FSMContext):
    shuffle(wild_animals)
    await state.update_data(current_module=wild_animals, module_name='wild animals', current_question = 1, current_points = 0)
    data = await state.get_data()
    await call.message.answer_photo(open_photo(data['current_module'][data['current_question'] - 1]['path']), reply_markup=generate_answers_markup(data['current_module'], data['current_module'][data['current_question'] - 1]['name']))
    await state.update_data(current_question = data['current_question'] + 1)
    await PlayFrom.next()

@dp.callback_query_handler(text_contains='pets', state=PlayFrom.module_name)
async def start_pets(call: types.CallbackQuery, state: FSMContext):
    shuffle(pets)
    await state.update_data(current_module=pets, module_name='pets', current_question = 1, current_points = 0)
    data = await state.get_data()
    await call.message.answer_photo(open_photo(data['current_module'][data['current_question'] - 1]['path']), reply_markup=generate_answers_markup(data['current_module'], data['current_module'][data['current_question'] - 1]['name']))
    await state.update_data(current_question = data['current_question'] + 1)
    await PlayFrom.next()

@dp.callback_query_handler(text_contains='jobs', state=PlayFrom.module_name)
async def start_jobs(call: types.CallbackQuery, state: FSMContext):
    shuffle(jobs)
    await state.update_data(current_module=jobs, module_name='jobs', current_question = 1, current_points = 0)
    data = await state.get_data()
    await call.message.answer_photo(open_photo(data['current_module'][data['current_question'] - 1]['path']), reply_markup=generate_answers_markup(data['current_module'], data['current_module'][data['current_question'] - 1]['name']))
    await state.update_data(current_question = data['current_question'] + 1)
    await PlayFrom.next()

@dp.callback_query_handler(text_contains='fruits', state=PlayFrom.module_name)
async def start_fruits(call: types.CallbackQuery, state: FSMContext):
    shuffle(fruits)
    await state.update_data(current_module=fruits, module_name='fruits', current_question = 1, current_points = 0)
    data = await state.get_data()
    await call.message.answer_photo(open_photo(data['current_module'][data['current_question'] - 1]['path']), reply_markup=generate_answers_markup(data['current_module'], data['current_module'][data['current_question'] - 1]['name']))
    await state.update_data(current_question = data['current_question'] + 1)
    await PlayFrom.next()

@dp.callback_query_handler(text_contains='vegetables', state=PlayFrom.module_name)
async def start_vegetables(call: types.CallbackQuery, state: FSMContext):
    shuffle(vegetables)
    await state.update_data(current_module=vegetables, module_name='vegetables', current_question = 1, current_points = 0)
    data = await state.get_data()
    await call.message.answer_photo(open_photo(data['current_module'][data['current_question'] - 1]['path']), reply_markup=generate_answers_markup(data['current_module'], data['current_module'][data['current_question'] - 1]['name']))
    await state.update_data(current_question = data['current_question'] + 1)
    await PlayFrom.next()

@dp.callback_query_handler(text_contains='wrong_', state=PlayFrom.current_question)
async def reply_wrong_answer(call: types.CallbackQuery, state: FSMContext):
    # global current_module, current_question, current_points, current_module_name
    data = await state.get_data()
    if data['current_question'] == 11:
        await call.message.answer(f'It is the end of the module. Your points are {data["current_points"]}')
        await call.message.answer_sticker(grades_stickers[data["current_points"]])
        if data["current_points"] > 4:
            await state.finish()
            await call.message.answer('Congradulations🎊🎉. Now, you can move forward', reply_markup=menu_kb)
        else:
            await state.finish()
            await call.message.answer('Try again😢', reply_markup=generate_again_kb(data['module_name']))
            await PlayFrom.module_name.set()
    else:
        await call.message.answer_sticker('CAACAgIAAxkBAAIBAWQ8Lj_VnjsQBO3CtuhH03sgUAeMAAJaAgACVp29ClvFwUJa4dm6LwQ')
        await call.message.answer_photo(open_photo(data['current_module'][data['current_question'] - 1]['path']), reply_markup=generate_answers_markup(data['current_module'], data['current_module'][data['current_question'] - 1]['name']))
        await state.update_data(current_question = data['current_question'] + 1)

@dp.callback_query_handler(text_contains='correct_', state=PlayFrom.current_question)
async def reply_correct_answer(call: types.CallbackQuery, state: FSMContext):
    # global current_module, current_question, current_points, current_module_name
    data = await state.get_data()
    # current_points = current_points + 1
    await state.update_data(current_points = data['current_points'] + 1)
    save_users(update_changes("Kate", data['module_name'], data["current_points"] + 1))
    print(data['current_points'])
    if data['current_question'] == 11:
        await call.message.answer(f'It is the end of the module. Your points are {data["current_points"] + 1}')
        await call.message.answer_sticker(grades_stickers[data["current_points"] + 1])
        if data["current_points"] > 4:
            await state.finish()
            await call.message.answer('Congradulations🎊🎉. Now, you can move forward', reply_markup=menu_kb)
        else:
            await state.finish()
            await call.message.answer('Try again😢', reply_markup=generate_again_kb(data['module_name']))
            await PlayFrom.module_name.set()
    else:
        await call.message.answer_sticker('CAACAgIAAxkBAAPuZDvwj55ADV4_8jN97YFR-utbR0oAAiwAA_cCyA-8QeDI--FA0y8E')
        await call.message.answer_photo(open_photo(data['current_module'][data['current_question'] - 1]['path']), reply_markup=generate_answers_markup(data['current_module'], data['current_module'][data['current_question'] - 1]['name']))
        await state.update_data(current_question = data['current_question'] + 1)