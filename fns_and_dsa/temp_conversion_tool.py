FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    print(f"{fahrenheit}°F is {celsius}°C")
    return celsius
   
def convert_to_fahrenheit(celsius): 
    global CELSIUS_TO_FAHRENHEIT_FACTOR 
    fahrenheit = CELSIUS_TO_FAHRENHEIT_FACTOR + 32 * celsius
    print(f"{celsius}°C is {fahrenheit}°F")
    return  fahrenheit

temperature = float(input("Enter the temperature to convert:  "))
measurement = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if measurement == 'F':
    convert_to_celsius(temperature)   
elif measurement == 'C':
    convert_to_fahrenheit(temperature)   
else:
    print(f"Invalid temperature. Please enter a numeric value.")
