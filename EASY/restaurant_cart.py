from tabulate import tabulate

# Menu Items
items = [
    ['1 --> Pizza', 4.99],
    ['2 --> Pasta - Alfredo', 6.50],
    ['3 --> Beef Burger', 3.50],
    ['4 --> Coke - 1L', 1.99],
    ['5 --> Water - 1L', 2.99]
]
head = ['Item', 'Price']
menu = tabulate(items, headers = head, tablefmt = 'grid')

# Menu Mapping
item_mapping = {
    "1": ("Pizza", 4.99),
    "2": ("Pasta - Alfredo", 6.50),
    "3": ("Beef Burger", 3.50),
    "4": ("Coke - 1L", 1.99),
    "5": ("Water - 1L", 2.99)
} # Used dict to map the num to each items

# Cart
cart = []
total_price = 0.0

# User Inputs
print("Welcome to our Restaurant!")
print(menu)

# Order System
while True:
    choice = input("\nEnter the number corresponding to your desired food (or type 'q' to finish): ").strip()
    if choice.lower() == "q":
        break
    elif choice in item_mapping:
        item_name, item_price = item_mapping[choice]
        cart.append((item_name, item_price))
        total_price += item_price
        print(f"Added {item_name} to your cart. Current total: ${total_price:.2f}")
    else:
        print("Invalid choice. Please select a valid item number.")

# Display order summary
if cart != None:
    print("\nYour Cart:")
    cart_table = tabulate(cart, headers=["Item", "Price"], tablefmt="grid")
    print(cart_table)
    print(f"Total Price: ${total_price:.2f}")
else:
    print("\nYour cart is empty.")