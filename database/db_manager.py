# внешние библиотеки
import asyncpg

# внутренние файлы
from config.postgre_config import (db_host, db_user,
                                    db_password, db_name)

class DatabaseManager:
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

    # Проверка наличия таблицы
    async def check_table_exists(self):
        await self.connect()

        result = await self.connection.fetchval('''
            SELECT EXISTS (
                SELECT 1
                FROM information_schema.tables
                WHERE table_name = 'ilgeri_jolu_clonbot'
            )
        ''')

        await self.disconnect()

        return result


    # Создание таблицы
    async def create_db(self):
        await self.connect()

        answers = ', '.join(f'answers_{i} VARCHAR(900)' for i in range(1, 20))

        await self.connection.execute(f'''
            CREATE TABLE IF NOT EXISTS ilgeri_jolu_clonbot (
                id SERIAL PRIMARY KEY,
                tg_id INTEGER UNIQUE,
                data_register TIMESTAMP,
                name_user VARCHAR(255),
                family_user VARCHAR(255),
                current_step INTEGER,
                {answers}
            )
        ''')

        await self.disconnect()

    # Регистрация пользователя по id telegram и дата регистрации
    async def create_user(self, tg_id):
        await self.connect()

        query = '''
            INSERT INTO ilgeri_jolu_clonbot (tg_id, data_register)
            VALUES ($1, NOW())
        '''
        await self.connection.execute(query, tg_id)

        await self.disconnect()

    # Добавление имени и фамилии в базу данных
    async def add_name_family_user(self, tg_id, name_user, family_user):
        await self.connect()

        query = '''
            UPDATE ilgeri_jolu_clonbot
            SET name_user = $2, family_user = $3
            WHERE tg_id = $1
        '''
        await self.connection.execute(query, tg_id, name_user, family_user)

        await self.disconnect()

    # добавление ответа в базу данных 
    async def save_answer(self, tg_id, number_answer, answer):
        await self.connect()

        query = f'''
            UPDATE ilgeri_jolu_clonbot
            SET answers_{number_answer} = $2
            WHERE tg_id = $1
        '''
        await self.connection.execute(query, tg_id, answer)
    
        await self.disconnect()
    
    # добавление прогресса пользователя в базу данных 
    async def update_current_step(self, tg_id, current_step):
        await self.connect()

        query = '''
            UPDATE ilgeri_jolu_clonbot
            SET current_step = $1
            WHERE tg_id = $2
        '''
        await self.connection.execute(query, current_step, tg_id)
    
        await self.disconnect()
    
    # получаем пользователя из базы данных
    async def check_user(self, tg_id):
        await self.connect()

        query = '''
            SELECT *
            FROM ilgeri_jolu_clonbot
            WHERE tg_id = $1
        '''
        result = await self.connection.fetchrow(query, tg_id)
    
        await self.disconnect()
    
        return result

    # получаем прогрес пользователя
    async def get_user_progress(self, tg_id):
        await self.connect()

        query = '''
            SELECT current_step
            FROM ilgeri_jolu_clonbot
            WHERE tg_id = $1
        '''
        result = await self.connection.fetchrow(query, tg_id)

        await self.disconnect()

        return result['current_step']






