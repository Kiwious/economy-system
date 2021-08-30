# Economy System

## Adding Items
Current Items are: Dino, Sword, and Kiwi. You can add/edit these items by just changing the **Name, Info** and **Price** values inside of the ' 's.
```py
shop_items=[f"Name: 'Dino', Info: 'A big dino', Price: '{str(10)}'",
            f"Name: 'Sword', Info: 'A epic sword', Price: '{str(3)}'",
            f"Name: 'Kiwi', Info: 'Kiwi yum', Price: '{str(50)}'"]
```
            
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

## Saving feature
Please note that the saving-feature has not been added yet.
