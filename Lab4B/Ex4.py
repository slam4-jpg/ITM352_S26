# Parse through the portions of an email address
#Name: Sidney Lam
#Date: February 3, 2026


#Method 1:using split() to seprate undername and domain
Email = input("Enter your email address: ")

parts = Email.split("@")
username = parts[0]
domain = parts[1]

print("Username:", username)
print("Domain:", domain)

#Method 2: using index () and slicing to separate undername and domain
at_symbol_index = Email.index("@")
username_manual = Email[:at_symbol_index]
domain_manual = Email[at_symbol_index + 1:] 

print("Username (manual method):", username_manual)
print("Domain (manual method):", domain_manual)