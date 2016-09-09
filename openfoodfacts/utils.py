import requests

API_URL = "http://world.openfoodfacts.org/"

def fetch(path):
    response = requests.get("%s/%s.json" % (API_URL, path))
    return response.json()

