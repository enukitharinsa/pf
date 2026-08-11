model=[]
storage=[]
price=[]
i=0

while i<=4:
    pmodel=input(f"Enter phone model {i}")
    model.append(pmodel)

    pstorage=input(f"Enter storage {i}")
    storage.append(pstorage)

    pprice=float(input(f"Enter price {i}"))
    price.append(pprice)

    i=i+1

print(f"{'MODEL':<15}{'STORAGE':<15}{'PRICE':<15}")
print("-"*50)

for i in range (5):
    print(f"{model[i]:<15}{storage[i]:<15}{price[i]:<15}")
