import random
names_string = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

# names=  names_string.split(", ")

length = len(names_string)

random_num = random.randrange(length - 1)

print(f"{names_string[random_num]} is going to buy the meal today!")