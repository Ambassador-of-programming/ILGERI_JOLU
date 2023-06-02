# Внешние библиотеки
from aiogram import types
from aiogram.dispatcher.filters import Text

# Внутренние файлы
from main import dp
from database.db_manager import DatabaseManager
from game_logic.logic import step1_logic

async def name_famaly_regist(tg_id):
    # Переменные для отслеживания состояний
    name_completed = False
    surname_completed = False
    name = None
    surname = None

    @dp.message_handler(Text('🤯НАЧАТЬ ИГРУ'))
    async def start_game_cmd(message: types.Message):
        global name_completed, surname_completed, name, surname

        if message.chat.type == "private":
            await message.answer('Введите ваше имя')
            name_completed = False
            surname_completed = False
            name = None
            surname = None

    @dp.message_handler(content_types=types.ContentType.TEXT)
    async def handle_text_answer(message: types.Message):
        global name_completed, surname_completed, name, surname

        if not name_completed:
            name = message.text
            name_completed = True
            await message.answer('Введите вашу фамилию')
        elif not surname_completed:
            surname = message.text
            surname_completed = True

            # Управление базой данных 
            db_manager = DatabaseManager()

            # Добавление имени и фамилии в базу данных
            await db_manager.add_name_family_user(tg_id, name, surname)

            # Выводим сохраненное имя и фамилию
            await message.answer(f"Имя: {name}, Фамилия: {surname}")

            await db_manager.update_current_step(tg_id, 1)
            await step1_logic(message, tg_id)


