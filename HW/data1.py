p_id=[]
name=[]
price=[]
i=0

while i<2:
    pid=input(f"Enter product {i} ID")
    p_id.append(pid)

    pname=input(f"Enter product {i} name")
    name.append(pname)

    pprice=float(input(f"Enter product {i} price"))
    price.append(pprice)

    i=i+1

print(f"{'PRODUCT ID':<15}{'PRODUCT NAME':<15}{'PRICE':<15}")
print("-"*50)

for i in range(2):
    print(f"{p_id[i]:<15}{name[i]:<15}{price[i]:<15}")

