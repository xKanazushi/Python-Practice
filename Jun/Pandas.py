import pandas as pd

scores = [
    {"student": "Alice", "subject": "Math", "score": 85},
    {"student": "Bob", "subject": "Math", "score": 90},
    {"student": "Alice", "subject": "Science", "score": 78},
    {"student": "Bob", "subject": "Science", "score": 88},
    {"student": "Charlie", "subject": "Math", "score": 72},
    {"student": "Charlie", "subject": "Science", "score": 95},
]

# ========================================================================
# pd.dataFrame() คือการสร้างตารางข้อมูล ในที่เราให้ df เป็นตัวแปรเก็บตารางข้อมูล scores
# ========================================================================

df = pd.DataFrame(scores)

# ========================================================================
# groupby() คือการที่เราจะจับกลุ่มอะไร แล้วเราสนใจอะไร
# df.groupby("จับกลุ่มอะไร")["สนใจอะไร"]
# .agg คือการทำหลายอย่างรวมกัน ถ้าทำอย่าางเดียวเราใช้ 
# df.groupby("จับกลุ่มอะไร")["สนใจอะไร"].สิ่งที่เราจะทำเช่น .sum() วงเล็บคือการเรียกใช้
# .round(2) ปัดทศนิยม 2 ตำแหน่ง
# ========================================================================

summary = df.groupby("subject")["score"].agg(total = "sum",count = "count",average = "mean").round(2)
print(summary)

# ========================================================================
# summary['average'] มันคือการเข้าถึง average ของ summary 
# .idxmax มันคือการหาที่ index ไหนมีค่ามากสุด [จากสิงที่เราสนใจ] และมันจะคืนค่าสิ่งที่เราสนใจออกมา
#  summary.loc[best_sub, "average"] มันคือการ locate อะไร แล้วเราดึงข้อมูลอะไรจากที่เรา locate เจอ
# ========================================================================

best_sub = summary['average'].idxmax()
best_avg = summary.loc[best_sub, "average"]
print(f"Best Subject : {best_sub} (Average : {best_avg})")



print("=====================================================")

# ========================================================================
# สร้าง dictionary ที่ใช้เก็บข้อมูลรายวิชา
# ========================================================================

subject_data = {}

# ========================================================================
# ใช้ for loop ใน dictionary scores ใช้ item ในการ loop
# ให้ sub คือค่าของ subject ใน scores
# ถ้า sub ไม่มีใน subject_data เราจะสร้างข้อมูลใน 
# Dictionary subject_data โดยให้ value total and count = 0 ก่อน มันอยู่ใน sub -> subject_data[sub]
# subject_data[sub]['total'] += item['score'] ให้ total มันบวกสะสมตาม score ใน scores
# subject_data[sub]['count'] += 1 ให้ count มันบวกสะสม 1
# ========================================================================

for item in scores:
    sub = item['subject']
    if sub not in subject_data:
        subject_data[sub] = {"total" : 0, "count" : 0}
    subject_data[sub]['total'] += item['score']
    subject_data[sub]['count'] += 1

# ========================================================================
# ใช้ for loop ใน subject_data.items() ใช้ sub, data ในการ loop 
# .item() คือการเข้าถึงข้อมูลทั้ง key และ value
# สร้าง data["average"] มี value = data['total'] / data['count']
# ทำไมเราใช้ sub แทนตรงส่วนที่ใช้ data ไม่ได้นั้นเพราะว่าในที่นี้มันเป็น dic ซ้อน dic sub มัน 
# loop dic ส่วนนอกก็คือ ชื่อวิชา แล้ว value ของมันคือ dic key total and count และเราใช้ data 
# ในการ loop ส่วนนั้นต่อ
# ========================================================================

for sub, data in subject_data.items():
    data["average"] = data['total'] / data['count']
    print(f"{sub} : {data['total']}, Average : {data['average']:.2f} ")

# ========================================================================
# เราหาค่าสูงสุดใน subject_data โดยใช้ lambda ในการแสดงผลข้อมูลอิงตามอะไร
# ในที่นี้ให้ แสดง sub ตาม average
# ========================================================================

best_sub = max(subject_data, key = lambda sub: subject_data[sub]['average'])
print(f"Best Subject : {best_sub} (Average : {subject_data[best_sub]['average']})")