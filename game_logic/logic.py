# внешние библиотеки
from aiogram import types

# внутренние файлы
from main import dp
from database.db_manager import DatabaseManager


# подключение к базе данных с вызовами функций
db_manager = DatabaseManager()

async def continue_game(progress, message, user_id):
    if progress == 1:
        await step1_logic(message, user_id)
    elif progress == 2:
        await step2_logic(message, user_id)
    elif progress == 3:
        await step3_logic(message, user_id)
    elif progress == 4:
        await step4_logic(message, user_id)
    elif progress == 5:
        await step5_logic(message, user_id)
    elif progress == 6:
        await step6_logic(message, user_id)
    elif progress == 7:
        await step7_logic(message, user_id)
    elif progress == 8:
        await step8_logic(message, user_id)
    elif progress == 9:
        await step9_logic(message, user_id)
    # и так далее, продолжайте добавлять логику для каждого шага игры

async def step1_logic(message: types.Message, user_id):
    try:
        # Логика для первого шага игры
        # Вывод вопроса и изображения
        question = "Вопрос №1: Какое озеро считается самым большим в Кыргызстане?"
        answer_question = "ИссыкКуль"
        image_filename = "image/answer_1.jpg"  # Имя файла изображения

        # Отправка сообщения с изображением и вопросом пользователю
        await message.answer_photo(photo=open(image_filename, 'rb'), caption=question)

        # Получение ответа пользователя
        answer = None

        @dp.message_handler(content_types=types.ContentType.TEXT)
        async def handle_text_answer(message: types.Message):
            nonlocal answer
            answer = message.text

            # Сохранение ответа пользователя в базе данных
            await db_manager.save_answer(user_id, 1, answer)

            # Удаление обработчика после получения ответа пользователя
            dp.message_handlers.unregister(handle_text_answer)

            # Обновление текущего шага пользователя в базе данных
            await db_manager.update_current_step(user_id, 2)

            # Выводим пользователю информацию о успешном приему ответа
            await message.answer('Ваш ответ зачислен! Приступайте к следующему')

            # Вызов логики для следующего шага игры
            await step2_logic(message, user_id)

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")


async def step2_logic(message: types.Message, user_id):
    try:
        # Логика для первого шага игры
        # Вывод вопроса и изображения
        question = "Вопрос №2: Как называется национальный парк, который включен в список Всемирного наследия ЮНЕСКО?"
        answer_question = "Суусамырский"
        image_filename = "image/answer_2.jpg"  # Имя файла изображения

        # Отправка сообщения с изображением и вопросом пользователю
        await message.answer_photo(photo=open(image_filename, 'rb'), caption=question)

        # Получение ответа пользователя
        answer = None

        @dp.message_handler(content_types=types.ContentType.TEXT)
        async def handle_text_answer(message: types.Message):
            nonlocal answer
            answer = message.text

            # Сохранение ответа пользователя в базе данных
            await db_manager.save_answer(user_id, 2, answer)

            # Удаление обработчика после получения ответа пользователя
            dp.message_handlers.unregister(handle_text_answer)

            # Обновление текущего шага пользователя в базе данных
            await db_manager.update_current_step(user_id, 3)

            # Выводим пользователю информацию о успешном приему ответа
            await message.answer('Ваш ответ зачислен! Приступайте к следующему')

            # Вызов логики для следующего шага игры
            await step3_logic(message, user_id)

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

async def step3_logic(message: types.Message, user_id):
    try:
        # Логика для первого шага игры
        # Вывод вопроса и изображения
        question = "Вопрос №2: Кто является основателем первой киргизской империи?"
        answer_question = "Манас"
        image_filename = "image/answer_3.jpg"  # Имя файла изображения

        # Отправка сообщения с изображением и вопросом пользователю
        await message.answer_photo(photo=open(image_filename, 'rb'), caption=question)

        # Получение ответа пользователя
        answer = None

        @dp.message_handler(content_types=types.ContentType.TEXT)
        async def handle_text_answer(message: types.Message):
            nonlocal answer
            answer = message.text

            # Сохранение ответа пользователя в базе данных
            await db_manager.save_answer(user_id, 3, answer)

            # Удаление обработчика после получения ответа пользователя
            dp.message_handlers.unregister(handle_text_answer)

            # Обновление текущего шага пользователя в базе данных
            await db_manager.update_current_step(user_id, 4)

            # Выводим пользователю информацию о успешном приему ответа
            await message.answer('Ваш ответ зачислен! Приступайте к следующему')

            # Вызов логики для следующего шага игры
            await step4_logic(message, user_id)

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

async def step4_logic(message: types.Message, user_id):
    pass

async def step5_logic(message: types.Message, user_id):
    pass

async def step6_logic(message: types.Message, user_id):
    pass

async def step7_logic(message: types.Message, user_id):
    pass

async def step8_logic(message: types.Message, user_id):
    pass

async def step9_logic(message: types.Message, user_id):
    pass