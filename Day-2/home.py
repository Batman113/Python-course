# Tip Calculator

print("Welcome to the tip calculator.")
Amount = float(input("What was the total bill? $"))
tip = int(input("Choose the percentage of tip you like to give? 1. 10\n2. 12\n3. 15\nTip: "))
total_person = int(input("How many people to split bill? "))
print("Discount% : 8")
total_cost = (Amount + Amount * tip * 0.01 - Amount * 0.08) / total_person
print(f"Each person have to pay: ${total_cost}")
