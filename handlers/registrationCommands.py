from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from utils import load_users, save_users
from utils_data.password_code import make_md5_password

from states.registrationFrom import RegForm, RegForm1, create_accont
from states.MenuForm import MenuForm
from keyboard.main_kb import main_kb, log_in_kb
from keyboard.menu_kb import menu_kb
from utils_data.angry_stickers import get_angry_sticker


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
        await message.answer("Hello, welcome to KidsMemoryBot. Look through the opening menu and choose one of the options", reply_markup = main_kb)
        
@dp.callback_query_handler(text='log_in') 
async def start_log_in(message: types.Message, state: FSMContext):
        await RegForm1.login.set()
        await message.answer("Enter your login")

@dp.message_handler(state=RegForm1.login)
async def process_password1(message: types.Message, state: FSMContext):
        if not message.text in [user['login'] for user in load_users()]:
                await message.answer("Try again or create a new account", reply_markup=log_in_kb)
        else:
                await state.update_data(login=message.text)
                await RegForm1.next()
                await message.answer("Enter your password") 

@dp.message_handler(state=RegForm1.password)
async def process_finish1(message: types.Message, state: FSMContext):
        data = await state.get_data()
        correct_password = ''
        for user in load_users():
                if user['login'] == data['login']:
                        correct_password = user['password'] #md5 hash
                        break
        if make_md5_password(message.text) == correct_password:
                # await state.update_data(password=message.text)
                await state.finish()
                await message.answer(f'Welcome back {data["login"]}', reply_markup=menu_kb)
                await MenuForm.main_menu.set()
                await state.update_data(login=data['login'])
        else:
                await message.answer("Try again")  
                return

@dp.callback_query_handler(text='sign_in') 
async def start_sign_in(message: types.Message):
        await RegForm.login.set()
        await message.answer("Choose your login")

@dp.message_handler(state=RegForm.login)
async def process_login(message: types.Message, state: FSMContext):
        if not message.text in [user['login'] for user in load_users()]:
                await state.update_data(login=message.text)
                await RegForm.next()
                await message.answer("Create a password")
        else:
                await message.answer('This login is already taken')
                return

@dp.message_handler(state=RegForm.password)
async def process_finish(message: types.Message, state: FSMContext):
        await state.update_data(password=make_md5_password(message.text))
        data = await state.get_data()
        users = load_users()
        users.append(create_accont(data['login'], data['password']))
        save_users(users)
        await state.finish()
        await message.answer(f'Welcome {data["login"]}', reply_markup=menu_kb)
        await MenuForm.main_menu.set()
        await state.update_data(login=data['login'])

@dp.message_handler(content_types=types.ContentType.STICKER)
async def echo(message: types.Message):
    await message.answer_sticker(get_angry_sticker())
    print(message.sticker.file_id)

@dp.message_handler()
async def echo(message: types.Message):
        await message.answer_sticker(get_angry_sticker())