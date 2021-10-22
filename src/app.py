#!/usr/bin/env python3

from flask import Flask, json, request


companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]
products = [{"id": 1, "name": "laptop"}, {"id": 1, "name": "headphones"}]
api = Flask(__name__)

@api.route('/companies', methods=['GET'])
def get_companies():
  return json.dumps(companies)

@api.route('/products', methods=['GET'])
def get_produts():
  return json.dumps(products)

@api.route('/products', methods=['POST'])
def post_products():
  products.append(request.get_json(force=True))
  return '', 204 
  



if __name__ == '__main__':
    api.run(host="0.0.0.0", debug=True)
