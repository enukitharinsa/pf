salary=float(input("Enter your salary"))

if salary>=100000:
    bonus=salary*0.15
elif salary>=50000:
    bonus=salary*0.1
else:
    bonus=salary*0.05
    
print("Bonus=",bonus)
