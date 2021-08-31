from os import sep
import time
from configparser import ConfigParser
from configHandler import *
import bcolors
from tabulate import tabulate

file = "config.ini"
config = ConfigParser()
config.read(file)

shop_items=[f"Name: {bcolors.bcolors.ENDC}'{item1_name}{bcolors.bcolors.BOLD}{bcolors.bcolors.ENDC}'{bcolors.bcolors.BOLD}, Info: {bcolors.bcolors.ENDC}'{item1_info}',{bcolors.bcolors.BOLD} Price: {bcolors.bcolors.ENDC}'{str(item1_price)}'\n",
            f"Name: {bcolors.bcolors.ENDC}'{item2_name}{bcolors.bcolors.BOLD}{bcolors.bcolors.ENDC}'{bcolors.bcolors.BOLD}, Info: {bcolors.bcolors.ENDC}'{item2_info}',{bcolors.bcolors.BOLD} Price: {bcolors.bcolors.ENDC}'{str(item2_price)}'\n",
            f"Name: {bcolors.bcolors.ENDC}'{item3_name}{bcolors.bcolors.BOLD}{bcolors.bcolors.ENDC}'{bcolors.bcolors.BOLD}, Info: {bcolors.bcolors.ENDC}'{item3_info}',{bcolors.bcolors.BOLD} Price: {bcolors.bcolors.ENDC}'{str(item3_price)}'\n",
            f"Name: {bcolors.bcolors.ENDC}'{item4_name}{bcolors.bcolors.BOLD}{bcolors.bcolors.ENDC}'{bcolors.bcolors.BOLD}, Info: {bcolors.bcolors.ENDC}'{item4_info}',{bcolors.bcolors.BOLD} Price: {bcolors.bcolors.ENDC}'{str(item4_price)}'\n",
            f"Name: {bcolors.bcolors.ENDC}'{item5_name}{bcolors.bcolors.BOLD}{bcolors.bcolors.ENDC}'{bcolors.bcolors.BOLD}, Info: {bcolors.bcolors.ENDC}'{item5_info}',{bcolors.bcolors.BOLD} Price: {bcolors.bcolors.ENDC}'{str(item5_price)}'\n",
            f"Name: {bcolors.bcolors.ENDC}'{item6_name}{bcolors.bcolors.BOLD}{bcolors.bcolors.ENDC}'{bcolors.bcolors.BOLD}, Info: {bcolors.bcolors.ENDC}'{item6_info}',{bcolors.bcolors.BOLD} Price: {bcolors.bcolors.ENDC}'{str(item6_price)}'\n",
            f"Name: {bcolors.bcolors.ENDC}'{item7_name}{bcolors.bcolors.BOLD}{bcolors.bcolors.ENDC}'{bcolors.bcolors.BOLD}, Info: {bcolors.bcolors.ENDC}'{item7_info}',{bcolors.bcolors.BOLD} Price: {bcolors.bcolors.ENDC}'{str(item7_price)}'\n",
            f"Name: {bcolors.bcolors.ENDC}'{item8_name}{bcolors.bcolors.BOLD}{bcolors.bcolors.ENDC}'{bcolors.bcolors.BOLD}, Info: {bcolors.bcolors.ENDC}'{item8_info}',{bcolors.bcolors.BOLD} Price: {bcolors.bcolors.ENDC}'{str(item8_price)}'\n"]

target = {39:None, 91:None, 93:None}
inventory = []
jobs = ["Job: Programmer, Income: 100", "Job: YouTuber, Income: 200", "Job: Artist, Income: 300"]
money = 1110

def buy_item(Name):
    for item in shop_items:
        item=item.split("'")
        if str(item[1]) == Name:
            global money
            if money >= int(item[5]):
                inventory.append(item)
                money = money - int(item[5])
            else:
                print("You don't have enough money!")
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
    print(*shop_items, sep="'")

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
    prompt1 = input("What do you want to do?\nA: Buy something: \nB: Work and get money: \nC: See your inventory: ")

    if prompt1 == "A":
        open_shop()

    elif prompt1 == "B":
        job_prompt()

    elif prompt1 == "C":
        print("----------------------------------------------------")
        print(*inventory, sep=",")
        time.sleep(2)
        start()

start()

with open(file, "w") as configfile:
    config.write(configfile)