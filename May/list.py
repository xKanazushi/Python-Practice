def Score():

    score = []

    while True:
        point = input("Enter you score (Type done for end) : ").lower()
    
    
        if point == "done":
            break

        score.append(int(point))

    print(f"All Score   : {score}")
    print(f"Max Score     : {max(score)} ")
    print(f"Min Score     : {min(score)} ")
    print(f"Average Score : {sum(score)/len(score)}" )

Score()