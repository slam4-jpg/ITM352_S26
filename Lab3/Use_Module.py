import HandyMath
from HandyMath import max, min

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: ")) 

mid = HandyMath.midpoint(number1, number2)
print(f"The midpoint between {number1} and {number2} is {mid}.")        

exp = HandyMath.exponent(number1, number2)
print(f"{number1} raised to the power of {number2} is approximately {exp}.")  

max_value = HandyMath.max(number1, number2)
print(f"The maximum value between {number1} and {number2} is approximately {max_value}.")

min_value = HandyMath.min(number1, number2)     
print(f"The minimum value between {number1} and {number2} is approximately {min_value}.")

Sqrt1 = HandyMath.sqrt(number1)
print(f"The square root of {number1} is {Sqrt1}.")