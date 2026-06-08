fruits = ["แอปเปิ้ล","กล้วย","มะม่วง","ส้ม","องุ่น"]
n = 1

# for i in fruits:
#     print(f"ผลที่ {n}: {i}")
#     n += 1

for i, fruit in enumerate(fruits):
    print(f"ผลที่ {i+1}: {fruit}")