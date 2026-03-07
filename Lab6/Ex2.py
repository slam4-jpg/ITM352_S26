# List with 5 elements
values = [1,2,3,4,5]

#check if list has fewer than 5 elements 
if len(values) < 5:
    print("List has fewer than 5 elements.")
# check if list has between 5 and 10 elements
elif len(values) >= 5 and len(values) <= 10:
    print("List has between 5 and 10 elements.")
# check if list has more than 10 elements
else:
    print("List has more than 10 elements.")    

#List of varying lengths 
test_cases=[[], [1], [1,2,3,4,5], [1,2,3,4,5,6,7,8,9,10], [1] *15]
def check_list_size(lst):
#returns a message based on the length of the list
    size= len(lst)
    if size < 5:
        return "List has fewer than 5 elements."
    elif size >= 5 and size <= 10:
        return "List has between 5 and 10 elements."
    else:
        return "List has more than 10 elements."
    
    for test in test_cases:
        result=check_list_size(test)
        print(f"List: {test} - {result}")   