# внешние библиотеки
from aiogram import Dispatcher, Bot, executor

# внутренние библиотеки
import asyncio

# внутренние файлы
from config.tg_config import TOKEN, cipher_token


loop = asyncio.new_event_loop()
bot = Bot(cipher_token.decrypt(TOKEN).decode(), parse_mode='HTML')
dp = Dispatcher(bot, loop=loop)

if __name__ == '__main__':
    from handlers.handler import dp
    executor.start_polling(dp, loop=loop)