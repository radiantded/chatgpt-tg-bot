import openai
import os

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.environ.get('OPENAI_API_KEY')


MESSAGE_MAX_LENGTH = 2048
BOT = Bot(token=os.environ.get('TG_TOKEN'))
DP = Dispatcher(BOT)
