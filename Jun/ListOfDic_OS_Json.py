import json
import os

if os.path.exists("stock.json"): # ใช้ os ผ่าน path ว่ามีไฟล์ stock.json มั้ย
    with open("stock.json", "r") as f: # อ่านไฟล์
        Stock = json.load(f) # เอาเข้า list stock

else:
    Stock = [] # สร้าง list

def save():
    with open("stock.json", "w") as f: 
        json.dump(Stock, f) # แค่เปิดไฟล์แล้วทับ save เดิม

def add_product(name_add, price_add, amount_add):
    Stock.append({
        "name": name_add,
        "price": price_add,
        "amount": amount_add
    })
    save()
    print("Add Complete")   

def all_product():
    if not  Stock:
        print("There are not Product yet")
        return
    for i, s in enumerate(Stock):
        print(f"{i+1}. Product Name : {s['name']}, Price : {s['price']}, Amout : {s['amount']} ")

def most_price():
    if not Stock:
        print("There are no Product yet.")
        return
    most = max(Stock, key = lambda s: s["price"])
    print(f"Most Expensive is {most['name']} Price {most['price']}")
    print("====================================")

def lower_pric():
    if not Stock:
        print("There are not Product yet")
        print("====================================")
        return
    lower = min(Stock, key = lambda s: s["price"])
    print(f"Cheapest Product is {lower['name']} Price {lower['price']}")
    print("====================================")

def edit_product(product_edit, new_price):
    for s in Stock:
        if s['name'] == product_edit:
            s['price'] = new_price
            print("Edit Complete")
            save()
            return
    print("There are not Product yet")

def remove_product(product_remove):
    for s in Stock:
        if s['name'] == product_remove:
            Stock.remove(s)
            print("Remove Complete")
            save()
            return
    print("There are not Product yet. Please Check and Try again")

print("============= Stock ==============")
print("1. Add Product")
print("2. See All Product")
print("3. Find the most expensive Product")
print("4. Find the cheapest Product")
print("5. Edit Product")
print("6. Remove Product")
print("7. Exit")
print("====================================")

while True:
    try:
        option = int(input("Choose : "))
        print("====================================")
    except ValueError:
        print("Error : Please Enter Number (1-7)")
        print("====================================")
        continue

    if option not in range(1,8):
        print("Error : Please Enter Number (1-7)")
        print("====================================")
        continue
    
    if option == 1:
        name_add = input("Add Product Name : ")
        while True:
            try:
                price_add = int(input("Product Price : "))
                break
            except ValueError:
                print("Error : Please Enter Number of Price")
        while True:
            try:
                amount_add = int(input("Added Amout : "))
                break
            except ValueError:
                print("Error :  Please Enter Number of Amount")
        add_product(name_add, price_add, amount_add)
        print("====================================")
    
    elif option == 2:
        all_product()

    elif option == 3:
        most_price()

    elif option == 4:
        lower_pric()

    elif option == 5:
        product_edit = input("Product Name to Edit : ")
        while True:
            try:
                new_price = int(input("New Price : "))
                break
            except ValueError:
                print("Error : Please Enter Number")
        edit_product(product_edit, new_price)

    elif option == 6:
        product_remove = input("Product Name  to Remove: ")
        remove_product(product_remove)

    elif option == 7:
        print("Bye Bye jub jub")
        break
