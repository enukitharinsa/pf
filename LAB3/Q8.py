num1=int(input("Enter number 1"))
num2=int(input("Enter number 2"))
num3=int(input("Enter number 3"))

if num1>num2 and num1>num3:
    print("Largest number=",num1)
elif num2>num1 and num2>num3:
    print("Largest number=",num2)
else:
    print("Largest number=",num3)
