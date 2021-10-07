#!/user/bin/env python3
#Daniel Espitia
#Cuyamaca College CS-119
#Lab 1, exercise 3 , MilesToKm

#enter miles
miles = float(input("Enter miles: "))

#conversion of Miles to Km 
# 0.62 miles = 1km
conv = 0.62

#calculate kilometers
kilometers = miles * conv
print("%0.2f miles is equal to %0.2f kilometers "%(miles,kilometers))
