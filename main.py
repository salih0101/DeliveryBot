from aiogram import Dispatcher, executor, Bot
from states import Registration, GetProduct, Cart, Order
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import buttons as btns
import database
import states
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

bot = Bot(os.getenv('TOKEN'))

dp = Dispatcher(bot, storage=MemoryStorage())

about = (f'Все наши продукты: '
         '\n- Изготовлено из высококачественных растительных масел и натуральных ингредиентов.'
         '\n- Производство производится в соответствии с правилами GMP (надлежащей производственной практики).'
         '\n- Вся продукция проходит проверку на безопасность, качество и срок годности.'
         '\n- Не тестируется на животных.'
         '\n- Не содержит парабенов, спирта, формальдегида, сульфата, алюминия, минеральных отложений, бензинопроизводного сырья.'
         '\n- Не используются вещества, которые могут быть канцерогенными, мутагенными и токсичными для репродукции.'
         '\n- Не содержит синтетических отдушек, синтетических красителей, вредных консервантов, SLS и SLES.'
         '\n- Не содержит «генетически модифицированного (ГМО)» сырья')


@dp.message_handler(commands=['start'])
async def start_message(message):
    # ---Получить user_id пользователя
    user_id = message.from_user.id
    # ---Происходит проверка в базе
    checker = database.check_user(user_id)
    if checker:
        await message.answer('Приветствуем вас в нашем Онлайн магазине ActiveBee🐝\n\nВыберите раздел🔽',
                             reply_markup=btns.main_menu())
    else:
        await message.answer(
            'Приветствую, Пройдите простую регистрацию чтобы в дальнейшем не было проблем!\n\nОтправьте Имя для регистрации!',
            reply_markup=btns.ReplyKeyboardMarkup())
        # ---Переход на этап получения имени----
        await Registration.getting_name_state.set()

# ---Этап получения имени----
@dp.message_handler(state=Registration.getting_name_state)
async def get_name(message, state=Registration.getting_name_state):
    # ---Получаем отправленное имя
    user_answer = message.text

    # ---Временно сохраняем---
    await state.update_data(name=user_answer)
    await message.answer('Имя сохранил!\n\nОтправьте номер телефона!', reply_markup=btns.phone_number_kb())

    # ---Переход на этап получения номера---
    await Registration.getting_phone_number.set()

# ---Этап получения номера телефона---
@dp.message_handler(state=Registration.getting_phone_number, content_types=['contact'])
async def get_number(message, state=Registration.getting_phone_number):
    # ---Получаем отправленный контакт---
    user_answer = message.contact.phone_number

    # ---Временно сохраняем---
    await state.update_data(number=user_answer)
    await message.answer('Номер сохранил!\n\nВыберите пол👫', reply_markup=btns.gender_kb())

    # ---Переход на этап получения пола
    await Registration.getting_gender.set()

# ---Этап получения пола
@dp.message_handler(state=Registration.getting_gender)
async def get_location(message, state=Registration.getting_gender):
    # ---Получаем пол
    user_answer = message.text
    await message.answer('Успешно зарегистрирован📝!\n\nВыберите раздел🔽', reply_markup=btns.main_menu())

    # ---Сохраняем пользователя
    all_info = await state.get_data()
    name = all_info.get('name')
    phone_number = all_info.get('number')
    latitude = all_info.get('latitude')
    longitude = all_info.get('longitude')
    gender = user_answer
    user_id = message.from_user.id
    database.add_user(user_id, name, phone_number, latitude, longitude, gender)
    print(database.get_users())
    # ---Остановка
    await state.finish()

# ----Обработчик для получения данных----

@dp.message_handler(state=GetProduct.getting_pr_name, content_types=['text'])
async def choose_count(message):
    user_answer = message.text
    user_id = message.from_user.id
    # Актуальный список продуктов
    user_data = await dp.current_state(user=user_id).get_data()
    category_id = user_data.get('category_id')

    actual_products = [i[0] for i in database.get_name_product(category_id)]
    # print(actual_products)
# Кнопка назад после нажатие кнопки назад если нажал не выбрав товар
    if user_answer == 'Назад◀️':
        await message.answer('Выберите категорию🔽', reply_markup=btns.catalog_folder())

        await dp.current_state(user=user_id).finish()

    elif user_answer in actual_products:

        product_info = database.get_all_info_product(user_answer)
        await bot.send_photo(user_id, photo=product_info[4],
                             caption=f'{product_info[0]}\n\nЦена: {product_info[2]} $\n\nОписание: {product_info[3]}\n\n@activebee_bot\n\nВыберите количество1️⃣2️⃣3️⃣',
                             reply_markup=btns.product_count())

        await dp.current_state(user=user_id).update_data(user_product=message.text, price=product_info[2])

        await states.GetProduct.getting_pr_count.set()

