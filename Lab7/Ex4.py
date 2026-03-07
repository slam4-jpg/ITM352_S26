#recent_purchase = [36,13,23,87,183.35,22,93,11.62]
recent_purchase = []

budegt = 50
total_spent = 0

for purchase in recent_purchase:
    total_spent += purchase
    if total_spent > budegt:
        print("This purchse is over budget:", purchase)
    else:
        print("This purchase is within budget:", purchase)

#def check_budget(purchase, limit):
#ON YOUR OWN: Create a function for this and write test cases for this and use them to test the function.

