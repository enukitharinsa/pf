customer=0
amount=0

while True:
    units=int(input("Enter wanter units used(-1 to stop)"))

    if units==-1:
        break

    if units<=50:
        bill=units*20
        
    elif units<=100:
        bill=(50*20)+((units-50)*30)

    else:
        bill=(50*20)+(50*30)+((units-100)*50)

    print("Bill amount for this customer=",bill)

    customer=customer+1
    amount=amount+bill

print("Total number of customers=",customer)
print("Total amount collected",amount)

if customer>0:
    avg=amount/customer
    print("Average bill amount=",avg)
