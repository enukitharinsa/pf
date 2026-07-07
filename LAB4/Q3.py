marks=float(input("Enter student marks"))

if marks>=75:
    income=float(input("Enter your family income"))
    if income<50000:
        print("Scholarship is approved")
    else:
        print("Scholarship is rejected")
else:
    print("Scholarship is rejected")
