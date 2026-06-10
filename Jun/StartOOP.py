class Product:
    def __init__(self, name, price, amount): # Set product detail --> Add Attribute in class Product
        self.productname = name
        self.productprice = price
        self.productamount = amount

    def add_product(self):                   # Add function --> Add method in class Product
        Stock.append(self)
        print("Add Complete")
        print("============================")

    def display(self):                       # display function --> Method
        print(f"Name : {self.productname}, Price : {self.productprice}, Amount : {self.productamount}")

    def edit_product(self):                 # edit function --> method
        for s in Stock:
            if s.productname == self.productname:
                s.productprice = self.productprice
                s.productamount = self.productamount
                print("Edit Complete")
                return
        print("There are not Product Yet")


print("========== Stock ===========")       # interface
print("1. Add Product")
print("2. View All")
print("3. Edit Product")
print("4. Exit")
print("============================")

Stock = []                                  # list

while True:                                 
    try:
        option = int(input("Choose : "))
        print("============================")
    except ValueError:
        print("Error : Plese Enter Number")
        print("============================")
        continue
    if option not in range(1,5):
        print("Error : Plese Enter Number")
        print("============================")
        continue

    if option == 1:
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
        print("Bye Bye Jub Jub <3333")
        break