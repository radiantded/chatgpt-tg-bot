from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


b1 = KeyboardButton('Что такое ChatGPT?')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True).row(b1)
