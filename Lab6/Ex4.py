#ask user for a year 

year = int(input("Please enter a year: "))  

#check if the year is a leap year
def isLeapYear(year):
    if year % 400 == 0:
        return "Leap year"
    elif year % 100 == 0:
        return "Not a leap year"
    elif year % 4 == 0:
        return "Leap year"
    else:
        return "Not a leap year"
    
print(isLeapYear(2004)) # Output: Leap year
print(isLeapYear(2005)) # Output: Not a leap year