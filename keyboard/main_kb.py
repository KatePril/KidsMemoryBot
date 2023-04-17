from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

main_kb = InlineKeyboardMarkup(row_width=1)
main_kb.add(InlineKeyboardButton(text='Log in 🗳️', callback_data='log_in'),
            InlineKeyboardButton(text='Sign in 🗃️', callback_data='sign_in'))

log_in_kb = InlineKeyboardMarkup(row_width=1)
log_in_kb.add(InlineKeyboardButton(text='Sign in 🗃️', callback_data='sign_in'))

sign_in_kb = ReplyKeyboardMarkup(resize_keyboard=True)
sign_in_kb.add(KeyboardButton('Submit registration ✅'), KeyboardButton('Cancel registration ❌'))