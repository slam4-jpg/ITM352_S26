# Handy Libary of Marhematical Functions
#Name: Sidney Lam
#Date: January 27, 2026
def midpoint(num1, num2):
    """calculate the midpoint of two numbers."""
    mid = (num1 + num2) / 2
    return mid

def sqrt(number):
    """Calculate the square root of a number."""
    if number < 0:
        return None
    return number ** 0.5

def exponent(base, exp, precision):
    """Calculate the exponent of a base to a given exponent."""
    result = base ** exp
    Rounded_result = round(result, precision)   
    return Rounded_result

def max(num1, num2):
    return (num1 + num2 + abs(num1 - num2)) / 2

def min(num1, num2):
    return (num1 + num2 - abs(num1 - num2)) / 2