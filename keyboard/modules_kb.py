from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

modules_kb = InlineKeyboardMarkup(row_width=1)
modules_kb.add(InlineKeyboardButton(text='Domesticated animals 🐷', callback_data='domesticated_animals')
            , InlineKeyboardButton(text='Wild animals 🐯', callback_data='wild_animals')
            , InlineKeyboardButton(text='Pets 🐶', callback_data='pets')
            , InlineKeyboardButton(text='Jobs 👩‍⚕️', callback_data='jobs')
            , InlineKeyboardButton(text='Fruits 🍊', callback_data='fruits')
            , InlineKeyboardButton(text='Vegetables 🍆', callback_data='vegetables'))

def generate_again_kb(name):
    answer_kb = InlineKeyboardMarkup(row_width=1)
    if name == 'domesticated animals':
        answer_kb.add(InlineKeyboardButton(text='Domesticated animals 🐷', callback_data='domesticated_animals'))
    elif name == 'wild animals':
        answer_kb.add(InlineKeyboardButton(text='Wild animals 🐯', callback_data='wild_animals'))
    elif name == 'pets':
        answer_kb.add(InlineKeyboardButton(text='Pets 🐶', callback_data='pets'))
    elif name == 'jobs':
        answer_kb.add(InlineKeyboardButton(text='Jobs 👩‍⚕️', callback_data='jobs'))
    elif name == 'fruits':
        answer_kb.add(InlineKeyboardButton(text='Fruits 🍊', callback_data='fruits'))
    elif name == 'vegetables':
        answer_kb.add(InlineKeyboardButton(text='Vegetables 🍆', callback_data='vegetables'))
    return answer_kb