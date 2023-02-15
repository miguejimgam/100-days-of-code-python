# Who pays the bill?

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")

name = random.choice(names)

print(f"{name} will pay the bill today")
