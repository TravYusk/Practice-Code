# Travis Yuskevich
# SPC ID 2543201
# User inputs the meal cost and tip percentage.
# The tip amount is calculated by multiplying the meal cost by the tip percentage.
# Then converted to a decimal.
# The tax is calculated by multiplying the meal cost by the tax.
# The total is the sum of the meal cost, tip amount, and tax amount.
# The result is displayed with two decimal places and commas.

# 7% tax rate constant decimal
tax_rate = 0.07

# Input: Cost of the meal and the tip percent from the user
meal_cost = float(input('Enter the cost of the meal (in dollars): '))
tip_percent = int(input('Enter the tip percentage (whole number): '))

# Calculating tip amount
tip_amount = meal_cost * (tip_percent / 100)

# Calculating tax amount
tax_amount = meal_cost * tax_rate

# Calculate the total
total = meal_cost + tip_amount + tax_amount

# Display results
print(f"Meal cost: ${meal_cost:.2f}")
print(f"Tip amount ({tip_percent}%): ${tip_amount:.2f}")
print(f"Tax amount (7%): ${tax_amount:.2f}")
print(f"Grand total: ${total:.2f}")
