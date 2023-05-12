import sqlite3

# ---Создать/ подключитсья к базе данных---
connection = sqlite3.connect('dostavka.db')

# ---Создаем переводчика---
sql = connection.cursor()



# ---Добавления пользователя---
def add_user(user_id, name, phone_number, latitude, longitude, gender):
    # Создать/подключиться к базе данных
    connection = sqlite3.connect('dostavka.db')
    sql = connection.cursor()
    sql.execute('INSERT INTO users VALUES (?,?,?,?,?,?);',
                (user_id, name, phone_number, latitude, longitude, gender))
    connection.commit()

    return add_user


# ---Получение пользователя---
def \
        _users():
    connection = sqlite3.connect('dostavka.db')
    sql = connection.cursor()
    users = sql.execute('SELECT name, id, gender FROM users;')
    return users.fetchall()


# ---Запрос для удаления пользователя из базы данных---
def delete_user():
    connection = sqlite3.connect('dostavka.db')
    sql = connection.cursor()
    # Отправляем запрос на удаления
    sql.execute('DELETE FROM users;')

    connection.commit()


# ---Функция для добавления продуктов---
def add_products(id, name, price, description, picture):
    connection = sqlite3.connect('dostavka.db')
    sql = connection.cursor()
    sql.execute("INSERT INTO products VALUES(?, ?, ?, ?);",
                (id, name, price, description, picture))
    connection.commit()


# ---Функция для получения всех данных о продукте---
def get_all_info_product(current_product):
    # Создать/подключиться к базе данных
    connection = sqlite3.connect('dostavka.db')
    # Создаем переводчика
    sql = connection.cursor()

    all_products = sql.execute('SELECT * FROM products WHERE name=?;', (current_product, ))

    return all_products.fetchone()


# ---Функция для получения наименований продуктов из базы данных---
def get_name_product(category_id):
    connection = sqlite3.connect('dostavka.db')
    sql = connection.cursor()
    product_id = sql.execute('SELECT * FROM products WHERE id=?;', (category_id,))
    return product_id.fetchall()

def spray_product(): #КАПЛИ / СПРЕИ
    connection = sqlite3.connect('dostavka.db')
    sql = connection.cursor()
    product_id = sql.execute('SELECT * FROM products WHERE id=11;')
    return product_id.fetchall()

def tablets_product(): #КАПСУЛЫ / ТАБЛЕТКИ
    connection = sqlite3.connect('dostavka.db')
    sql = connection.cursor()
    product_id = sql.execute('SELECT * FROM products WHERE id = 22;')
    return product_id.fetchall()

def syrup_product(): #СИРОПЫ
    connection = sqlite3.connect('dostavka.db')
    sql = connection.cursor()
    product_id = sql.execute('SELECT * FROM products WHERE id = 33;')
    return product_id.fetchall()

def pastes_product():#ПАСТЫ
    connection = sqlite3.connect('dostavka.db')
    sql = connection.cursor()
    product_id = sql.execute('SELECT * FROM products WHERE id = 44;')
    return product_id.fetchall()

def other_product(): #Остальное
    connection = sqlite3.connect('dostavka.db')
    sql = connection.cursor()
    product_id = sql.execute('SELECT * FROM products WHERE id = 55;')
    return product_id.fetchall()


# ---Функция для проверки пользователя на наличие в базе---
def check_user(user_id):
    connection = sqlite3.connect('dostavka.db')
    sql = connection.cursor()
    checker = sql.execute('SELECT id FROM users WHERE id=?;',
                          (user_id,))
    # Проверка есть ли данные из запроса
    if checker.fetchone():
        return True
    else:
        return False


# ---Функцию добавления товара в корзину---
def add_pr_to_cart(user_id, product_name, price_pr, product_count):
    connection = sqlite3.connect('dostavka.db')
    sql = connection.cursor()

    phone_number = sql.execute('select phone_number from users where id=?;', (user_id,))
    user_number = phone_number.fetchone()[0]

    sql.execute('INSERT INTO cart VALUES (?,?,?,?,?);', (user_id, product_name, user_number, price_pr*product_count, product_count))

    # Зафиксировать
    connection.commit()


# ---Создать функцию получения корзины (WHERE user_id=?)---
def get_user_cart(user_id):
    connection = sqlite3.connect('dostavka.db')
    sql = connection.cursor()
    all_products_from_cart = sql.execute('SELECT * FROM cart WHERE user_id=?;',
                                         (user_id,))

    return all_products_from_cart.fetchall()


# Создать функцию удаления корзины (WHERE user_id=?)
def delete_from_cart(user_id):
    connection = sqlite3.connect('dostavka.db')
    sql = connection.cursor()
    sql.execute('DELETE FROM cart WHERE user_id=?;', (user_id,))

    connection.commit()



# Запрос на создание таблицы
# sql.execute('CREATE TABLE users (id INTEGER, name INTEGER, phone_number TEXT, loc_lat REAL, loc_long REAL, gender TEXT);')
# sql.execute('CREATE TABLE products (name INTEGER, id INTEGER, price INTEGER, description TEXT, picture TEXT, notes TEXT);')
# sql.execute('CREATE TABLE cart (user_id INTEGER, product_name TEXT, user_number TEXT, product_price INTEGER, product_count INTEGER);')
