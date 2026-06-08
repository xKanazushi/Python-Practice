def Todo():

    todo = []

    while True:

        print("=============================")
        print("1.Add Note")
        print("2.See All More")
        print("3.Search Note")
        print("4.Delete Note")
        print("5.Exit")
        print("=============================")

        try:
            option = int(input("Choose : "))
        except ValueError:
            print("Please Type Number")
            continue

        if option not in [1,2,3,4,5]:
            print("Please Choose Number 1-4")
            continue

        if option == 1:
            User = input("Name Work : ")
            todo.append(User)
            print("Add Complete")
        
        elif option == 2:
            print(f"[{len(todo)}] {todo}")

        elif option == 3:
            keyword = input(f"Search : ")
            Found = []
            for note in todo:
                if keyword in note:
                    Found.append(note)
            
            if Found:
                print(f"Found : {Found}")
            else:
                print(f"Don't Found")
                    
        
        elif option == 4:
            User = input("Delete : ")
            if User in todo:
                todo.remove(User)
                print("Delete Complete")
            else:
                print("This Work was not found in list")

        elif option == 5:
            break
        
Todo()