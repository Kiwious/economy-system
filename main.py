
import time
from typing import ItemsView
from item import Item
from item import inventory
from item import shop_items1

# your money
money = 10000

def open_shop():

    Item.buy_item()

def do_shit():
    
    # create an item here => Name of the item, description, and price as int
    Item(name="Pizza", desc="Delicious pizza, yum!", price=25)
    Item(name="Keyboard", desc="Mechanical keyboard with Outemu blue switches.", price=50)
    
    print("----------------------")
    question = input("Do you wanna open your inventory? y/n: ")

    if question == "y":
        print("----------------------")
        print(inventory)
        print("----------------------")
        do_shit()

    elif question == "n":

        shop_question = input("Do you wanna open the shop? y/n: ")
        print("----------------------")

        if shop_question == "y":
            open_shop()
        elif shop_question == "n":
            do_shit()

do_shit()

