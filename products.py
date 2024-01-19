from flask import Flask, jsonify, request
import json

app = Flask("Product Server")

@app.route("/")
def hello_world():
	return "Hello World"

products = [
	{'id':143, 'name': 'Notebook', 'price':5.49},
	{'id':144, 'name': 'Black Market', 'price':1.99}
]

@app.route('/products', methods=['GET'])
def get_products():
	return jsonify(products)

# localhost:5000/products/144 - with method GET
@app.route('/products/<id>', methods=['GET'])
def get_product(id):
	id=int(id)
	product = [x for x in products if x["id"] == id][0]
	return jsonify(product)



app.run(port=5000,debug=True)

