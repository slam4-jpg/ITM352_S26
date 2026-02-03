#manipulate a list in various ways
#Name: Sidney Lam
#Date: February 2, 2026

ResponseValues = [5, 7, 3, 8]
ResponseValues.append (0)
print("After appending 0:", ResponseValues)

# ResponseValues.insert(2, 6)
ResponseValues = ResponseValues[:2] + [6] + ResponseValues [2:]
print("After inserting 6 at index 2:", ResponseValues)  