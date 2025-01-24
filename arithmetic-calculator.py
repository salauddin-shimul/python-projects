# Initializing operator and numbers
operator = input("Enter your arithmatic operator (+ - * /): ")
n1 = float(input("Enter 1st number: "))
n2 = float(input("Enter 2nd number: "))

result = None

# Main logic
if operator == "+":
    result = n1 + n2
    print(f"Your answer is: {round(result, 3)}.")
elif operator == "-":
    result = n1 - n2
    print(f"Your answer is: {round(result, 3)}.")
elif operator == "*":
    result = n1 * n2
    print(f"Your answer is: {round(result, 3)}.")
elif operator == "/":
    result = n1 / n2
    print(f"Your answer is: {round(result, 3)}.")
else:
    print("Your operator is not valid!")
