from item import *
import time


def add_item():
    i = input("What item do you wanna create?: ")
    time.sleep(1)
    desc = input("What description?: ")
    
    # creating the item and putting it into the inventory
    created_item = Item(i, desc)
    inventory.append(created_item.name)

    q = input("Do you wanna open your inventory? Y/N: ")

    if q == "y":
        print(inventory)
    else:
        print("----------------------")
        add_item()

add_item()