from aiogram.dispatcher.filters.state import State, StatesGroup


# ---Процессы для регистрации---
class Registration(StatesGroup):
    getting_name_state = State()
    getting_phone_number = State()
    getting_location = State()
    getting_gender = State()


#----Процесс добавления----
class Add_product(StatesGroup):
    get_name = State()  # Получаем название товара
    get_id = State()  # Получаем Айди товара
    get_price = State()  # Получаем стоимость
    get_info = State()  # Получаем описание
    get_photo = State()  # Получаем фото


#----Получения статуса----
class Admin(StatesGroup):
    get_status = State()

#----Процессы для Выбора определенного товара---

class GetProduct(StatesGroup):
    getting_pr_name = State()
    getting_pr_count = State()


# ---Процесс при работе с корзиной---
class Cart(StatesGroup):
    waiting_for_product = State()
    waiting_new_count = State()


# ---Процессы при оформлении заказа---
class Order(StatesGroup):
    waiting_location = State()
    waiting_pay_type = State()
    waiting_accept = State()
