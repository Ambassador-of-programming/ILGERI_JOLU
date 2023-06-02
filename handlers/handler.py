# внешние библиотеки
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

# внутренние файлы
from main import dp
from database.db_manager import DatabaseManager
from game_logic.name_famaly import name_famaly_regist
from game_logic.logic import continue_game
from messages.mess import MESSAGES

# Клавиатура
def start_game():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button_buy = KeyboardButton("🤯НАЧАТЬ ИГРУ")
    return keyboard.add(button_buy)

# Обработчик команды /start
@dp.message_handler(Command('start'))
async def start_cmd(message: Message):
    if message.chat.type == "private":
        user_id = message.from_user.id

        db_manager = DatabaseManager()

        # Проверка на наличие таблицы ilgeri_jolu_clonbot в бд
        check_db = await db_manager.check_table_exists()

        # Если таблицы нету то создает таблицу
        if check_db == False:
            await db_manager.create_db()
            await start_cmd(message)

        # Проверка на наличие пользователя в бд
        check = await db_manager.check_user(user_id)

        if check is not None:
            progres = await db_manager.get_user_progress(user_id)

            if progres is not None:
                await continue_game(progres, message, user_id)

            else:
                await message.answer(MESSAGES['start'], reply_markup=start_game())

                # Регистрация имени и фамилии
                await name_famaly_regist(user_id)

        else:
            # регистрация пользователя в БД
            await db_manager.create_user(user_id)

            # /start приветствие
            await message.answer(MESSAGES['start'], reply_markup=start_game())

            # Регистрация имени и фамилии
            await name_famaly_regist(user_id)

# Обработчик команды /admin
@dp.message_handler(Command('admin'))
async def admin_cmd(message: Message):
    if message.chat.type == "private":
        user_id = message.from_user.id

        # /admin приветствие 
        await message.answer(MESSAGES['admin'])