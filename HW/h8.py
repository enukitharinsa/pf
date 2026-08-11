#cinema ticket discount system

no_tickets=int(input("Enter the number of movie tickets"))

total=no_tickets*800
discount=0

if no_tickets>5:
    card=input("Do you have a loyalty card?(yes/no)")

    if card=="yes":
        discount=total*0.2

    else:
        discount=total*0.1

final=total-discount

print("Total ticket cost=",total)
print("Discount amount=",discount)
print("Final amount to pay=",final)

    
        


    
