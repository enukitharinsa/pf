#input nalues into a list

numbers=[]

for i in range(5):
    num=int(input(f"Enter {i+1} numbetr:"))
    numbers.append(num)
    
print(numbers)

total=sum(numbers)

avg=total/5

print(f"Total:{total}")
print(f"Average:{avg}")
