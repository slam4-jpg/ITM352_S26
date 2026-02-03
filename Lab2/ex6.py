#Ask the user to enter their weight in pounds. 
# Convert the weight to kilograms (1 pound = 0.453592 kg)
#name: Sidney Lam
#date: January 22, 2026

Kg_to_pounds = 0.453592


weight_in_pounds = input("Please enter your weight in pounds: ")
weight_in_pounds_float = float(weight_in_pounds)
weight_in_kilograms = float(weight_in_pounds) * Kg_to_pounds
weight_in_kilograms_rounded = round(weight_in_kilograms,)

print("You entered:", weight_in_pounds_float)
print(f"Your weight in kilograms is: {weight_in_kilograms_rounded} kg.")

