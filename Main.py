import json

with open("data.json", "r") as file:
    data = json.load(file)

def load_data():
    return data.json 

def save_data(data):
    return data.json 

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