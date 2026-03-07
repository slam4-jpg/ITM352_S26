# set up variables

age =70 
weekday = "Tuesday "
matinee = True

print(f"age: {age}")
print(f"weekday: {weekday}")
print(f"matinee: {matinee}")

price = 14 

if matinee:
    if age>=65:
        price = 5
    else:
        price = 8
elif age >= 65:
    price = 8
elif weekday =="Tuesday "
    price = 10

print (f"Ticket price: ${price} ")