FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius =  (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {celsius}°C")
    return celsius
   
def convert_to_fahrenheit(celsius): 
    global CELSIUS_TO_FAHRENHEIT_FACTOR 
    fahrenheit = CELSIUS_TO_FAHRENHEIT_FACTOR + 32 * celsius
    print(f"{celsius}°C is {fahrenheit}°F")
    return  fahrenheit

measurement = float(input("Enter the temperature to convert:  "))
temperature = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if temperature == 'F':
    convert_to_celsius(measurement)   
elif temperature == 'C':
    convert_to_fahrenheit(measurement)   
else:
    print(f"Invalid temperature. Please enter a numeric value.")
