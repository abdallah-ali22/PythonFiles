print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give?"))
num_of_people = int(input("How many people to split the bill?"))

tip = 1 + tip / 100
each_person = (total_bill / num_of_people) * tip

print(f"Each person should pay: {round(each_person,2)}")