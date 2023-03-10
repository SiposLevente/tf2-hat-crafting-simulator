import os
from file_handler import *
from api_handler import *
from logic import *

LINE_WIDTH = 10

settings = read_settings()
hats = get_hats_with_price(settings["user_api_key"])
gameloop = True
crafted_hat_value = 0.0
spent_metal_value = 0
crafted_hats = {}


def print_owned_hats():
    print("Crafted hats:")
    counter = 0
    for hat, count in crafted_hats.items():
        print(str(count) + "x" + hat.__str__(), end="")
        if counter % LINE_WIDTH == 0 and counter != 0:
            print()
        else:
            print(", ", end="")
        counter += 1
    print("\n")

def print_profit():
    print("Refind metals spent on making hats: " + str(spent_metal_value) + " metal\nCrafted hat value: " + str(crafted_hat_value) + " metal")


def craft_hat():
    global crafted_hat_value
    global spent_metal_value
    crafted_hat = get_random_hat(hats)
    
    if crafted_hat in crafted_hats:
        crafted_hats[crafted_hat] = crafted_hats[crafted_hat] + 1
    else:
        crafted_hats[crafted_hat] = 1
    crafted_hat_value += hats[crafted_hat].price
    spent_metal_value += 3


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


if __name__ == "__main__":
    try:
        while (gameloop):
            clear()
            print_owned_hats()
            print_profit()
            try:
                print("Menu:\n1, Craft a hat!\n2, Craft 'n' hats\n3, Exit!")
                user_input = int(input())
                if user_input == 1:
                    craft_hat()
                elif user_input == 2:
                    try:
                        number_of_hats = int(input("Enter the number of hats to craft: "))
                        for _ in range(number_of_hats):
                            craft_hat()

                    except ValueError:
                        print("Invalid input! Returning to menu")

                elif user_input == 3:
                    gameloop = False
            except ValueError:
                print("Unexpected value! Please enter the input again!")
            except EOFError:
                gameloop = False
    except KeyboardInterrupt:
        exit()
