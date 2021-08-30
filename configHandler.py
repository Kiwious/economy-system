import time
from configparser import ConfigParser

file = "config.ini"
config = ConfigParser()
config.read(file)

item1_name = config["item1"]["name"]
item1_info = config["item1"]["description"]
item1_price = config["item1"]["price"]

item2_name = config["item2"]["name"]
item2_info = config["item2"]["description"]
item2_price = config["item2"]["price"]

item3_name = config["item3"]["name"]
item3_info = config["item3"]["description"]
item3_price = config["item3"]["price"]

item4_name = config["item4"]["name"]
item4_info = config["item4"]["description"]
item4_price = config["item4"]["price"]

item5_name = config["item5"]["name"]
item5_info = config["item5"]["description"]
item5_price = config["item5"]["price"]

item6_name = config["item6"]["name"]
item6_info = config["item6"]["description"]
item6_price = config["item6"]["price"]

item7_name = config["item7"]["name"]
item7_info = config["item7"]["description"]
item7_price = config["item7"]["price"]

item8_name = config["item8"]["name"]
item8_info = config["item8"]["description"]
item8_price = config["item8"]["price"]

with open(file, "w") as configfile:
    config.write(configfile)