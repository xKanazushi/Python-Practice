while True:
    try:
        weight = float(input("กรอกน้ำหนัก (kg.) : "))
        break
    except ValueError:
        print("กรุณากรอกข้อมูล")

while True:
    
    try:
        height = float(input("กรอกส่วนสูง (cm.) : "))
        break
    except ValueError:
        print("กรุณากรอกข้อมูล")

def calculate_bmi(weight,height):

    bmi = weight/((height/100)**2)

    def Bmi_level(bmi):

        if bmi < 18.5:
            return "ผอมเกินไป"
        elif bmi > 18.5 and bmi < 24.9:
            return "น้ำหนักปกติ"
        elif bmi > 25 and bmi < 29.9:
            return "น้ำหนักเกินเกณฑ์"
        else:   
            return "อ้วน"

    return Bmi_level(bmi),bmi

level , bmi = calculate_bmi(weight,height)
print(f"Bmi ของคุณ : {bmi:.2f}")
print(f"ระดับของคุณ : {level}")