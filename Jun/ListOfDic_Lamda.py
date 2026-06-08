students = []

def add_students(name, score):
    students.append({"name" : name, "score" : score})
    print("Add Complete")

def view_all_students():
    for i, s in enumerate(students):
        print(f"{i+1}. {s['name']} : {s['score']}")

def top_student():
    if not students:
            print("There are no students yet.")
            return
    top = max(students, key = lambda s: s["score"])
    print(f"Top Score is {top['name']} have {top['score']} point")


print("==== Students System ====")
print("1. Add Students")
print("2. View All Students")
print("3. Find Student Max Score")
print("4. Exit")
print("=========================")

while True:
    
    try:
        option = int(input("Choose : "))
    except ValueError:
        print("Error : Please enter the number (1-4)")
        continue

    if option not in range(1,5):
        print("Error : Please enter the number (1-4)")

    if option == 1:
        print("=========================")
        name = input("Enter Username : ")
        score = int(input("Enter Score : "))
        add_students(name, score)
        print("=========================")
        
    elif option == 2:
        print("=========================")
        view_all_students()
        print("=========================")

    elif option == 3:
        top_student()

    elif option == 4:
        print("Bye Bye")
        break