# --- Обработчик для получения количества продукта ---
@dp.message_handler(state=GetProduct.getting_pr_count)
async def text_message3(message, state=GetProduct.getting_pr_count):
    product_count = message.text
    user_data = await state.get_data()
    user_product = user_data.get('user_product')
    category_id = user_data.get('category_id')
    pr_price = float(user_data.get('price').replace(',', '.'))

    if product_count.isnumeric():
        database.add_pr_to_cart(message.from_user.id, user_product, pr_price, int(product_count))

        await message.answer('Товар добавлен в корзину✅\n\nВыберите продукт🔽', reply_markup=btns.catalog_folder())
        await state.finish()

    elif message.text != 'Назад◀️':
        await message.answer('Выберите количество используя кнопки🔽', reply_markup=btns.product_count())

    else:
        await message.answer('Выберите товар из списка🔽', reply_markup=btns.count_kb(category_id))
        await states.GetProduct.getting_pr_name.set()


# ---Обработчик действий корзины
@dp.message_handler(state=Cart.waiting_for_product)
async def cart_function(message, state=Cart.waiting_for_product):
    user_answer = message.text
    user_id = message.from_user.id

    if user_answer == 'Назад◀️':
        await message.answer('❗️Вы вернулись в Главное меню❗️\n\nВыберите раздел🔽', reply_markup=btns.main_menu())
        await dp.current_state(user=message.from_user.id).finish()

    # ---Проверка на то что было выбрано
    elif user_answer == 'Очистить🆑':
        # ---Очищаем корзину из базы(для конкретного пользователя)
        database.delete_from_cart(user_id)
        await message.answer('Корзина очищена✅\n\n❗️❗️Нажмите кнопку Назад❗️❗️')
    # else:
    #     await message.answer('Выберите разд')

    if user_answer == 'Оформить заказ✅':
        # ---Получить данные из корзины
        user_cart = database.get_user_cart(message.from_user.id)
        # ---Проверка есть ли вообще что-то в базе
        if user_cart:
            # ---Формируем сообщения
            result_answer = 'Ваш заказ✅🔽:\n\n'
            admin_message = 'Новый заказ✅✅:\n\n'
            total_price = 0

            for i in user_cart:
                result_answer += f'- {i[1]}: {i[-1]} шт = {i[3]:.2f}$\n\n'
                admin_message += f'- {i[1]}: {i[-1]} шт = {i[3]:.2f}$\n'
                total_price += i[3]

            admin_message += f'Номер телефона: {i[2]}\n\nИтог: {total_price:.2f}'
        await message.answer('Раздел оформления заказа🔽', reply_markup=btns.confirmation_kb())

    elif user_answer == 'Отменить':
        await message.answer('❗️Вы вернулись в Главное меню❗️', reply_markup=btns.main_menu())

    elif user_answer == 'Подтвердить':
        # ---Получить данные из корзины
        user_cart = database.get_user_cart(message.from_user.id)
        # ---Проверка есть ли вообще что-то в базе
        if user_cart:
            # ---Формируем сообщения
            result_answer = 'Ваш заказ✅🔽:\n\n'
            admin_message = 'Новый заказ✅✅:\n\n'
            total_price = 0

            for i in user_cart:
                result_answer += f'- {i[1]}: {i[-1]} шт = {i[3]:.2f}$\n\n'
                admin_message += f'- {i[1]}: {i[-1]} шт = {i[3]:.2f}$\n\n'
                total_price += i[3]

            admin_message += f'Номер телефона: {i[2]}\n\nИтог: {total_price:.2f}$'
            # ---Отправка пользователю
            await message.answer(result_answer, reply_markup=btns.main_menu())
            print(user_cart)
            await message.answer('Успешно оформлен✅\n\n')
            await state.finish()
            # ---Отправка админу
            await bot.send_message(5928000362, admin_message)
            # await bot.send_message(123283566, admin_message)
            # ---Очистим корзину
            database.delete_from_cart(user_id)


