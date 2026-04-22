import matplotlib.pyplot as plt

# a. Define x and y values
x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
x2 = [1, 2, 3, 4, 5]
y2 = [1, 3, 5, 7, 9]

# b & d. Line graph with two sets
plt.plot(x1, y1, label="Line 1")
plt.plot(x2, y2, label="Line 2")
plt.title("Simple Line Graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.grid(True)
plt.show()

# c. Scatter plot
plt.scatter(x1, y1, label="Scatter 1")
plt.scatter(x2, y2, label="Scatter 2")
plt.title("Simple Scatter Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.grid(True)
plt.show()