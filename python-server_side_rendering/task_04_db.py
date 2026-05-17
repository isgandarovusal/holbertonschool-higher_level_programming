from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

def create_database():
    """SQLite verilənlər bazasını və Products cədvəlini yaradır, ilkin datanı doldurur."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Hər dəfə tətbiq başlayanda eyni datanın dublikat olmaması üçün yoxlanış edirik
    cursor.execute('SELECT COUNT(*) FROM Products')
    if cursor.fetchone()[0] == 0:
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ''')
        conn.commit()
    conn.close()

def read_json():
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except Exception:
        return []

def read_csv():
    products = []
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except Exception:
        pass
    return products

def read_sql():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row  # Sətirləri lüğət (dict) formatında oxumaq üçün
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        for row in rows:
            products.append(dict(row))
        conn.close()
    except Exception:
        pass
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Mənbə yoxlanışı (json, csv və ya sql olmalıdır)
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    # Mənbəyə uyğun funksiyanın çağırılması
    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        data = read_sql()

    # ID-yə görə süzgəcləmə (id parametri göndərilibsə)
    if product_id:
        try:
            product_id = int(product_id)
            data = [p for p in data if p['id'] == product_id]
            if not data:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    create_database()  # Server başlamazdan əvvəl bazanı hazır edirik
    app.run(debug=True, port=5000)
