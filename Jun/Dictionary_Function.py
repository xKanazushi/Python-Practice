def Dictionary_Function():
    
    print("====== Store ======")
    print("1. View Product")
    print("2. Add to Bucket")
    print("3. View Bucket")
    print("4. Purchase")
    print("5. Exit")
    print("===================")

    shop = {
        "น้ำ" : 10,
        "ขนม" : 25,
        "กาแฟ" : 40,
        "ข้าว" : 55
    }

    Bucket = []
    total = 0

    while True:

        try:
            option = int(input("Choose : "))
        except ValueError:
            print("Error : Please Enter 1-4 in place")
            continue

        if option not in range(1,6):
            print("Error : Please Enter 1-4 in place")
            continue

        if option == 1:

            print("\n===== Product =====")
            for i, (name,price) in enumerate(shop.items()):
                print(f"{i+1}. {name} : {price} Bath")
            print("=====================")

        elif option == 2:

            User_add = input("Add Product : ")

            if User_add in shop:
                Bucket.append(User_add)
                print(f"Add '{User_add}' Complete")
            else:
                print("Sorry : The Product don't have in this store")

            print("=====================")

        elif option == 3:

            print("====== Bucket ======")
            for i, name in enumerate(Bucket):
                price = shop[name]
                total += price
                print(f"{i+1}. {name} : {price} Bath")
            print(f"รวม : {total} Bath")
            print("=====================")

        
        elif option == 4:

            while True:
                print(f"รวมทั้งหมด : {total} Bath")

                try:
                    User_pay = int(input("กรอกเงิน : "))
                except ValueError:
                    print("โปรดกรอกจำนวนเงิน")

                if User_pay < total:
                    print("ยอดชำระไม่เพียงพอ")
                else:
                    print(f"เงินทอน : {User_pay-total} บาท")
                    print("ขอบคุณครับ/ค่ะ")
                    break
            break

        elif option == 5:
            print("Bye Bye")
            break     

Dictionary_Function()