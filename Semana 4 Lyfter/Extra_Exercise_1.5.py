# Exercise 5: Convert speed from km/h to m/s

# Input
speed_kmh = float(input("Enter a speed in km/h: "))

# Conversion
if speed_kmh >= 0:
    speed_ms = speed_kmh / 3.6
    print("The speed in m/s is:", speed_ms)
else:
    print("Error: speed cannot be negative")