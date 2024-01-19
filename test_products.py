# from products import get_products
import requests
import json

def base_url(param):
	return 'http://localhost:5000' + param

response = requests.get(base_url('/products'))
print(len(response.json()))
print(response.status_code)
