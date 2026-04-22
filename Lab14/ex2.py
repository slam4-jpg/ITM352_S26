import matplotlib.pyplot as plt
import pandas as pd
import json

with open("Trips from area 8.json") as f:
    data = pd.DataFrame(json.load(f))

trip_miles = data['trip_miles'].dropna()
plt.hist(trip_miles, bins=30, edgecolor='black')
plt.title('Histogram of Trip Miles')
plt.xlabel('Trip Miles')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()