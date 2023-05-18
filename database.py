import sqlite3


connection = sqlite3.connect('dostavka.db')


sql = connection.cursor()




def add_user(user_id, name, phone_number, latitude, longitude, gender):

    connection = sqlite3.connect('dostavka.db')
    sql = connection.cursor()
    sql.execute('INSERT INTO users VALUES (?,?,?,?,?,?);',
                (user_id, name, phone_number, latitude, longitude, gender))
    connection.commit()

    return add_user



def get_users():
    connection = sqlite3.connect('dostavka.db')
    sql = connection.cursor()
    users = sql.execute('SELECT name, id, gender FROM users;')
    return users.fetchall()



def delete_user():
    connection = sqlite3.connect('dostavka.db')
    sql = connection.cursor()

    sql.execute('DELETE FROM users;')

    connection.commit()



def add_products(id, name, price, description, picture):
    connection = sqlite3.connect('dostavka.db')
    sql = connection.cursor()
    sql.execute("INSERT INTO products VALUES(?, ?, ?, ?);",
                (id, name, price, description, picture))
    connection.commit()



def get_all_info_product(current_product):

    connection = sqlite3.connect('dostavka.db')

    sql = connection.cursor()

    all_products = sql.execute('SELECT * FROM products WHERE name=?;', (current_product, ))

    return all_products.fetchone()



def get_name_product(category_id):
    connection = sqlite3.connect('dostavka.db')
    sql = connection.cursor()
    product_id = sql.execute('SELECT * FROM products WHERE id=?;', (category_id,))
    return product_id.fetchall()

def spray_product():
    connection = sqlite3.connect('dostavka.db')
    sql = connection.cursor()
    product_id = sql.execute('SELECT * FROM products WHERE id=11;')
    return product_id.fetchall()

def tablets_product():
    connection = sqlite3.connect('dostavka.db')
    sql = connection.cursor()
    product_id = sql.execute('SELECT * FROM products WHERE id = 22;')
    return product_id.fetchall()

def syrup_product():
    connection = sqlite3.connect('dostavka.db')
    sql = connection.cursor()
    product_id = sql.execute('SELECT * FROM products WHERE id = 33;')
    return product_id.fetchall()

def pastes_product():
    connection = sqlite3.connect('dostavka.db')
    sql = connection.cursor()
    product_id = sql.execute('SELECT * FROM products WHERE id = 44;')
    return product_id.fetchall()

def other_product():
    connection = sqlite3.connect('dostavka.db')
    sql = connection.cursor()
    product_id = sql.execute('SELECT * FROM products WHERE id = 55;')
    return product_id.fetchall()



def check_user(user_id):
    connection = sqlite3.connect('dostavka.db')
    sql = connection.cursor()
    checker = sql.execute('SELECT id FROM users WHERE id=?;',
                          (user_id,))

    if checker.fetchone():
        return True
    else:
        return False



def add_pr_to_cart(user_id, product_name, price_pr, product_count):
    connection = sqlite3.connect('dostavka.db')
    sql = connection.cursor()

    phone_number = sql.execute('select phone_number from users where id=?;', (user_id,))
    user_number = phone_number.fetchone()[0]

    sql.execute('INSERT INTO cart VALUES (?,?,?,?,?);', (user_id, product_name, user_number, price_pr*product_count, product_count))


    connection.commit()



def get_user_cart(user_id):
    connection = sqlite3.connect('dostavka.db')
    sql = connection.cursor()
    all_products_from_cart = sql.execute('SELECT * FROM cart WHERE user_id=?;',
                                         (user_id,))

    return all_products_from_cart.fetchall()



def delete_from_cart(user_id):
    connection = sqlite3.connect('dostavka.db')
    sql = connection.cursor()
    sql.execute('DELETE FROM cart WHERE user_id=?;', (user_id,))

    connection.commit()


