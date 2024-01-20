import requests
from unittest import TestCase
from dataclasses import asdict, dataclass
import json
import random
import unittest


class TestProducts(TestCase):
	# https://stackoverflow.com/questions/43957860/python-unittest-ran-0-tests-in-0-000s
	# Pretty sure you need test somewhere in the method name. – 
	# The TestCase methods to be run must start with 'test'! – 
	# Yes! Strange, did not know about this restriction. Thank you kind sirs. 

	# new_product = New_data(146,'Black Market',3.99).tojson()
		
	new_product = {'id':random.randint(100,200), 'name': 'Black Market', 'price':3.99}
	product_update = {'price':2.50}
	header = {'Content-Type':'application/json'}

	def base_url(self,param):
		return 'http://localhost:5000' + param

	def get_products(self):
		response = requests.get(self.base_url('/products'))
		return response

	def add_product(self, header=header, body=new_product):
		response = requests.post(self.base_url('/products'), headers = header, json = body)
		return response

	def get_product(self,product_id=new_product['id']):
		response = requests.get(self.base_url(f'/products/{product_id}'))
		return response

	def update_product(self,product_id=new_product['id'], body=product_update):
		response = requests.put(self.base_url(f'/products/{product_id}'), json=body)
		return response

	def delete_product(self,product_id=new_product['id']):
		response = requests.delete(self.base_url(f'/products/{product_id}'))
		return response
	
########################### TESTS BEGIN HERE #############################################
	
	def setUp(self):
		self.add_product()

	def tearDown(self):
		self.delete_product()
	
	def test_get_products(self):
		"""Test GET all products http://localhost:5000/products"""
		response = self.get_products()
		# self.assertEqual(len(response.json()), 3)
		self.assertEqual(response.status_code, 200)
		print(self.get_products().json())

	def test_add_product(self):
		"""Test ADD product http://localhost:5000/products - with method POST"""
		response = self.add_product()
		self.assertEqual(response.status_code, 201)
		# self.assertEqual(len(self.get_products().json()), 4)
		print(self.get_products().json())
		self.delete_product()
		

	def test_get_product(self):
		"""Test GET product 146 http://localhost:5000/products/146 - with method GET"""
		response = self.get_product()
		self.assertEqual(response.status_code, 200)
		self.assertDictEqual(self.new_product,response.json())
		print(self.get_products().json())

	def test_update_product(self):
		"""Test UPDATE product 146 http://localhost:5000/products/146 - with method PUT"""
		response = self.update_product()
		self.assertEqual(response.status_code, 200)
		print(self.get_products().json())

	def test_delete_product(self):
		"""Test DELETE product 146 http://localhost:5000/products/146 - with method DELETE"""
		response = self.delete_product()
		self.assertEqual(response.status_code, 204)
		print(self.get_products().json())
		# raise Exception("not implemented")


# if __name__ == '__main__':
#     unittest.main()
		

@dataclass
class New_data:
	id: int
	name: str
	price: int

	def __init__(self, id, name, price):
		self.id = id
		self.name = name
		self.price = price
	
	def tojson(self):
		return json.dumps(asdict(self))