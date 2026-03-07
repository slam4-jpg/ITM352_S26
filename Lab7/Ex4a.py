def check_budget(purchase, limit):
    if purchase > limit:
        return "This purchase is over budget!"
    else:
        return "This purchase is within budget."

# Test data
recent_purchases = [36.13, 23.87, 183.35, 22.93, 11.62]
budget = 50

# Iterate through purchases
for purchase in recent_purchases:
    message = check_budget(purchase, budget)
    print(f"{purchase}: {message}")

# Test cases
print("\nTest Cases:")
print(check_budget(75, 50))   # Over budget
print(check_budget(40, 50))   # Within budget
print(check_budget(50, 50))   # Within budget (not greater than)