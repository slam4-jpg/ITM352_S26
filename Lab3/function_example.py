#An example of creating and user your own function
# Name: Sidney Lam
# Date: January 24, 2026
import datetime

def great(name):
    """This function greets the person whose name is passed in, 
    In asddition we want to print a welcome message that 
    includes the day of the week."""
    message = "Hello" + " " + name + "!"
    x= datetime.datetime.now()
    day_of_week = x.strftime("%A")
    message += "happy" + " " + day_of_week + "!"
    return message

    user_name = input("Please enter your name: ")
    greeting_message = greet(user_name)
    print(greeting_message)