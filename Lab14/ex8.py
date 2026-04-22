# Heatmap of pickup vs dropoff community area
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # requires seaborn to be installed

# Read the CSV file
trips_df = pd.read_csv('../taxi trips Fri 7_7_2017.csv')

# Build a contingency table (counts) of pickup vs dropoff community areas
heat_data = pd.crosstab(
    trips_df['pickup_community_area'],
    trips_df['dropoff_community_area']
)

plt.figure(figsize=(10, 8))
sns.heatmap(heat_data, cmap="viridis")
plt.title("Heatmap of Pickup vs Dropoff Community Areas")
plt.xlabel("Dropoff community area")
plt.ylabel("Pickup community area")
plt.tight_layout()
plt.show()