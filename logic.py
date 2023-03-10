from api_handler import *
from file_handler import *
import random

class Price:
    def __init__(self, price, currency):
        self.price = price
        self.currency = currency
    
    def __str__(self) -> str:
        return str(self.price) + " " + self.currency

    def get_price(self):
        return self.price

    def get_currency(self):
        return self.currency


def get_hats_with_price(api_key) -> dict[str, Price]:
    hats = read_hats()
    data = get_api_data(api_key)
    return_dict = {}
    for hat in hats:
        hat_json = data["response"]["items"][hat]["prices"]["6"]["Tradable"]["Craftable"][0]
        if hat_json["currency"] == "hat":
            return_dict[hat] = Price(1.44, "metal")
        else:
            return_dict[hat] = Price(float(hat_json["value"]), hat_json["currency"])
    return return_dict

def get_random_hat(hats):
    return random.choice(list(hats.keys()))
