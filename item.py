

inventory = []
shop_items = []


class Item:

    def __init__(self, name, desc, price):
        self.name = name
        self.desc = desc
        self.price = price

        shop_items.append(f"Item: {self.name}, Description: {self.desc}, Price: {self.price}")

    @classmethod
    def buy_item(cls):
        from main import money
        question = input(f"What product do you wanna buy? {str(shop_items)}\nYour available Money: {money}\n\n")

        if question in shop_items:
            
            if cls.price >= money:
                inventory.append(f"{cls.name}, {cls.desc}")
                print(f"{cls.name} successfully bought!")
            else: 
                print("Item not found!")


