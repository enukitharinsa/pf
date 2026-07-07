pm=input("Are you a premium member(yes/no)")

if pm=="yes":
    pa=float(input("Enter purchase amount"))
    if pa>=10000:
        print("20% discount applied")
    else:
        print("10% discount applied")
else:
    print("no discount available")
