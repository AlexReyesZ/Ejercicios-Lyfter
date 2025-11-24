# Exercise 1: Calculate final price with discount

# Input
product_price = float(input("Enter the price of the product: "))

# Determine discount
if product_price < 100:
    discount = product_price * 0.2
else:
    discount = product_price * 0.1

# Calculate final price
final_price = product_price - discount

# Output
print("The final price with discount included is:", final_price)