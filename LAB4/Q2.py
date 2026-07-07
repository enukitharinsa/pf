correct_pin=1234
balance=20000

entered_pin=int(input("Enter your PIN"))
if entered_pin==correct_pin:
    amount=float(input("Enter withdrawal amount"))
    if amount<=balance:
        balance=balance-amount
        print("Withdrawal successful")
        print("Remain balance:Rs.",balance)
    else:
        print("Insufficient balance")
else:
    print("Incorrect PIN")
