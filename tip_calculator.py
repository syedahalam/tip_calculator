print("Welcome to the Tip Calculator")
bill = float(input("What was the Total Bill?  $"))
total_number_people = int(input("How many people to split the bill? "))
tip = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
total_tip = round(((tip/100)*bill), 2)
print(f"Bill is ${bill}")
print(f"Tip is ${total_tip}")
total = total_tip+bill
print(f" Total + Tip is ${total}")
final = total//total_number_people
each = round(final, 2)
print(f"Each person has to chip in = ${each}")
