# name = input("กรอกชื่อ: ")
# age = input("กรอกอายุ: ")
# height = input("กรอกส่วนสูง: ")
# print(f"ชื่อ: {name}")
# print(f"อายุ: {age} ปี")
# print(f"ส่วนสูง: {height} cm")


# # =====================================================================================



# fruits = ["แอปเปิ้ล","กล้วย","มะม่วง","ส้ม","องุ่น"]
# n = 1

# # for i in fruits:
# #     print(f"ผลที่ {n}: {i}")
# #     n += 1

# for i, fruit in enumerate(fruits):
#     print(f"ผลที่ {i+1}: {fruit}")


# # =====================================================================================


# import random
# Ans = random.randint(1,100)
# count = 0

# while True: # loop untill true
#     UserAns = int(input(f"Chose Number from 1-100 :"))
#     print("------------------------")
#     count += 1

#     if UserAns == Ans:
#         print(str(Ans)+" Congratulations Guess correctly in " + str(count) +" time")
#         break
#     elif UserAns > Ans:
#         print(str(UserAns)+" That to much please try again")
#     elif UserAns < Ans:
#         print(str(UserAns)+" That to low please try again")
#     print("------------------------")


# # =====================================================================================


# def calculator():
#     print("=============================")
#     print("      Simple Calculator      ")
#     print("=============================")

# while True:
#     first = int(input("Enter first Number : "))
#     second = int(input("Enter second Number : "))
#     calmethod = input("Choose Method (+,-,*,/) : ")

#     if calmethod == "+":
#         Ans = first + second
#     elif calmethod == "-":
#         Ans = first - second
#     elif calmethod == "*":
#         Ans = first * second
#     elif calmethod == "/":
#         if second == 0:
#             print("Error : Can't devide by zero")
#             continue
#         Ans = first / second

#     else:
#         print(" Invalid method! Use +,-,*,/ only")
#     print(f"{first} {calmethod} {second} = {Ans}")

#     endloop = input("Calculate again ? (y/n) : ").lower()
#     print("=============================")

#     if endloop == "n":
#         print("You're Welcome")
#         print("=============================")
#         break
    
# calculator()



# # =====================================================================================



# def Score():

#     score = []

#     while True:
#         point = input("Enter you score (Type done for end) : ").lower()
    
    
#         if point == "done":
#             break

#         score.append(int(point))

#     print(f"All Score   : {score}")
#     print(f"Max Score     : {max(score)} ")
#     print(f"Min Score     : {min(score)} ")
#     print(f"Average Score : {sum(score)/len(score)}" )

# Score()


# # =====================================================================================


# def Todo():

#     todo = []

#     while True:

#         print("=============================")
#         print("1.Add")
#         print("2.See more")
#         print("3.Delete")
#         print("4.Exit")
#         print("=============================")

#         try:
#             option = int(input("Choose : "))
#         except ValueError:
#             print("Please Type Number")
#             continue

#         if option not in [1,2,3,4]:
#             print("Please Choose Number 1-4")
#             continue

#         if option == 1:
#             User = input("Name Work : ")
#             todo.append(User)
#             print("Add Complete")
        
#         elif option == 2:
#             print(f"[{len(todo)}] {todo}")

#         elif option == 3:
#             User = input("Delete : ")
#             if User in todo:
#                 todo.remove(User)
#                 print("Delete Complete")
#             else:
#                 print("This Work was not found in list")

#         elif option == 4:
#             break
        
# Todo()


# # =====================================================================================


# def Todo():

#     todo = []

#     while True:

#         print("=============================")
#         print("1.Add Note")
#         print("2.See All More")
#         print("3.Search Note")
#         print("4.Delete Note")
#         print("5.Exit")
#         print("=============================")

#         try:
#             option = int(input("Choose : "))
#         except ValueError:
#             print("Please Type Number")
#             continue

#         if option not in [1,2,3,4,5]:
#             print("Please Choose Number 1-4")
#             continue

#         if option == 1:
#             User = input("Name Work : ")
#             todo.append(User)
#             print("Add Complete")
        
#         elif option == 2:
#             print(f"[{len(todo)}] {todo}")

#         elif option == 3:
#             keyword = input(f"Search : ")
#             Found = []
#             for note in todo:
#                 if keyword in note:
#                     Found.append(note)
            
#             if Found:
#                 print(f"Found : {Found}")
#             else:
#                 print(f"Don't Found")
                    
        
#         elif option == 4:
#             User = input("Delete : ")
#             if User in todo:
#                 todo.remove(User)
#                 print("Delete Complete")
#             else:
#                 print("This Work was not found in list")

#         elif option == 5:
#             break
        
# Todo()


# # =====================================================================================


# import random

# def Dice():

#     while True:

#         print("==================================")
#         print("Dice Roller")
#         num_dice = int(input("How Many Dice Roll (1-5) : "))
#         print("==================================")

#         result = []

#         if num_dice not in [1,2,3,4,5]:
#             print("Error : Please Choose Number 1-5")
#             continue

#         for i in range(num_dice):
#             result.append(random.randint(1,6))
#             print(f"ลูกที่ {i+1} : {result[i]}")

#         print("==================================")

#         print(f"Total : {sum(result)}")
#         option = input("Try Again (y/n) : ").lower()

#         if option == "y":
#             continue
#         else:
#             break

# Dice()