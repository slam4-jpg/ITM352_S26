# Open a text file and print its type
file_object = open("names.txt")

print(type(file_object))
file_object.close()


# Open a text file using with
with open("names.txt", "r") as file_object:
    print(type(file_object))