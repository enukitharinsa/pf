total=0
i=1

while i<=10:
    mark=float(input("Enter mark"))
    total=total+mark
    i=i+1
    
avg=total/10

print("Total of marks=",total)
print("Average of marks=",avg)

if avg<50:
    print("Fail!")
else:
    print("Pass!")
