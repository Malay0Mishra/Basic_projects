import json





def load_data():
    with open("data.json", "r") as file:
        return json.load(file)
    
data = load_data()



def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)




def register_shop(): 
    name = input("Enter your Shop Name : ")
    if name in data:
        print(f"{name} is already registered")
        return None
    else:
        data[name] = {}
        print(f"{name} is registered successfully")
        save_data(data)
        return name 


def add_product():
    name = input("Enter your Shop Name to Verify :  ")
    if name in data:
        print(f"{name} is Shop Verified")
        product = input("Enter product name: ")
        price = int(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        if product in data[name]:
            print(f"{product} is already added")
        else:
            data[name][product] = {"price": price, "quantity": quantity}
            print(f"{product} is added successfully")
            save_data(data)
    else:
        print(f"{name} is not shop verified")



def view_products():
    if not data:
        print("No data available.")
        return

    print("\n===== ALL SHOPS AND PRODUCTS =====")
    for shop, products in data.items():
        print(f"\nShop: {shop}")
        if not products:
            print("  (No products added yet)")
        else:
            for product, details in products.items():
                print(f"  Product: {product}")
                print(f"    Price: {details['price']}")
                print(f"    Quantity: {details['quantity']}")