import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.files import JSONStorage


from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from decouple import config

API_TOKEN = config('API_TOKEN')

logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
storage = JSONStorage('storage.json')
dp = Dispatcher(bot, storage=storage)