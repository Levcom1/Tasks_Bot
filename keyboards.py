from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('Hello')
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b1)
b2 = KeyboardButton('Добавить задание', callback_data='butt_id')
b3 = KeyboardButton('Удалить задание')
markup1 = ReplyKeyboardMarkup(resize_keyboard=True).row(b2, b3)
