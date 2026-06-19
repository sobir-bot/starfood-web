import sqlite3

from config import DATABASE_NAME


db = sqlite3.connect(
    DATABASE_NAME,
    check_same_thread=False
)

cursor = db.cursor()


# ==========================
# USERS
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    telegram_id INTEGER UNIQUE,

    full_name TEXT,

    phone TEXT,

    latitude REAL,

    longitude REAL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")


# ==========================
# ORDERS
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER,

    total_price INTEGER,

    status TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")


# ==========================
# ORDER ITEMS
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS order_items(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    order_id INTEGER,

    product_name TEXT,

    quantity INTEGER,

    price INTEGER

)
""")

db.commit()


# ==========================
# USER FUNCTIONS
# ==========================

def add_user(
    telegram_id,
    full_name
):

    cursor.execute(
        """
        INSERT OR IGNORE INTO users
        (
            telegram_id,
            full_name
        )
        VALUES (?,?)
        """,

        (
            telegram_id,
            full_name
        )
    )

    db.commit()


def save_phone(
    telegram_id,
    phone
):

    cursor.execute(
        """
        UPDATE users

        SET phone=?

        WHERE telegram_id=?
        """,

        (
            phone,
            telegram_id
        )
    )

    db.commit()



def save_location(
    telegram_id,
    latitude,
    longitude
):

    cursor.execute(
        """
        UPDATE users

        SET

        latitude=?,

        longitude=?

        WHERE telegram_id=?
        """,

        (
            latitude,
            longitude,
            telegram_id
        )
    )

    db.commit()



def get_user(telegram_id):

    cursor.execute(

        """
        SELECT *

        FROM users

        WHERE telegram_id=?
        """,

        (telegram_id,)
    )

    return cursor.fetchone()



# ==========================
# ORDER
# ==========================

def create_order(
    user_id,
    total_price,
    status
):

    cursor.execute(

        """
        INSERT INTO orders

        (
            user_id,
            total_price,
            status
        )

        VALUES (?,?,?)
        """,

        (
            user_id,
            total_price,
            status
        )
    )

    db.commit()

    return cursor.lastrowid



def add_order_item(

    order_id,

    product_name,

    quantity,

    price

):

    cursor.execute(

        """
        INSERT INTO order_items

        (
            order_id,

            product_name,

            quantity,

            price
        )

        VALUES (?,?,?,?)
        """,

        (
            order_id,

            product_name,

            quantity,

            price
        )
    )

    db.commit()



# ==========================
# GET
# ==========================

def get_orders():

    cursor.execute(

        """
        SELECT *

        FROM orders

        ORDER BY id DESC
        """
    )

    return cursor.fetchall()



def get_order_items(order_id):

    cursor.execute(

        """
        SELECT *

        FROM order_items

        WHERE order_id=?
        """,

        (order_id,)
    )

    return cursor.fetchall()
def update_order_status(order_id, status):

    cursor.execute(
        """
        UPDATE orders
        SET status = ?
        WHERE id = ?
        """,
        (status, order_id)
    )

    db.commit()


def get_total_orders():

    cursor.execute(
        "SELECT COUNT(*) FROM orders"
    )

    return cursor.fetchone()[0]


def get_total_users():

    cursor.execute(
        "SELECT COUNT(*) FROM users"
    )

    return cursor.fetchone()[0]


def get_total_sales():

    cursor.execute(
        "SELECT SUM(total_price) FROM orders"
    )

    result = cursor.fetchone()[0]

    if result is None:
        return 0

    return result