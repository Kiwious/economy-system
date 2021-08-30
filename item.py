
inventory = []
shop_items1 = []


class Item:

    def __init__(self, name, desc, price):
        self.name = name
        self.desc = desc
        self.price = price

        def add_item_to_shop(name, desc, price):
            if name in shop_items1:
                pass
            else:
                shop_items1.append(f"Name: {name}, Description: {desc}, Price: {price}")

        add_item_to_shop(self.name, self.desc, self.price)

    @classmethod
    def buy_item(cls):
        from main import money
        print(shop_items1)
        question1 = input(f"What product do you wanna buy? \nYour available Money: {money}\n\n")
        print("----------------------")

        if question1 in shop_items1:
            
            if cls.price >= money:
                inventory.append(f"{cls.name}, {cls.desc}")
                print(f"{cls.name} successfully bought!")
                
        elif question1 not in shop_items1: 
            print("Item not found!")
            print("----------------------")


