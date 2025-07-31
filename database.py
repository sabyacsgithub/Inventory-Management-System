import sqlite3

def connect():
    conn = sqlite3.connect('inventory.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT,
            price REAL,
            stock INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def get_all_products(search_term=None):
    conn = sqlite3.connect('inventory.db')
    cur = conn.cursor()
    if search_term:
        cur.execute("SELECT * FROM products WHERE name LIKE ? OR category LIKE ?",
                    (f'%{search_term}%', f'%{search_term}%'))
    else:
        cur.execute("SELECT * FROM products")
    products = cur.fetchall()
    conn.close()
    return products

def add_product(name, category, price, stock):
    conn = sqlite3.connect('inventory.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)",
                (name, category, price, stock))
    conn.commit()
    conn.close()

def delete_product(product_id):
    conn = sqlite3.connect('inventory.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM products WHERE id=?", (product_id,))
    conn.commit()
    conn.close()

def update_product(product_id, name, category, price, stock):
    conn = sqlite3.connect('inventory.db')
    cur = conn.cursor()
    cur.execute('''UPDATE products SET name=?, category=?, price=?, stock=? WHERE id=?''',
                (name, category, price, stock, product_id))
    conn.commit()
    conn.close()
