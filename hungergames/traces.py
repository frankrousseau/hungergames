import requests

API_URL = "http://world.openfoodfacts.org/"

def fetch(path):
    response = requests.get("%s/%s.json" % (API_URL, path))
    return response.json()

def get_traces():
    return fetch('traces')['tags']

def get_allergens():
    return fetch('allergens')['tags']

def get_product(barcode):
    return fetch('api/v0/product/%s' % barcode)
