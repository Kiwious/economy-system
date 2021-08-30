import time
from configparser import ConfigParser
from configHandler import *

file = "config.ini"
config = ConfigParser()
config.read(file)

shop_items=[f"Name: '{item1_name}', Info: '{item1_info}', Price: '{str(item1_price)}'",
            f"Name: '{item2_name}', Info: '{item2_info}', Price: '{str(item2_price)}'",
            f"Name: '{item3_name}', Info: '{item3_info}', Price: '{str(item3_price)}'",
            f"Name: '{item4_name}', Info: '{item4_info}', Price: '{str(item4_price)}'",
            f"Name: '{item5_name}', Info: '{item5_info}', Price: '{str(item5_price)}'",
            f"Name: '{item6_name}', Info: '{item6_info}', Price: '{str(item6_price)}'",
            f"Name: '{item7_name}', Info: '{item7_info}', Price: '{str(item7_price)}'",
            f"Name: '{item8_name}', Info: '{item8_info}', Price: '{str(item8_price)}'"]

inventory = []
jobs = ["Job: Programmer, Income: 100", "Job: YouTuber, Income: 200", "Job: Artist, Income: 300"]

money = 999999

def buy_item(Name):
    for item in shop_items:
        item=item.split("'")
        if item[1] == Name:
            global money
            if money >= int(item[5]):
                inventory.append(item)
                money = money - int(item[5])
            else:
                print("You don't have enough money!")
                time.sleep(1)
                print("Redirecting you back....")
                time.sleep(1)
                start()

def work(job):
    if job == "Programmer":
        income = 100
        global money
        money = money + income
        print(f"You worked as a {job} and got {income}!")
    elif job == "YouTuber":
        income = 200
        money = money + income
        print(f"You worked as a {job} and got {income}!")
    elif job == "Artist":
        income = 300
        money = money + income
        print(f"You worked as a {job} and got {income}!")
    else:
        print("Invalid job name!")

def job_prompt():
    print(jobs)
    print("----------------------------------------------------")
    prompt = input("What job do you want to work as?: ")
    work(prompt)
    time.sleep(2)
    print(f"Your balance is now: {money}€!")
    start()

def open_shop():
    print("----------------------------------------------------")
    print(shop_items)
    print("----------------------------------------------------")
    item = input("What do you want to buy?: ")
    buy_item(item)
    time.sleep(2)
    print(f"Successfully bought {item}!")
    time.sleep(1)
    print(f"Your balance is now {money}€!")
    time.sleep(1)
    print("Redirecting you back....")
    start()



def start():
    print("----------------------------------------------------")
    prompt1 = input("What do you want to do?\nA: Buy something, B: Work and get money: ")

    if prompt1 == "A":
        open_shop()

    elif prompt1 == "B":
        job_prompt()

start()

with open(file, "w") as configfile:
    config.write(configfile)