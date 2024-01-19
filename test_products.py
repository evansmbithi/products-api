# from products import get_products
from unittest import TestCase
import requests

class Test_products(TestCase):
	def base_url(self,param):
		return 'http://localhost:5000' + param

	def get_products(self):
		"""Test http://localhost:5000/products"""
		response = requests.get(self.base_url('/products'))
		# print(len(response.json()))
		self.assertEqual(response.status_code, 200)

	def get_product(self):
		"""Test http://localhost:5000/products/144 - with method GET"""

	def add_product(self):
		"""Test http://localhost:5000/products - with method POST"""

	def update_product(self):
		"""Test http://localhost:5000/products/144 - with method PUT"""

	def delete_product(self):
		"""Test http://localhost:5000/products/144 - with method DELETE"""