import requests

API_URL = "http://world.openfoodfacts.org/"


def get_traces():
    response = requests.get("%s/traces.json" % API_URL)
    return response.json()

def get_by_traces(product):
    pass
