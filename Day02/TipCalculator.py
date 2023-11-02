print("Welcome to the Tip Calculator")

total = float(input("What was your total bill: ₹"))
tip_perc = int(input("How much do you want to tip: "))

total_bill = total + (total * tip_perc * 0.01)

split = int(input("How many people?: "))
per_person_cost = round((total_bill / split),2)

print(f"Each person owes: ₹{per_person_cost}.")