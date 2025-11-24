# Program to convert temperature from Celsius to Fahrenheit and Kelvin

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

kelvin = celsius + 273.15

print("Temperature in Celsius:", celsius)
print("Temperature in Fahrenheit:", fahrenheit)
print("Temperature in Kelvin:", kelvin)