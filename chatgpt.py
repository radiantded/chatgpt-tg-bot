from aiogram.types import Message, chat
from aiogram.utils.executor import start_polling
from openai import Completion

from config import DP, MESSAGE_MAX_LENGTH
from keyboards import kb_client


@DP.message_handler(commands=['start'])
async def command_start(message: Message):
    await message.delete()
    await message.answer( 
        'Добро пожаловать!👋 Отправь свой запрос для ChatGPT💡',
        reply_markup=kb_client
    )


@DP.message_handler()
async def handle_message(message: Message):
    processing_message = await message.answer('⚙️Запрос обрабатывается')
    await chat.Chat.do(message.chat, 'typing')
    response = Completion.create(
        model="text-davinci-003",
        prompt=f'{message.text}|',
        max_tokens=1024,
        stop=['|'],
        frequency_penalty=0.0,
        presence_penalty=0.6,
        temperature=0.1,
    )
    await processing_message.delete()
    text = response['choices'][0]['text']
    for i in range(0, len(text), MESSAGE_MAX_LENGTH):
        reply = text[i:i + MESSAGE_MAX_LENGTH]
        await message.reply(reply)


if __name__ == "__main__":
    start_polling(DP, skip_updates=True)
