p_id=[]
name=[]
price=[]
i=0

while i<=3:
    pid=input(f"enter product id {i}")
    p_id.append(pid)
    pname=input(f"enter product name {i}")
    name.append(pname)
    pprice=int(input(f"enter price {i}"))
    price.append(pprice)
    i=i+1

print(f"{'P_ID':<15}{'NAME':<15}{'PRICE':<15}")
print("-"*35)

for i in range(4):
    print(f"{p_id[i]:<15}{name[i]:<15}{price[i]:<15}")

