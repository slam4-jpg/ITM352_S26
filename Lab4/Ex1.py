# String manipulation examples
#Name: Sidney Lam
#Date: February 2, 2026

First = input("Enter your first name: ")
MiddleInitial = input("Enter your middle initial: ")
Last = input("Enter your last name: ")  

Full_Name = First + " " + MiddleInitial + ". " + Last
print("Your full name is:", Full_Name)

print(f"Your full name is :{First} {MiddleInitial}. {Last}")

print("Your full name is :%s %s. %s" % (First, MiddleInitial, Last))

print("Your full name is :{} {}. {}".format(First, MiddleInitial, Last))

print("Your full name is :" + " ".join([First, MiddleInitial + ".", Last]))

name_list = [First, MiddleInitial, Last]
print("Your full name is :{} {}. {}".format(*name_list))