# внешние библиотеки
import asyncpg

# внутренние файлы
from config.postgre_config import (db_host, db_user,
                                   db_password, db_name)


class AdminManager:
    def __init__(self):
        self.connection = None

    # подключение к БД
    async def connect(self):
        self.connection = await asyncpg.connect(
            user=db_user,
            password=db_password,
            database=db_name,
            host=db_host,
        )

    # отключение от БД
    async def disconnect(self):
        await self.connection.close()

    # Создание таблицы
    async def create_db(self):
        await self.connect()

        await self.connection.execute(f'''
            CREATE TABLE IF NOT EXISTS ilgeri_jolu_admin (
                id SERIAL PRIMARY KEY,
                tg_id INTEGER UNIQUE,
                data_register TIMESTAMP,
            )
        ''')

        await self.disconnect()

    # Регистрация пользователя по id telegram и дата регистрации
    async def add_new_admin(self, tg_id):
        await self.connect()

        query = '''
            INSERT INTO ilgeri_jolu_clonbot (tg_id, data_register)
            VALUES ($1, NOW())
        '''
        await self.connection.execute(query, tg_id)

        await self.disconnect()