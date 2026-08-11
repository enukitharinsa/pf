sales=[]
day=1
while day<=7:
    sal=float(input(f"Enter sales {day} week"))
    sales.append(sal)
    day=day+1
print("sales of the week",sales)
