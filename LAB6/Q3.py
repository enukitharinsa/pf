total=0
count=0

price=float(input("Enter item price"))

while price!=0:
    total=total+price
    count=count+1

    price=float(input("Enter item price"))
    
if count>0:
    average=total/count
else:
    average=0


print("Total Bill Amount=",total)
print("Number of Items=",count)
print("Average price of Items=",average)
