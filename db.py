import sqlite3

DB_NAME = "inventory.db"

def connect():
    return sqlite3.connect(DB_NAME)

def init_db():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL
            )
        """)
        conn.commit()

def get_all_items():
    with connect() as conn:
        cursor = conn.execute("SELECT * FROM inventory")
        return cursor.fetchall()

def add_item(name, quantity, price):
    with connect() as conn:
        conn.execute("INSERT INTO inventory (name, quantity, price) VALUES (?, ?, ?)",
                     (name, quantity, price))
        conn.commit()

def get_item(item_id):
    with connect() as conn:
        cursor = conn.execute("SELECT * FROM inventory WHERE id = ?", (item_id,))
        return cursor.fetchone()

def update_item(item_id, name, quantity, price):
    with connect() as conn:
        conn.execute("UPDATE inventory SET name=?, quantity=?, price=? WHERE id=?",
                     (name, quantity, price, item_id))
        conn.commit()

def delete_item(item_id):
    with connect() as conn:
        conn.execute("DELETE FROM inventory WHERE id=?", (item_id,))
        conn.commit()
