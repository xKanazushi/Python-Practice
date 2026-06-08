import random
Ans = random.randint(1,100)
count = 0

while True: # loop untill true
    UserAns = int(input(f"Chose Number from 1-100 :"))
    print("------------------------")
    count += 1

    if UserAns == Ans:
        print(str(Ans)+" Congratulations Guess correctly in " + str(count) +" time")
        break
    elif UserAns > Ans:
        print(str(UserAns)+" That to much please try again")
    elif UserAns < Ans:
        print(str(UserAns)+" That to low please try again")
    print("------------------------")