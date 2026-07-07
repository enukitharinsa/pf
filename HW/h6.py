balance=10000
total=0
count=0

while balance>0:
    reload=float(input("Enter reload amount(or -1 to stop)"))

    if reload==-1:
        break

    if reload<=balance:
        balance=balance-reload
        total=total+reload
        count=count+1

    else:
        print("Not enough to balance")
        
print("Remaining balance=",balance)
print("Total reload amount=",total)
print("Number of successful reloads=",count)

    

    
