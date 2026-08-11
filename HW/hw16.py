#check a number is a prime number or not

num=int(input("Enter number"))
i=2
fact=0

while i<=num:
    if num%i==0:
        fact=fact+1
    i=i+1

if fact>=2:
    print("Not a prime number")
else:
    print("Prime number")
