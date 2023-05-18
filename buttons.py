from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import database



def phone_number_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Отправить номер телефона', request_contact=True)
    kb.add(button)

    return kb



def location_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Отправить локацию', request_location=True)
    kb.add(button)

    return kb


def gender_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Мужчина👨')
    button1 = KeyboardButton('Женщина👩‍🦰')
    kb.add(button, button1)

    return kb


def product_count():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    buttons = [KeyboardButton(i) for i in range(1, 5)]
    back = KeyboardButton('Назад◀️')
    kb.add(*buttons)
    kb.add(back)

    return kb


def main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button = KeyboardButton('Каталог📦')
    order = KeyboardButton('Список заказов📄')
    cart = KeyboardButton('Корзина🗑')
    about = KeyboardButton('О нас')
    callback = KeyboardButton('Контакты☎️')

    kb.add(button, order, cart, callback, about)

    return kb


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


def spray_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Назад◀️')
    all_products = database.spray_product()
    #print(all_products)


    buttons = [KeyboardButton(i[0]) for i in all_products]
    kb.add(*buttons, button)

    return kb

def tablets_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Назад◀️')
    all_products = database.tablets_product()
    #print(all_products)


    buttons = [KeyboardButton(i[0]) for i in all_products]
    kb.add(*buttons, button)

    return kb

def syrup_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Назад◀️')
    all_products = database.syrup_product()
    #print(all_products)


    buttons = [KeyboardButton(i[0]) for i in all_products]
    kb.add(*buttons, button)

    return kb

def pastes_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Назад◀️')
    all_products = database.pastes_product()
    #print(all_products)


    buttons = [KeyboardButton(i[0]) for i in all_products]
    kb.add(*buttons, button)

    return kb

def other_pr_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Назад◀️')
    all_products = database.other_product()



    buttons = [KeyboardButton(i[0]) for i in all_products]
    kb.add(*buttons, button)

    return kb



def count_kb(category_id):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Назад◀️')
    all_products = database.get_name_product(category_id)



    buttons = [KeyboardButton(i[0]) for i in all_products]
    kb.add(*buttons, button)

    return kb

# --- Кнопки для корзины
def cart_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button = KeyboardButton('Очистить🆑')
    button1 = KeyboardButton('Оформить заказ✅')

    back = KeyboardButton('Назад◀️')
    kb.add(button1, button, back)

    return kb


def confirmation_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button = KeyboardButton('Подтвердить')
    back = KeyboardButton('Назад◀️')
    kb.add(button, back)

    return kb


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




def admin_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn_add = KeyboardButton('Добавить товар')
    btn_client = KeyboardButton('Зайти как клиент')
    kb.add(btn_add, btn_client)
    return kb
