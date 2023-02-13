print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give= 10, 12, or 15? ")
people = input("How many people to split the bill? ")

bill_float = float(bill)
tip_percentage = int(tip)/100
people_int = int(people)

bill_and_tip = float(bill) + (bill_float*tip_percentage)
bill_divided = round(bill_and_tip/people_int, 2)
print(f"Each person should pay: ${bill_divided}")
