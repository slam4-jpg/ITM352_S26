trip_durations = [1.1,0.8,2.5,2,6]
trip_fares= (6.25,5.25,10.50,8.05)

trips =dict(zip(trip_durations,trip_fares))
print(trips)




#Trips= dict(zip(trip_durations,trip_fares))
#print("\nTrips Dictionary")
#print(Trips)



trip_num= input("what trip do you want? (1-4):")
trip_index=int(trip_num)-1
#print(f"Duration: {list(trips.keys())[trip_index]} miles")
#print(f"Fare: ${list(trips.values())[trip_index]:.2f}")
