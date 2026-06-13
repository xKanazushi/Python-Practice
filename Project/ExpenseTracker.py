import os
import json

# ===============================================================
# เก็บ object ทั้งหมดไว้ในลิสต์นี้
# ===============================================================
transactions_list = []


class Transaction():
    def __init__(self, name, amount=0, trans_type=0):
        # self.xxx = ค่าที่เก็บไว้ "ใน" object นี้ (attribute)
        # ทุก object ที่สร้างจาก class นี้จะมี name/amount/type เป็นของตัวเอง
        self.name = name
        self.amount = amount
        self.type = trans_type

    def add_list(self):
        # เอา object ตัวเอง (self) ไปเก็บใน list กลาง แล้วบันทึกลงไฟล์ทันที
        transactions_list.append(self)
        save()
        print("Add Complete")
        print("=============================")

    def all_list(self):
        # income -> โชว์เครื่องหมาย "+", อย่างอื่น (expense) -> "-"
        sign = "+" if self.type == "income" else "-"
        print(f"{self.name} : {sign}{self.amount} ({self.type})")

    def remove_list(self):
        # วนหา transaction ที่ "ชื่อ" ตรงกับที่ผู้ใช้กรอก แล้วลบออกจากลิสต์
        for s in transactions_list:
            if s.name == self.name:
                transactions_list.remove(s)
                save()
                print("Remove Complete")
                print("=============================")
                return "found"

        print("Error : There is no item with that name yet")
        print("=============================")
        return "not found"


def total_summary(transactions):
    income = 0
    expense = 0
    for r in transactions:
        if r.type == "income":
            income += r.amount
        else:
            expense += r.amount

    print(f"Total income : {income}")
    print(f"Total expense : {expense}")
    print(f"Balance : {income - expense}")
    print("=============================")


def save():
    # แปลง object แต่ละตัวเป็น dict ด้วย __dict__
    # เช่น Transaction(name="Coffee", amount=50, type="expense")
    #      -> {"name": "Coffee", "amount": 50, "type": "expense"}
    # แล้วเอา list of dict นี้ไป json.dump ลงไฟล์ (object -> dict -> JSON)
    data = []
    for s in transactions_list:
        data.append(s.__dict__)
    with open("ExpenseTracker.json", "w") as f:
        json.dump(data, f)


# ===============================================================
# ตอนเปิดโปรแกรม: เช็คว่ามีไฟล์ JSON เก่าอยู่ไหม
# ถ้ามี -> โหลดข้อมูลกลับมาเป็น object (JSON -> dict -> object)
# ===============================================================
if os.path.exists("ExpenseTracker.json"):
    try:
        with open("ExpenseTracker.json", "r") as f:
            data = json.load(f)
        for d in data:
            transactions_list.append(Transaction(d['name'], d['amount'], d['type']))
    except json.JSONDecodeError:
        print("Warning: JSON file is empty or corrupted, starting fresh")
        transactions_list = []
else:
    transactions_list = []


print("====== Expense Tracker ======")
print("1. Add List")
print("2. View All list")
print("3. Total Summary")
print("4. Remove List")
print("5. Exit")
print("=============================")

while True:
    try:
        option = int(input("Choose : "))
        print("=============================")
    except ValueError:
        print("Error : Please enter a number and try again")
        print("=============================")
        continue  # กลับไปวนถามใหม่ทันที ไม่ต้องไหลลงไปเช็ค if ข้างล่าง

    # ----------------------------------------------------------
    # ถ้าผู้ใช้กรอกเลขที่ไม่ใช่ 1-5 (เช่น 0 หรือ 99) ให้เตือนแล้ว
    # "วนกลับไปถามใหม่เลย" ไม่ต้องไหลไปเช็คทุก if ข้างล่างให้เสียเวลา
    # ----------------------------------------------------------
    if option not in range(1, 6):
        print("Error : Please choose a number between 1-5")
        print("=============================")
        continue

    if option == 1:
        name_list = input("Name List : ")

        # วน loop จนกว่าจะได้ตัวเลขจริงๆ ค่อยออกจาก loop ด้วย break
        while True:
            try:
                amount_list = int(input("Amount (Baht) : "))  
                break
            except ValueError:
                print("Error : Please Enter Number")
                print("=============================")

        # วน loop จนกว่าจะได้ "income" หรือ "expense" เท่านั้น
        while True:
            trans_type = input("Type (income or expense) : ").lower()
            if trans_type in ["income", "expense"]:
                break
            else:
                print("Error : Please Enter income or expense")
                print("=============================")

        # สร้าง object ใหม่ แล้วเรียก method ของตัวเองเพื่อเก็บ + save ลงไฟล์
        new_transaction = Transaction(name_list, amount_list, trans_type)
        new_transaction.add_list()

    if option == 2:
        # enumerate ช่วยให้ได้ทั้ง index (i) และ object (view) ไปพร้อมกัน
        # i+1 เพราะอยากให้แสดงเลขลำดับเริ่มที่ 1 (อ่านง่ายสำหรับมนุษย์)
        for i, view in enumerate(transactions_list):
            print(f"{i+1}. ", end="")
            view.all_list()
        print("=============================")

    if option == 3:
        total_summary(transactions_list)

    if option == 4:
        while True:
            find_list = input("Enter Name : ")
            # สร้าง object เปล่าๆ ขึ้นมาแค่เพื่อ "ยืม" method remove_list มาใช้
            remove = Transaction(find_list)
            result = remove.remove_list()
            if result == "found":
                break

    if option == 5:
        print("Bye Bye")
        print("=============================")
        break