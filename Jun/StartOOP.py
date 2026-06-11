import json
import os

Stock = []

class Product:
    def __init__(self, name, price = 0, amount = 0): # Set product detail --> Add Attribute in class Product
        self.name = name
        self.price = price
        self.amount = amount

    def add_product(self):                   # Add function --> Add method in class Product
        Stock.append(self)
        save()
        print("Add Complete")
        print("============================")

    def display(self):                       # display function --> Method
        print(f"Name : {self.name}, Price : {self.price}, Amount : {self.amount}")

    def edit_product(self):                 # edit function --> method
        for s in Stock:
            if s.name == self.name:
                s.price = self.price
                s.amount = self.amount
                save()
                print("Edit Complete")
                print("============================")
                return
        print("There are not Product yet")
        print("============================")

    def remove_product(self):
        for s in Stock:
            if s.name == self.name:
                Stock.remove(s)
                save()
                print("Delete Complete")
                print("============================")
                return "found"
        print("There are not Product yet")
        return "notfound"

def save():
    data = []
    for s in Stock:
        data.append(s.__dict__)
    with open("OOP_Stock.json", "w") as f:
        json.dump(data,f)

if os.path.exists("OOP_Stock.json"):
    with open("OOP_Stock.json", "r") as f:
        data = json.load(f)
    for d in data:
        Stock.append(Product(d["name"], d["price"], d["amount"]))
else:
    Stock = []

print("========== Stock ===========")       # interface
print("1. Add Product")
print("2. View All")
print("3. Edit Product")
print("4. Remove Product")
print("5. Exit")
print("============================")

while True:                                 
    try:
        option = int(input("Choose : "))
    except ValueError:
        print("Error : Plese Enter Number")
        print("============================")
        continue
    if option not in range(1,6):
        print("Error : Plese Enter Number")
        print("============================")
        continue

    if option == 1:
        print("============================")
        name = input("Product Name : ")
        while True:
            try:
                price = int(input("Price : "))
                break
            except ValueError:
                print("Error : Please Enter Price in Number")
                continue
        while True:
            try:
                amont = int(input("Total Amount : "))
                break
            except ValueError:
                print("Error : Please Enter Amount in Number")
                continue
        print("============================")

        added = Product(name, price, amont)         # create Data to Product
        added.add_product()                         # use method in added data

    if option == 2:
        print("========== Stock ==========")
        for i, p in enumerate(Stock):               # i = order in loop, p variable for use method
            print(f"{i+1}. ", end = "")
            p.display()
        print("===========================")
        
    if option == 3:
        print("========== Edit ==========")
        find_product = input("Find Product : ")
        while True:
            try:
                edit_price = int(input("Edit Price : "))
                break
            except ValueError:
                print("Error : Please Enter Price in Number")
                continue
        while True:
            try:
                edit_amount = int(input("Edit Amount : "))
                break
            except ValueError:
                print("Error : Please Enter Amount in Number")
                continue

        edit = Product(find_product, edit_price, edit_amount)   # create Data to Product
        edit.edit_product()                                     # use method in edit data

    if option == 4:
        print("========= Remove =========")
        while True:
            findtoRemove = input("Product Remove : ")
            remove = Product(findtoRemove)
            result = remove.remove_product()
            if result == "found":
                break

    if option == 5:
        print("Bye Bye Jub Jub <3333")
        break