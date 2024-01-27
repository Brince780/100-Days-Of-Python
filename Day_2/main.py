#Tip Calculator

print("Welcome to the tip calculator!")

bill_total = float(input("What was the total bill? "))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
split_bill_by = int(input("How manbiy people to split the bill? "))

tip_amount = bill_total/100
bill_with_tip = bill_total + tip_amount
each_person_should_pay = bill_with_tip/split_bill_by
payable = round(each_person_should_pay, 2)

print(f"Each person should pay: {payable}")
