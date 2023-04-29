from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu_kb = InlineKeyboardMarkup(row_width=1)
menu_kb.add(InlineKeyboardButton(text='Modules 📚', callback_data='modules'),
            InlineKeyboardButton(text='Progress 📊', callback_data='progress'),
            InlineKeyboardButton(text='Rating 🏆', callback_data='rating'),
            InlineKeyboardButton(text='Log out ➡️', callback_data='log_out'))