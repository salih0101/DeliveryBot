from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import database


# --- Кнопка для отправки номера телефона ---
def phone_number_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Отправить номер телефона', request_contact=True)
    kb.add(button)

    return kb


# --- Кнопка для отправки локации ---
def location_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Отправить локацию', request_location=True)
    kb.add(button)

    return kb

# --- Кнопка для выбора пола---
def gender_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Мужчина👨')
    button1 = KeyboardButton('Женщина👩‍🦰')
    kb.add(button, button1)

    return kb

# --- Кнопки для выбора количество товаров
def product_count():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    buttons = [KeyboardButton(i) for i in range(1, 5)]
    back = KeyboardButton('Назад◀️')
    kb.add(*buttons)
    kb.add(back)

    return kb

# ---Кнопки с названием товаров---
def main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button = KeyboardButton('Каталог📦')
    order = KeyboardButton('Список заказов📄')
    cart = KeyboardButton('Корзина🗑')
    about = KeyboardButton('О нас')
    callback = KeyboardButton('Контакты☎️')

    kb.add(button, order, cart, callback, about)

    return kb

#---Кнопки для категории товаров---
def catalog_folder():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    spray = KeyboardButton('КАПЛИ / СПРЕИ')
    tablets = KeyboardButton('КАПСУЛЫ / ТАБЛЕТКИ')
    syrup = KeyboardButton('СИРОПЫ')
    pastes = KeyboardButton('ПАСТЫ')
    other = KeyboardButton('ОСТАЛЬНОЕ')
    back = KeyboardButton('Назад🔙')

    kb.add(spray, tablets, syrup, pastes, other, back)

    return kb

#Кнопки для подкатегории товаров
def spray_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Назад◀️')
    all_products = database.spray_product()
    #print(all_products)

    #Генерируем список кнопок с названием продуктов
    buttons = [KeyboardButton(i[0]) for i in all_products]
    kb.add(*buttons, button)

    return kb

def tablets_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Назад◀️')
    all_products = database.tablets_product()
    #print(all_products)

    #Генерируем список кнопок с названием продуктов
    buttons = [KeyboardButton(i[0]) for i in all_products]
    kb.add(*buttons, button)

    return kb

def syrup_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Назад◀️')
    all_products = database.syrup_product()
    #print(all_products)

    #Генерируем список кнопок с названием продуктов
    buttons = [KeyboardButton(i[0]) for i in all_products]
    kb.add(*buttons, button)

    return kb

def pastes_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Назад◀️')
    all_products = database.pastes_product()
    #print(all_products)

    #Генерируем список кнопок с названием продуктов
    buttons = [KeyboardButton(i[0]) for i in all_products]
    kb.add(*buttons, button)

    return kb

def other_pr_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Назад◀️')
    all_products = database.other_product()
    #print(all_products)

    #Генерируем список кнопок с названием продуктов
    buttons = [KeyboardButton(i[0]) for i in all_products]
    kb.add(*buttons, button)

    return kb


#Кнопка для выбора количество
def count_kb(category_id):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Назад◀️')
    all_products = database.get_name_product(category_id)
    #print(all_products)

    #Генерируем список кнопок с названием продуктов
    buttons = [KeyboardButton(i[0]) for i in all_products]
    kb.add(*buttons, button)

    return kb

# --- Кнопки для корзины
def cart_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button = KeyboardButton('Очистить🆑')
    button1 = KeyboardButton('Оформить заказ✅')
    # button2 = KeyboardButton('Редактировать🖊')
    back = KeyboardButton('Назад◀️')
    kb.add(button1, button, back)

    return kb

# ---Кнопки для подтверждения заказа
def confirmation_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button = KeyboardButton('Подтвердить')
    button1 = KeyboardButton('Отменить')
    back = KeyboardButton('Назад◀️')
    kb.add(button, button1, back)

    return kb

# ---Кнопки для оформления заказа ---
def order_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    # button = KeyboardButton('Наличные')
    button1 = KeyboardButton('Оформить заказ')
    back = KeyboardButton('Назад◀️')
    kb.add(button1, back)

    return kb

def user_screen():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Администратор')
    back = KeyboardButton('Назад◀️')
    kb.add(button, back)

    return kb



#----Кнопка добавления товара для администратора----
def admin_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn_add = KeyboardButton('Добавить товар')
    btn_client = KeyboardButton('Зайти как клиент')
    kb.add(btn_add, btn_client)
    return kb
