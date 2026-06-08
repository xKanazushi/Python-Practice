def Exercise_adjust():

    students = {}

    while True:

        name = input("Enter Username : ").lower()

        if name == "":
            continue  

        if name == "done":
            break

        score = int(input("Enter Score : "))

        students[name] = score

        if score < 0 or score > 100:
            print("Error : Please Check Score and try again")
            continue

    print("====== Score Resut =====")

    for name, score in students.items():

        if score >= 50:
            print(f"{name} : {score} Point Pass")

        else:
            print(f"{name} : {score} Point fail")

Exercise_adjust()