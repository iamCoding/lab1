#!/user/bin/env python3
#Daniel Espitia
#Cuyamaca College CS-119
#Lab 1, exercise 2 , KmToMiles

#enter kilometers
kilometers = float(input("Enter Kilometers: "))

#conversion of Km to Miles
#1 km = 0.62 miles
conv = 0.62

#calculate miles
miles = kilometers * conv
print("%0.2fkilometers is equal to %0.2f miles "%(kilometers,miles))
