FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)
temptature = int(input("Enter the temperature to convert:  "))
measurement = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
def convert_to_celsius(fahrenheit):
    return FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
   
def convert_to_fahrenheit(celsius):  
    return (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32

if measurement == 'F':
    print(f"{temptature}°F is {convert_to_celsius(temptature)}°C")
elif measurement == 'T':
    print(f"{temptature}°C is {convert_to_fahrenheit(temptature)}°F")
else:
    print(f"Invalid temperature. Please enter a numeric value.")