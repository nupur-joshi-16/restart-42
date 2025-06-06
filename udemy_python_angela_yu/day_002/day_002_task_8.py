print("Welcome to tip calculator!")
bill_amount = float(input("What was the total bill? : ₹"))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? : "))
tip_amount = (tip_percent / 100) * bill_amount
total_amount = bill_amount + tip_amount
people = int(input("How many people to split the bill: "))
each_person_pay = total_amount / people
round_amount = round(each_person_pay, 2)

print("-----------------------------------")
print(f"Bill\t\t\t : ₹{bill_amount}")
print(f"Tip ({tip_percent}%)\t\t : ₹{tip_amount}")
print(f"Total Amount\t\t : ₹{total_amount}")
print(f"people\t\t\t : {people}")
print("-----------------------------------")
print(f"Each person should pay\t : ₹{round_amount}")
print("-----------------------------------")