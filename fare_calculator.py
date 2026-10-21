# Travel Fare Calculator
FARE_RATE = 14

namenotentered = True
while namenotentered == True:
    name = input("Enter passenger name: ")
    if name != "":
        namenotentered = False
    else:
        print("Your name cannot be empty! Please enter a valid name.")

distancenotentered = True
while distancenotentered == True:
    distance = float(input("Enter distance (km): "))
    if distance > 0:
        distancenotentered = False
    else:
        print("You cannot travel 0 km! Please enter a valid distance.")

passengersnotentered = True
while passengersnotentered == True:
    passengers = int(input("Enter number of passengers: "))
    if passengers >= 1:
        passengersnotentered = False
    else:
        print("Zero or negative passengers cannot travel! PLease enter a valid amount of passengers.")
        
total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))

# Validation rules
# 1. Passenger name -- Must not be empty
# 2. Distance -- Number greater than 0
# 3. Passengers -- Positive whole number
