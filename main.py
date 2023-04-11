from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import buttons
from states


#Подключения боту

bot = Bot('TOKEN')

#Диспетчер

dp = Dispatcher(bot)

#Обработчик команды Start

@dp.message_handler(commands=['start'])

async def start_command(message):

    start_text = f'Привет {message.from_user.first_name}\n Тест текст'

    #Получить айди ползователья
    user_id = message.from_user.id


#Ответ
    await message.answer(start_text, reply_markup=)