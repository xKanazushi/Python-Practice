def Todo():

    todo = []

    while True:

        print("=============================")
        print("1.Add")
        print("2.See more")
        print("3.Delete")
        print("4.Exit")
        print("=============================")

        try:
            option = int(input("Choose : "))
        except ValueError:
            print("Please Type Number")
            continue

        if option not in [1,2,3,4]:
            print("Please Choose Number 1-4")
            continue

        if option == 1:
            User = input("Name Work : ")
            todo.append(User)
            print("Add Complete")
        
        elif option == 2:
            print(f"[{len(todo)}] {todo}")

        elif option == 3:
            User = input("Delete : ")
            if User in todo:
                todo.remove(User)
                print("Delete Complete")
            else:
                print("This Work was not found in list")

        elif option == 4:
            break
        
Todo()