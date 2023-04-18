from aiogram.dispatcher.filters.state import State, StatesGroup

class PlayFrom(StatesGroup):
    # login = State()
    current_module = State()
    module_name = State()
    current_question = 1
    current_points = 0