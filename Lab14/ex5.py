import matplotlib.pyplot as plt
import pandas as pd
import json

with open("Trips from area 8.json") as f:
    data = pd.DataFrame(json.load(f))

fare_miles = data[['fare', 'trip_miles']].dropna()

# a. Basic scatter
plt.scatter(fare_miles['fare'], fare_miles['trip_miles'], alpha=0.5)
plt.title('Scatter: Fare vs. Trip Miles')
plt.xlabel('Fare')
plt.ylabel('Trip Miles')
plt.grid(True)
plt.show()

# b. Using plt.plot
plt.plot(fare_miles['fare'], fare_miles['trip_miles'], linestyle='none', marker='.')
plt.title('Plot: Fare vs. Trip Miles')
plt.xlabel('Fare')
plt.ylabel('Trip Miles')
plt.grid(True)
plt.show()

# c. Fancy version
plt.plot(fare_miles['fare'], fare_miles['trip_miles'], linestyle='none', marker='v', color='cyan', alpha=0.2)
plt.title('Fancy Plot: Fare vs. Trip Miles')
plt.xlabel('Fare')
plt.ylabel('Trip Miles')
plt.grid(True)
plt.show()