import requests


def get_api_data(api_key):
    url = "https://backpack.tf/api/IGetPrices/v4?key=" + api_key
    response = requests.get(url).json()
    if response["response"]["success"] == 1:
        return response
    else:
        return ValueError
