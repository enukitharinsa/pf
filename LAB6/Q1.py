total=0
i=1

while i<=5:
    units=int(input("Enter units"))

    if units<=100:
        bill=units*10
    elif units<=200:
        bill=(100*10)+((units-100)*15)
    else:
        bill=(100*10)+(100*15)+((units-200)*20)

    print("Bill amount=Rs.",bill)

    total=total+bill
    i=i+1

print("Total amount colectes=Rs.",total)
    
