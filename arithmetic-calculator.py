# Initializing operator and numbers
operator = input("Enter your arithmatic operator (+ - * /): ")
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))

result = None

# Main logic
if operator == "+":
    result = n1 + n2
    print(f"Your answer is: {result}.")
elif operator == "-":
    result = n1 - n2
    print(f"Your answer is: {result}.")
elif operator == "*":
    result = n1 * n2
    print(f"Your answer is: {result}.")
elif operator == "/":
    result = n1 / n2
    print(f"Your answer is: {result}.")
else:
    print("Your operator is not valid!")
