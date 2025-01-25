# Temperature Converter

# User Input
temp = float(input("Enter your temperature: "))
unit = input("Enter your unit (C -> Celsius, F -> Fahrenheit): ")

result = None

# Main logic
if unit == 'C':
    result = (temp * 9)/5 + 32
    print(f"Your temperature in fahrenheit is {round(result, 3)} F.")
elif unit == 'F':
    result = ((temp - 32) * 5) / 9
    print(f"Your temperature in celsius is {round(result, 3)} C.")
else:
    print("Invalid unit")