from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect("inventory.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    price REAL NOT NULL)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect("inventory.db")
    c = conn.cursor()
    c.execute("SELECT * FROM items")
    items = c.fetchall()
    conn.close()
    return render_template("index.html", items=items)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        quantity = int(request.form['quantity'])
        price = float(request.form['price'])

        conn = sqlite3.connect("inventory.db")
        c = conn.cursor()
        c.execute("INSERT INTO items (name, quantity, price) VALUES (?, ?, ?)",
                  (name, quantity, price))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template("add.html")

@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    conn = sqlite3.connect("inventory.db")
    c = conn.cursor()
    if request.method == 'POST':
        name = request.form['name']
        quantity = int(request.form['quantity'])
        price = float(request.form['price'])

        c.execute("UPDATE items SET name=?, quantity=?, price=? WHERE id=?",
                  (name, quantity, price, item_id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    c.execute("SELECT * FROM items WHERE id=?", (item_id,))
    item = c.fetchone()
    conn.close()
    return render_template("edit.html", item=item)

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    conn = sqlite3.connect("inventory.db")
    c = conn.cursor()
    c.execute("DELETE FROM items WHERE id=?", (item_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
