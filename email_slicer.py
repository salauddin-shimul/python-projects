# Email Slicer - It slices an email into username and domain

# User Input

email = input("Enter email: ")
if '@' in email:
    mid = email.index("@") # Finds the index of @ symbol

    user_name = email[:mid]
    domain = email[mid+1 : ]
    print(f"Username: {user_name} \nDomain: {domain}")
else:
    print("Invalid Email address!")