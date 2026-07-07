weight=float(input("Enter your baggage weight"))

if weight<=20:
    print("No extra charge")
elif weight<=30:
    extra_kg=weight-20
    charge=extra_kg*200
    print("Extra charge:Rs",charge)
else:
    print("Baggage is not allowed")
