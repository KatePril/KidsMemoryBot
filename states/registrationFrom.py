from aiogram.dispatcher.filters.state import State, StatesGroup

class RegForm(StatesGroup):
    login = State()
    password = State()
    
class RegForm1(StatesGroup):
    login = State()
    password = State()
    
def create_accont(login, password):
    return {'login' : login
            ,'password' : password
            , 'progress' : {'domesticated animals' : 0
                , 'wild animals' : 0
                , 'pets' : 0
                , 'jobs' : 0
                , 'fruits' : 0
                , 'vegetables' : 0}}
    
def get_current_user(users, login):
    for user in users:
        if user['login'] == login:
            return user