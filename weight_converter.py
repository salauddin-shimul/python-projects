# Weight Converter

conversion_factor = 2.205

# User Input
weight = float(input("Enter your weight: "))
unit = input("Unit of weight (K - Kilograms or L - Pounds): ")

# Main Logic
if unit == "K":
    weight = weight * conversion_factor
    print(f"Your weight in Pounds is {round(weight, 3)} Lbs.")
elif unit == "L":
    weight = weight / conversion_factor
    print(f"Your weight in Kilograms is {round(weight, 3)} KG.")
else:
    print("You have entered invalid unit!")