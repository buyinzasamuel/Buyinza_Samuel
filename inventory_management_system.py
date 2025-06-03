def display_inventory(inventory):
    print("\\nCurrent Inventory:")
    if not inventory:
        print("Inventory is empty.")
    else:
        for item, quantity in inventory.items():
            print(f"- {item}: {quantity}")
    print()

def update_inventory(inventory):
    while True:
        display_inventory(inventory)
        print("Options:")
        print("1. Add new item")
        print("2. Update existing item quantity")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            item = input("Enter the name of the new item to add: ").strip()
            if item in inventory:
                print(f"Item '{item}' already exists in inventory.")
            else:
                try:
                    qty = int(input(f"Enter the quantity of '{item}': ").strip())
                    if qty < 0:
                        print("Quantity cannot be negative.")
                    else:
                        inventory[item] = qty
                        print(f"Added '{item}' with quantity {qty}.")
                except ValueError:
                    print("Please enter a valid integer quantity.")
        elif choice == '2':
            item = input("Enter the name of the item to update: ").strip()
            if item not in inventory:
                print(f"Item '{item}' not found in inventory.")
            else:
                try:
                    qty = int(input(f"Enter the new quantity of '{item}': ").strip())
                    if qty < 0:
                        print("Quantity cannot be negative.")
                    else:
                        inventory[item] = qty
                        print(f"Updated '{item}' to quantity {qty}.")
                except ValueError:
                    print("Please enter a valid integer quantity.")
        elif choice == '3':
            print("Exiting inventory update.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def main():
    print("Welcome to the Inventory Management System!")
    inventory = {}

    while True:
        print("\\nMain Menu:")
        print("1. Display Inventory")
        print("2. Update Inventory")
        print("3. Exit")
        main_choice = input("Choose an option (1-3): ").strip()

        if main_choice == '1':
            display_inventory(inventory)
        elif main_choice == '2':
            update_inventory(inventory)
        elif main_choice == '3':
            print("Thank you for using the Inventory Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

