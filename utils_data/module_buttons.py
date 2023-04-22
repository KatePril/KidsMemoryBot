from random import shuffle
from keyboard.modules_kb import generate_again_kb
from keyboard.menu_kb import menu_kb
from utils_data.grades_data import grades_stickers

from states.MenuForm import MenuForm
from states.playFrom import PlayFrom

async def update_state_data(state, module, name):
    shuffle(module)
    await state.update_data(current_module=module, module_name=name, current_question = 1, current_points = 0)

async def finish_module(state, call, data):
    await call.answer(f'It is the end of the module. Your points are {data["current_points"] + 1}')
    await call.answer_sticker(grades_stickers[data["current_points"] + 1])
    if data["current_points"] > 4:
        await state.finish()
        await call.answer('Congradulations🎊🎉. Now, you can move forward', reply_markup=menu_kb)
        await MenuForm.main_menu.set()
        await state.update_data(login=data['login'])
    else:
        await state.finish()
        await call.answer('Try again😢', reply_markup=generate_again_kb(data['module_name']))
        await PlayFrom.module_name.set()