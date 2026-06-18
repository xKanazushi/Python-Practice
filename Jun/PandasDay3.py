import pandas as pd

watches = [
    {"user": "Aon",  "platform": "Netflix", "genre": "Action", "minutes": 120},
    {"user": "Beam", "platform": "Netflix", "genre": "Comedy", "minutes": 90},
    {"user": "Cher", "platform": "Disney+", "genre": "Action", "minutes": 110},
    {"user": "Dao",  "platform": "Disney+", "genre": "Family", "minutes": 100},
    {"user": "Eve",  "platform": "Netflix", "genre": "Action", "minutes": 130},
    {"user": "Fon",  "platform": "Disney+", "genre": "Action", "minutes": 95},
]

df = pd.DataFrame(watches)
by_pl_act = df.groupby(['platform','genre'])['minutes'].agg(average = "mean").round(2)
print(by_pl_act)

best_idx = by_pl_act['average'].idxmax()
best_mean = by_pl_act['average'][best_idx]
print(f"Best Platform : {best_idx[0]} - {best_idx[1]} (Average : {best_mean})")
