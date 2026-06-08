import random

def Dice():

    while True:

        print("==================================")
        print("Dice Roller")
        num_dice = int(input("How Many Dice Roll (1-5) : "))
        print("==================================")

        result = []

        if num_dice not in [1,2,3,4,5]:
            print("Error : Please Choose Number 1-5")
            continue

        for i in range(num_dice):
            result.append(random.randint(1,6))
            print(f"ลูกที่ {i+1} : {result[i]}")

        print("==================================")

        print(f"Total : {sum(result)}")
        option = input("Try Again (y/n) : ").lower()

        if option == "y":
            continue
        else:
            break

Dice()