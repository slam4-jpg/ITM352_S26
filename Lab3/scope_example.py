# This program demonstrate variable scope in Python
# Name: Sidney Lam
# Date: January 27, 2026

def calculate_discounted_price(price, discount):
    price = price * discount
    print(f"inside the function, the discounted price is: {price:.2f}")
    return price

discount = 0.6
price = 100.0
print(f"Original price before function call: {price:.2f}")
discounted_price = calculate_discounted_price(price, discount)

print(f"Original price after function call: {price:.2f}")
print("Discount", discount)

