from Functions import *

while True:
    print("\n===== SIMPLE INVENTORY SYSTEM =====")
    print("1. Register Shop")
    print("2. Add Product")
    print("3. View Products")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register_shop()

    elif choice == "2":
        add_product()

    elif choice == "3":
        view_products()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")