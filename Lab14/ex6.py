# Scatter plot of fares by trip miles with filters and saved image
import pandas as pd
import matplotlib.pyplot as plt

trips_df = pd.read_json('../Trips from area 8.json')

# Filter out trips of 0 miles
trips_df = trips_df[trips_df.trip_miles > 0]

# Filter out trips less than 2 miles
trips_df = trips_df[trips_df.trip_miles >= 2]

fare_series = trips_df.fare
miles_series = trips_df.trip_miles

plt.figure()
plt.plot(fare_series, miles_series, linestyle="none", marker=".")
plt.title("Trip Miles (>= 2) by Fare")
plt.xlabel("Fare, in $")
plt.ylabel("Trip miles")
# Save the plot to a file
plt.savefig("FaresXmiles.png")
plt.show()