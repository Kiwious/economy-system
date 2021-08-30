
import time
from item import Item
from item import inventory
from item import shop_items

money = 10000



def add_item():
    
    # create an item here => Name of the item, description, and price as int
    Item(name="Kiwi", desc="Kiwis are the best", price=100)
    Item(name="Discord", desc="The whole discord company.", price=6969696969)

    q = input("Do you wanna open your inventory? y/n: ")


    if q == "y":
        print(inventory)
        time.sleep(5)
        print("----------------------")
        add_item()

    elif q == "n":
        Item.buy_item()

    else:
        print("----------------------")
        add_item()

add_item()

