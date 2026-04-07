import csv

filename = "..\\taxi_1000.csv"
with open(filename) as csvfile:
    csv_reader = csv.reader(csvfile)
# Read the header row
headers = next(csv.reader)

# Find the index of relevant fields
fare_index = headers.index("Fare")
trip_miles_index = headers.index("Trip Miles")

# Initialize variables for calculations
total_fare = 0
max_trip_distance = 0
fare_count = 0

# Process the first 1,000 lines of data
for i, row in enumerate(csv_reader):
    if i >= 1000:
        break  # Stop after 1,000 rows
    
    try:
        fare = float(row[fare_index])
        trip_miles = float(row[trip_miles_index])

        if fare > 10:  # Only consider fares greater than $10
            total_fare += fare
            max_trip_distance = max(max_trip_distance, trip_miles)
            fare_count += 1
    except ValueError:
        # Handle missing or invalid values
        continue

# Calculate average fare
average_fare = total_fare / fare_count if fare_count else 0

# Print results
print(f"Total Fare (>$10): ${total_fare:,.2f}")
print(f"Average Fare (>$10): ${average_fare:,.2f}")
print(f"Maximum Trip Distance (>$10): {max_trip_distance:.2f} miles")