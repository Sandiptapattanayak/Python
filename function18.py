#

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


temperature = float(input("Enter a temperature: "))
converted_fahrenheit = celsius_to_fahrenheit(temperature)
converted_celsius = fahrenheit_to_celsius(temperature)

print(f"{temperature} degrees Celsius is {converted_fahrenheit:.2f} degrees Fahrenheit.")
print(f"{temperature} degrees Fahrenheit is {converted_celsius:.2f} degrees Celsius.")