# ---Независимый обработчик текста для основного меню
@dp.message_handler(content_types=['text'])
async def main_menu(message):
    user_answer = message.text
    user_id = message.from_user.id

    # Актуальный список продуктов
    # Проверка на какую кнопку нажал пользователь
    if user_answer == 'Корзина🗑':
        # Получить из базы корзину пользователя
        user_cart = database.get_user_cart(message.from_user.id)
        # ---Проверка есть ли вообще что-то в базе
        if user_cart:
            # Формируем сообщение
            result_answer = 'Ваша корзина🗑:\n\n'
            total_price = 0

            for i in user_cart:
                result_answer += f'- {i[1]}: {i[-1]} шт = {i[3]:.2f}$\n\n'
                total_price += i[3]
            await message.answer(result_answer, reply_markup=btns.cart_kb())
            await Cart.waiting_for_product.set()

        else:
            await message.answer('Ваша корзина пустая🗑')

    # ---Если отправлено сообщения - это продукт
    if user_answer == 'Каталог📦':
        await message.answer('Выберите категорию🔽', reply_markup=btns.catalog_folder())

    elif user_answer == 'Назад🔙':
        await message.answer('❗️Вы вернулись в Главное меню❗️\n\nВыберите раздел🔽', reply_markup=btns.main_menu())

    elif user_answer == 'КАПЛИ / СПРЕИ':
        await dp.current_state(user=user_id).update_data(category_id=11)
        await message.answer('Выберите продукт🔽', reply_markup=btns.spray_kb())
        await states.GetProduct.getting_pr_name.set()

    elif user_answer == 'КАПСУЛЫ / ТАБЛЕТКИ':
        await dp.current_state(user=user_id).update_data(category_id=22)
        await message.answer('Выберите продукт🔽', reply_markup=btns.tablets_kb())
        await states.GetProduct.getting_pr_name.set()

    elif user_answer == 'СИРОПЫ':
        await dp.current_state(user=user_id).update_data(category_id=33)
        await message.answer('Выберите продукт🔽', reply_markup=btns.syrup_kb())
        await states.GetProduct.getting_pr_name.set()

    elif user_answer == 'ПАСТЫ':
        await dp.current_state(user=user_id).update_data(category_id=44)
        await message.answer('Выберите продукт🔽', reply_markup=btns.pastes_kb())
        await states.GetProduct.getting_pr_name.set()

    elif user_answer == 'ОСТАЛЬНОЕ':
        await dp.current_state(user=user_id).update_data(category_id=55)
        await message.answer('Выберите продукт🔽', reply_markup=btns.other_pr_kb())
        await states.GetProduct.getting_pr_name.set()

# Кнопка назад после выбора количество товара если выбрал товар
    if user_answer == 'Назад◀️':
        await message.answer('Выберите категорию🔽', reply_markup=btns.catalog_folder())

    elif user_answer == 'О нас':
        await message.answer(about)

    elif user_answer == 'Контакты☎️':
        await message.answer(f'📞 Телефон:\n+998990952992\n+998990902992 \n\nTelegram: @activebee_tashkent'
                             f'\n\n🚚  Цена доставки по городу: 20000 сум')

    elif user_answer == 'Список заказов📄':
        # ---Получить данные из корзины
        user_cart = database.get_user_cart(message.from_user.id)
        # ---Проверка есть ли вообще что-то в базе
        if user_cart:
            # ---Формируем сообщения
            result_answer = 'Ваш заказ✅🔽:\n\n'
            admin_message = 'Новый заказ✅✅:\n\n'
            total_price = 0

            for i in user_cart:
                result_answer += f'- {i[1]}: {i[-1]} шт = {i[3]:.2f}$\n\n'
                admin_message += f'- {i[1]}: {i[-1]} шт = {i[3]:.2f}$\n\n'
                total_price += i[3]

            admin_message += f'-Номер телефона: {i[2]}\n\nИтог: {total_price:.2f}$'
            # ---Отправка пользователю
            await message.answer(result_answer, reply_markup=btns.order_kb())

            await Order.waiting_accept.set()

        else:
            await message.answer('Ваша корзина пустая🗑\n\n'
                                 'Для выбора продукта нажмите кнопку <Каталог>')

# Order list
@dp.message_handler(state=Order.waiting_accept)
async def accept_order(message):
    user_answer = message.text
    user_id = message.from_user.id
    if user_answer == 'Назад◀️':
        await message.answer('❗️Вы вернулись в Главное меню ActiveBee❗️\n\nВыберите раздел🔽', reply_markup=btns.main_menu())
        await dp.current_state(user=message.from_user.id).finish()

    elif user_answer == 'Оформить заказ':
        # ---Получить данные из корзины
        user_cart = database.get_user_cart(message.from_user.id)
        # ---Проверка есть ли вообще что-то в базе
        if user_cart:
            # ---Формируем сообщения
            result_answer = 'Ваш заказ✅🔽:\n\n'
            admin_message = 'Новый заказ✅✅:\n\n'
            total_price = 0

            for i in user_cart:
                result_answer += f'- {i[1]}: {i[-1]} шт = {i[3]:.2f}\n\n'
                admin_message += f'- {i[1]}: {i[-1]} шт = {i[3]:.2f}\n\n'
                total_price += i[3]

            admin_message += f'Номер телефона: {i[2]}\n\nИтог: {total_price:.2f}$'
            # ---Отправка пользователю
            await message.answer(result_answer, reply_markup=btns.main_menu())
            print(user_cart)
            await message.answer('Успешно оформлен✅\n\n')
            await bot.send_message(5928000362, admin_message)
            await dp.current_state(user=message.from_user.id).finish()
            database.delete_from_cart(user_id)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)