celebs = ("Taylor Swift", "Lionel Messi", "The Weeknd")

new_celeb = input("Enter a celebrity to add: ")

celebs.append(new_celeb)   # This will cause an error

print(celebs) 




celebs = ("Taylor Swift", "Lionel Messi", "The Weeknd")

new_celeb = input("Enter a celebrity to add: ")

try:
    celebs.append(new_celeb)
except Exception as e:
    print("Attempted to append a value to a tuple.")
    print("Error message:", e)

print("Final tuple:", celebs)






celebs = ("Taylor Swift", "Lionel Messi", "The Weeknd")

new_celeb = input("Enter a celebrity to add: ")

try:
    celebs.append(new_celeb)
except Exception:
    celebs = celebs + (new_celeb,)   # Create new tuple

print("Updated tuple:", celebs)




celebs = ("Taylor Swift", "Lionel Messi", "The Weeknd")

new_celeb = input("Enter a celebrity to add: ")

celebs = (*celebs, new_celeb)

print("Updated tuple:", celebs)





celebs = ("Taylor Swift", "Lionel Messi", "The Weeknd")

new_celeb = input("Enter a celebrity to add: ")

celebs_list = list(celebs)   # Convert tuple to list
celebs_list.append(new_celeb)

celebs = tuple(celebs_list)  # Convert back to tuple

print("Updated tuple:", celebs)