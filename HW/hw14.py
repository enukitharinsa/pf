#find the maximum of 5 numbers

Max=int(input("Enter number"))
i=2

while i<=5:
    num=int(input("Enter number"))
    if num>Max:
        Max=num
    i=i+1

print("Maximum number=",Max)
