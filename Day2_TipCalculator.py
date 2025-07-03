print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? : $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? : "))
people = int(input("How many people to split the bill? : "))

bill_total = bill + (bill / 100 * tip)
each_person = bill_total / people 
print(f"Each person should pay : ${each_person:.2f}")

print("\n")

formatted_number = "{:.2f}".format(each_person)
print(f"Each charge : ${formatted_number}")
