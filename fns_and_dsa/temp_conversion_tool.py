FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    print(f"{temperature}°F is {celsius}°C")
    return celsius
   
def convert_to_fahrenheit(celsius):  

    fahrenheit = (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32

    print(f"{temperature}°C is {fahrenheit}°F")
    return  fahrenheit

temperature = float(input("Enter the temperature to convert:  "))
measurement = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if measurement == 'F':
    convert_to_celsius(temperature)   
elif measurement == 'C':
    convert_to_fahrenheit(temperature)   
else:
    print(f"Invalid unit.")
