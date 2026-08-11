#find even and odd numbers

even_count=0
odd_count=0
i=1

while i<=5:
    num=int(input(f"Enter number{i}"))
    if i%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
    i=i+1
    
print("Count of even numbers=",even_count)
print("Count of odd numbers=",odd_count)

