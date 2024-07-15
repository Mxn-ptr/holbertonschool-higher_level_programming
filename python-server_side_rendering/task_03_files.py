#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_file(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def read_csv_file(filepath):
    products = []
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products


@app.route('/')
def home():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/items')
def items():
	items = read_json_file('items.json')
	return render_template('items.html', items=items.get('items'))

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
      
    if source == 'json':
        filepath = 'products.json'
        try:
            products = read_json_file(filepath)
        except Exception:
            return render_template('product_display.html', error="Error reading JSON file.")
    elif source == 'csv':
        filepath = 'products.csv'
        try:
            products = read_csv_file(filepath)
        except Exception:
            return render_template('product_display.html', error="Error reading CSV file.")
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        try:
            product_id = int(product_id)
            products = [product for product in products if product['id'] == product_id]
            if not products:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html', error="Invalid product ID")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
	app.run(debug=True, port=5000)
