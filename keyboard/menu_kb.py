from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu_kb = InlineKeyboardMarkup(row_width=1)
menu_kb.add(InlineKeyboardButton(text='Modules 📚', callback_data='modules'),
            InlineKeyboardButton(text='Progress 📊', callback_data='progress'),
            InlineKeyboardButton(text='Rating 🏆', callback_data='rating'))

# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
# menu_kb.add(KeyboardButton('Modules 📚'), KeyboardButton('Progress 📊'))