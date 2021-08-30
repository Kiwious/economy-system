# Economy System

# config.ini
If you want to modify or change certain items, than the **config.ini** file is the file you are looking for. In this file, you can change:
the **name, description** and **price** of an item.

**Example:**
```ini
[item1]
name = Dino
description = A big Dino.
price = 10
```
As you can see here, it is very easy to setup a new item. Please note that this code holds a maximum ammount of **8** Items. If you add more, the programm will eventually break, and will no longer work:
```ini
[item1-8]
name = NAME
description = ITEM_DESCIPTION
price = ITEM_PRICE
```

# Modding
## Giving yourself money
If you want to give yourself some money, just change the **money** value.
```py
money = 0
```

## Adding jobs and changing job income
By changing the **INCOME** and the **JOB_NAME** values, you can simply create, and add your own custom jobs.
```py
elif job == "JOB_NAME":
    income = INCOME
    money = money + income
    print(f"You worked as a {job} and got {income}!")
```
After that, add the **JOB_NAME** and the **INCOME** value to the **'jobs'** List, and you are done with
your custom Job!

```py
jobs = ["Job: Programmer, Income: 100", "Job: YouTuber, Income: 200", "Job: Artist, Income: 300"]
```
# Saving
## Saving feature
Please note that the saving-feature has not been added yet.
