from flask import Flask, render_template, request, redirect
import database

app = Flask(__name__)
database.connect()

@app.route('/', methods=['GET', 'POST'])
def index():
    search = request.form.get('search') if request.method == 'POST' else None
    products = database.get_all_products(search)
    return render_template('index.html', products=products, search=search)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    category = request.form['category']
    price = float(request.form['price'])
    stock = int(request.form['stock'])
    database.add_product(name, category, price, stock)
    return redirect('/')

@app.route('/update', methods=['POST'])
def update():
    product_id = int(request.form['id'])
    name = request.form['name']
    category = request.form['category']
    price = float(request.form['price'])
    stock = int(request.form['stock'])
    database.update_product(product_id, name, category, price, stock)
    return redirect('/')

@app.route('/delete/<int:product_id>')
def delete(product_id):
    database.delete_product(product_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
