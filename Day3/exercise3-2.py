# BMI Calculator 2.0

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = int(weight) / float(height)**2

if bmi <= 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You have a normal weight")
elif bmi < 30:
    print("You have overweight")
elif bmi < 35:
    print("You are obese")
else:
    print("You are clinically obese")