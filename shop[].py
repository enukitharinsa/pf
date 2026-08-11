code=["ITM001","ITM002","ITM003","ITM004","ITM005"]
name=["eggs","tea","bite","soap","shampoo"]
price=[520,780,650,950,220]

print(f"{'ITEM CODE':<20}{'ITEM NAME':<20}{'ITEM PRICE':<20}")
print("-"*50)

for i in range(5):
    print(f"{code[i]:<20}{name[i]:<20}{price[i]:<20}")
    
#to store bill details
itemcode=[]
itemname=[]
quantity=[]
unitprice=[]
totalprice=[]

con=1
total=0

#loop to get multiple item
while con!=0:
    item_code=input("Item code?")
    qty=int(input("Qantity?"))

    i=0

    while i<=4:
        if code[i]==item_code:
            u_price=price[i]
            tot=u_price*qty
            total=total+tot

            #append item details to the bill
            itemcode.append(code[i])
            itemname.append(name[i])
            quantity.append(qty)
            unitprice.append(u_price)
            totalprice.append(tot)
            
        i=i+1

    con=int(input("Enter 1 for next item OR Enter 0 for exit!"))
    
#disply the final bill
print(f"{'item code':<20}{'item name':<20}{'quantity':<20}{'unit price':<20}{'total price':<20}")
print("-"*95)

for i in range(len(itemcode)):
    print(f"{itemcode[i]:<20}{itemname[i]:<20}{quantity[i]:<20}{unitprice[i]:<20}{totalprice[i]:<20}")
    
print("_"*95)
print("Total bill=",total)

