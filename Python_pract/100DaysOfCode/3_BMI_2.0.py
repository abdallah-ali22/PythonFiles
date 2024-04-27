height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / height ** 2)

if bmi <= 18.5:
    print(bmi, "underweight")
elif bmi <= 25:
    print(bmi, "normal weight")
elif bmi <= 30:
    print(bmi, "overweight")
elif bmi <= 35:
    print(bmi, "obese")
else:
    print(bmi, "clinically obese")