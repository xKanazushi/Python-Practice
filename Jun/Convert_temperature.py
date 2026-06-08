def Celsius_to_Fahrenheit(temperature1):
            CeltoFah = (temperature1*(9/5)) + 32
            return CeltoFah

def Fahrenheit_to_Celsius(temperature2):
            FahtoCel = ((temperature2)-32) * 5/9
            return FahtoCel

def Celsius_to_Kelvin(temperature3):
            Celtokel = temperature3 + 273.15
            return Celtokel

while True:

    print("=== Change Temperature ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Exit")
    print("==========================")

    try:
        option = int(input("Choose : "))
    except ValueError:
        print("==========================")
        print("Error : Please Enter Number")
        print("==========================")
        continue

    if option not in range(1,5):
        print("==========================")
        print("Error : Please Enter (1-4)")
        print("==========================")

    if option == 1:
    
        while True:
            try:
                temperature1 = int(input("Enter Temperature (°C): "))
                break
            except ValueError:
                print("==========================")
                print("Error : Please Enter Number")
                print("==========================")

        print(f"{temperature1}°C = {Celsius_to_Fahrenheit(temperature1)}°F")

    elif option == 2:

        while True:
            try:
                temperature2 = int(input("Enter Temperature (°F) : "))
                break
            except ValueError:
                print("==========================")
                print("Error : Please Enter Number")
                print("==========================")
        
        print(f"{temperature2}°F = {Fahrenheit_to_Celsius(temperature2)}°C")

    elif option == 3:
    
        while True:
            try:
                temperature3 = int(input("Enter Temperature (°C): "))
                break
            except ValueError:
                print("==========================")
                print("Error : Please Enter Number")
                print("==========================")
        
        print(f"{temperature3}°C = {Celsius_to_Kelvin(temperature3)}K")

    elif option == 4:
        print("Bye Bye")
        break
