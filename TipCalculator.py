# Welcome to the tip calculator
# what was the total bill
# What percent tip would you like to give? 10, 12, or 15
# How many people to split the bill?
# Each person should pay: $x.xx

# Prompt the user for the total bill, tip percentage, and number of people to split the bill
print("Welcome to the tip calculator")
TotalBill = input("What was the total bill? $")
TipPercent = input("What percent tip would you like to give? ")
People = input("How many people to split the bill? ")

# Convert the tip percentage to a decimal and add 1 to it
TipConvert = (float(TipPercent) / 100) + 1

# Calculate the amount to pay
AmountToPay = (float(TotalBill) / int(People)) * TipConvert
AmountToPay = round(AmountToPay, 2)

# Print the amount to pay
print(f"Each person should pay: ${AmountToPay}")