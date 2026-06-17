import json

with open("data.json", "r") as file:
    data = json.load(file)



def load_data():
    with open("data.json", "r") as file:
        return json.load(file)



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