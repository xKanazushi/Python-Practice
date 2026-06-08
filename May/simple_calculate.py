def calculator():
    print("=============================")
    print("      Simple Calculator      ")
    print("=============================")

while True:
    first = int(input("Enter first Number : "))
    second = int(input("Enter second Number : "))
    calmethod = input("Choose Method (+,-,*,/) : ")

    if calmethod == "+":
        Ans = first + second
    elif calmethod == "-":
        Ans = first - second
    elif calmethod == "*":
        Ans = first * second
    elif calmethod == "/":
        if second == 0:
            print("Error : Can't devide by zero")
            continue
        Ans = first / second

    else:
        print(" Invalid method! Use +,-,*,/ only")
    print(f"{first} {calmethod} {second} = {Ans}")

    endloop = input("Calculate again ? (y/n) : ").lower()
    print("=============================")

    if endloop == "n":
        print("You're Welcome")
        print("=============================")
        break
    
calculator()