import pandas as pd

# orders = [
#     {"branch": "Siam", "item": "Latte", "price": 70, "qty": 3},
#     {"branch": "Siam", "item": "Espresso", "price": 60, "qty": 2},
#     {"branch": "Asoke", "item": "Latte", "price": 70, "qty": 5},
#     {"branch": "Asoke", "item": "Mocha", "price": 80, "qty": 4},
#     {"branch": "Thonglor", "item": "Latte", "price": 70, "qty": 1},
#     {"branch": "Thonglor", "item": "Espresso", "price": 60, "qty": 6},
# ]

# df = pd.DataFrame(orders)


# df['revenue'] = df['price'] * df['qty']
# branch_Rev = df.groupby('branch')['revenue'].sum()
# print("Revenue by branch :")
# print(branch_Rev)

# top_rev = branch_Rev.idxmax()
# top_branch = branch_Rev.loc[top_rev]
# print(f"Top branch : {top_rev} (revenue = {top_branch})")

# branch_cou = df.groupby('branch')['item'].count()
# print(branch_cou)


# print("=====================================================")


# for item in orders:
#     item['revenue'] = item['price'] * item['qty']

# branch_data = {}


# for item in orders:
#     bra = item['branch']
#     if bra not in branch_data:
#         branch_data[bra] = {"total" : 0, "count" : 0}
#     branch_data[bra]["total"] += item['revenue']
#     branch_data[bra]["count"] += 1

# print("Revenue by branch :")
# for branch, data in branch_data.items():
#     print(f"{branch} : {data['total']}")

# top_branch = max(branch_data, key = lambda bra:branch_data[bra]['total'])
# print(f"Top branch : {top_branch} (revenue = {branch_data[top_branch]['total']})")

# for branch, data in branch_data.items():
#     print(f"{branch} : {data['count']}")


# print("=====================================================")

members = [
    {"name": "Mint",  "plan": "Basic",   "branch": "Siam",     "visits": 5},
    {"name": "Got",   "plan": "Premium", "branch": "Siam",     "visits": 12},
    {"name": "Pim",   "plan": "Basic",   "branch": "Asoke",    "visits": 3},
    {"name": "Bank",  "plan": "Premium", "branch": "Asoke",    "visits": 8},
    {"name": "Fah",   "plan": "Basic",   "branch": "Siam",     "visits": 7},
    {"name": "Nan",   "plan": "Premium", "branch": "Thonglor", "visits": 15},
]

df = pd.DataFrame(members)
by_plan = df.groupby(["plan","branch"])["visits"].agg(count = "count", sum = "sum", mean = "mean").round(2)

result = by_plan.reset_index()
print(result)
# print(by_plan)

best_plan = by_plan['mean'].idxmax()
best_avg = by_plan['mean'].loc[best_plan]

print(f"Best plan (avg visits): {best_plan} (avg = {best_avg})")


# plan_data = {}

# for item in members:
#     pl = item['plan']
#     if pl not in plan_data:
#         plan_data[pl] = {'count' : 0, 'total_vis' : 0}
#     plan_data[pl]['count'] += 1
#     plan_data[pl]['total_vis'] += item['visits']
    

# print("Member count by plan :")
# for p, data in plan_data.items():
#     print(f"{p} : {data['count']}")

# print("Total visits by plan :")
# for p, data in plan_data.items():
#     print(f"{p} : {data['total_vis']}")

# print("Average visits by plan :")
# for p, data in plan_data.items():
#     data['average'] = data['total_vis'] / data['count']
#     print(f"{p} : {data['average']:.2f}")

# best_pl = max(plan_data, key = lambda pl: plan_data[pl]['average'])
# print(f"Best plan (avg visits): {best_pl} (avg = {plan_data[best_pl]['average']:.2f})")