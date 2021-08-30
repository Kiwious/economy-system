from item import *
import time


def add_item():
    i = input("What item do you wanna create?: ")
    time.sleep(1)
    desc = input("What description?: ")
    time.sleep(1)
    price = input("What price?: ")
    
    # creating the item and putting it into the inventory
    created_item = Item(name=i, desc=desc, price=price)
    inventory.append(created_item.name)

    q = input("Do you wanna open your inventory? y/n: ")

    if q == "y":
        print(inventory)
    else:
        print("----------------------")
        add_item()

add_item()