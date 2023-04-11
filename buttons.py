from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


#--- Кнопка для отправки номера телефона---
def phone_number_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Отправить номер телефона', request_contact=True)
    kb.add(button)

    return kb


#--- Кнопка для отправки локации---
def location_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Отправить номер телефона', request_location=True)
    kb.add(button)

    return kb

#--- Кнопка для выбора пола---
def gender_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Мужчина')
    button1 = KeyboardButton('Женщина')
    kb.add(button, button1)

    return kb

#--- Кнопки для выбора количество товаров
def product_count():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    buttons = [KeyboardButton(i) for i in range(1, 10)]
    kb.add(*buttons)

    return kb

#---Кнопки с названием товаров---
def product_kb():
    pass

#--- Кнопки для корзины
def cart_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Очистить')
    button1 = KeyboardButton('Оформить заказ')
    button2 = KeyboardButton('Редактировать')
    button3 = KeyboardButton('Назад')
    kb.add(button, button1, button2, button3)

    return kb

#---Кнопки при выборе способа оплаты
def order_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Наличные')
    button1 = KeyboardButton('Картой')
    button2 = KeyboardButton('Назад')
    kb.add(button, button1, button2)

    return kb

#---Кнопки для подтверждения заказа
def confirmation():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Потвердить')
    button1 = KeyboardButton('Отменить')
    button2 = KeyboardButton('Назад')
    kb.add(button, button1, button2)

    return kb