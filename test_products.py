# from products import app
from unittest import TestCase
import requests

class TestProducts(TestCase):
	# https://stackoverflow.com/questions/43957860/python-unittest-ran-0-tests-in-0-000s
	# Pretty sure you need test somewhere in the method name. – 
	# The TestCase methods to be run must start with 'test'! – 
	# Yes! Strange, did not know about this restriction. Thank you kind sirs. 

	new_product = 	{
					'id':146, 
					'name': 'Black Market', 
					'price':3.99
					}
	update_product = {
						'price':2.50
					}

	def base_url(self,param):
		return 'http://localhost:5000' + param

	def test_get_products(self):
		"""Test GET all products http://localhost:5000/products"""
		response = requests.get(self.base_url('/products'))
		self.assertEqual(len(response.json()), 2)
		self.assertEqual(response.status_code, 200)

	def test_add_product(self):
		"""Test ADD product http://localhost:5000/products - with method POST"""
		response = requests.post(self.base_url('/products'), headers = {"dataType": "json",
    "accept":"application/json", "Content-Type":"application/json"}, data=self.new_product)
		self.assertEqual(response.status_code, 201)

	def test_get_product(self,product=new_product['id']):
		"""Test GET product 146 http://localhost:5000/products/144 - with method GET"""
		response = requests.get(self.base_url(f'/products/{product}'))
		self.assertEqual(response.status_code, 200)
		self.assertDictEqual(response.json, self.new_product)	

	def test_update_product(self,product=new_product['id']):
		"""Test UPDATE product 146 http://localhost:5000/products/146 - with method PUT"""
		response = requests.put(self.base_url(f'/products/{product}'), data=self.update_product)
		self.assertEqual(response.status_code, 204)
		self.assertDictContainsSubset(self.update_product,response.json())

	def test_delete_product(self,product=new_product['id']):
		"""Test DELETE product 146 http://localhost:5000/products/146 - with method DELETE"""
		# raise Exception("not implemented")
		response = requests.delete(self.base_url(f'/products/{product}'))
		self.assertEqual(response.status_code, 200)
		self.test_get_products()