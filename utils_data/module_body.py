from random import shuffle
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def open_photo(path):
    return open(path, 'rb')

def generate_wrong_answers(module, correct_answer):
    wrong_answers = []
    for item in module:
        if item['name'] != correct_answer:
            wrong_answers.append(item['name'])
    shuffle(wrong_answers)
    return wrong_answers

def generate_answers_markup(module, correct_answer):
    wrond_answers = generate_wrong_answers(module, correct_answer)
    answers_kb = InlineKeyboardMarkup(row_width=1)
    answers_list = [InlineKeyboardButton(wrond_answers[0], callback_data='wrong_answer')
                    , InlineKeyboardButton(wrond_answers[3], callback_data='wrong_answer')
                    , InlineKeyboardButton(wrond_answers[6], callback_data='wrong_answer')
                    , InlineKeyboardButton(correct_answer, callback_data='correct_answer')]
    shuffle(answers_list)
    for answer in answers_list:
        answers_kb.add(answer)
    return answers_kb