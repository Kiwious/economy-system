import time

shop_items=[f"Name: 'Dino', Info: 'A big dino', Price: '{str(10)}'",
            f"Name: 'Sword', Info: 'A epic sword', Price: '{str(3)}'",
            f"Name: 'Kiwi', Info: 'Kiwi yum', Price: '{str(50)}'"]

inventory = []
jobs = ["Job: Programmer, Income: 100", "Job: YouTuber, Income: 200", "Job: Artist, Income: 300"]

money = 0

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