# Open the file names.txt and read its contents and print the number of names
# append a new name at end of the file 
with open("names.txt") as file_object:
    contents_list = file_object.readlines()
    print(contents_list)
    print(f"Number of names: {len(contents_list)}") 
with open ("names.txt") as file_object:
    file_object.write("Lam, Sidney/n")