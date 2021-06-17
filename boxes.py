import math

items = int(input("Please enter the number of items: "))
items_per_box = int(input("Please enter the number of items per box: "))

solution = math.ceil(items / items_per_box)

print(f"For {items} items in the box, packing {items_per_box} items in each box, you will need {solution} boxes")