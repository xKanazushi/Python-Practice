


Stock = []

def add_product(name_add, price_add, amount_add):
    Stock.append({
        "name": name_add,
        "price": price_add,
        "amount": amount_add
    })
    print("Add Complete")   

def all_product():
    for i, s in enumerate(Stock):
        print(f"{i+1}. Product Name : {s['name']}, Price : {s['price']}, Amout : {s['amount']} ")
        print("====================================")

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

print("============= Stock ==============")
print("1. Add Product")
print("2. See All Product")
print("3. Find the most expensive Product")
print("4. Find the cheapest Product")
print("5. Exit")
print("====================================")

while True:
    try:
        option = int(input("Choose : "))
        print("====================================")
    except ValueError:
        print("Error : Please Enter Number (1-5)")
        print("====================================")
        continue

    if option not in range(1,6):
        print("Error : Please Enter Number (1-5)")
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
        print("Bye Bye jub jub")
        break
