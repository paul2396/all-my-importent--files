class Item:
    # ... (Item class definition)

item1 = Item(name="phone", price=100, quantity=5)
item2 = Item(name="laptop", price=1000, quantity=3)
item3 = Item(name="ipad", price=300, quantity=2)
item4 = Item(name="monitor", price=100, quantity=2)

for item in [item1, item2, item3, item4]:
    print(f"Total price for {item.name}: {item.calculate_total_price()}")
    print(f"Price of {item.name}: {item.price}")
#!================================================
#Logical operators can be used to make complex expressions that ultimately evaluate to true or false.
#and --> both must be true
#or --> one must be true
#not --> negates (flips)


#An example with or
thunder = False
lighting  = True

if lighting or thunder:
    print("Don't go swimming!")

#An example with and
car_nice = True
on_sale = False

if car_nice and on_sale:
    print("Buy the car!") #This will not execute!

#An example with not AND and
temp_outside = 50
pool_heated = False

if temp_outside < 60 and not pool_heated:
    print("Don't go swimming!")

#this can be confusing, so it might be best to read it as english
#however, logically... pool_heated is false so not pool_heated is true.
#therefore, both sides are true. 
#!===========================================================