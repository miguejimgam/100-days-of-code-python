# Love calculator

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names_combined = name1.lower() + name2.lower()

t = int(names_combined.count("t"))
r = int(names_combined.count("r"))
u = int(names_combined.count("u"))
e = int(names_combined.count("e"))

true = t + r + u + e

l = int(names_combined.count("l"))
o = int(names_combined.count("o"))
v = int(names_combined.count("v"))
e = int(names_combined.count("e"))

love = l + o + v + e

score = int(str(true) + str(love))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < score < 50:
    print(f"Your score is {score}. you are allright together")
else:
    print(f"Your score is {score}")
