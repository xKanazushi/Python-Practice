def dictionary_cont():

    print("====== PhoneNumber Book ======")
    print("1. Add PhoneNumber")
    print("2. Search PhoneNumber")
    print("3. View All")
    print("4. Exit")
    print("==============================")

    Users = {}

    while True:

        try:
            option = int(input("Choose : "))
        except ValueError:
            print("Error : Please Choose 1-4")
            continue

        if option not in [1,2,3,4]:
            print("Error : Please Choose 1-4")
            continue

        if option == 1:

            while True:
                username = input("Enter Name : ")

                if username == "":
                    print("Error : Please Enter Username")
                    continue
                else:
                    break

            while True:
                
                try:
                    phone = input("Enter Phone : ")
                    if not phone.isdigit():
                        print("Error : Please Enter PhoneNumber")
                    else:
                        break

                except ValueError:
                    print("Error : Please Enter PhoneNumber")
            
            print("Add Complete")
            print("==============================")
            Users[username] = phone 

        elif option == 2:

            while True:

                findusername = input("Search Name : ").lower()
                found = []
                for ConName in Users:
                    if findusername in ConName:
                        found.append(ConName)

                if found:
                    for name in found:
                        print(f"{name} : {Users[name]}")

                else:
                    print(f"Error : Don't Found {findusername}")
                    break

            print("==============================")

        elif option == 3:

            i = 0
            for username, phone in Users.items():
                i += 1
                print(f"{i} {username} : {phone}")
            
            # for i, (username, phone) in enumerate(Users.items()): ทำได้เหมือนกัน
            #     print(f"{i+1}. {username} : {phone}")

        elif option == 4:
            print("Bye!")
            break
            
dictionary_cont()