# from products import app
from unittest import TestCase
import requests

class TestProducts(TestCase):
	# https://stackoverflow.com/questions/43957860/python-unittest-ran-0-tests-in-0-000s
	# Pretty sure you need test somewhere in the method name. – 
	# The TestCase methods to be run must start with 'test'! – 
	# Yes! Strange, did not know about this restriction. Thank you kind sirs. 

	def base_url(self,param):
		return 'http://localhost:5000' + param

	def test_get_products(self):
		"""Test GET all products http://localhost:5000/products"""
		response = requests.get(self.base_url('/products'))
		# print(len(response.json()))
		self.assertEqual(response.status_code, 200)

	def test_get_product(self):
		"""Test GET product 144 http://localhost:5000/products/144 - with method GET"""
		raise Exception("not implemented")

	def test_add_product(self):
		"""Test ADD product http://localhost:5000/products - with method POST"""
		raise Exception("not implemented")

	def test_update_product(self):
		"""Test UPDATE product 144 http://localhost:5000/products/144 - with method PUT"""
		raise Exception("not implemented")

	def test_delete_product(self):
		"""Test DELETE product 144 http://localhost:5000/products/144 - with method DELETE"""
		raise Exception("not implemented")