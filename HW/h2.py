ep=float(input("Enter emplooyees performance score"))

if ep>=85:
    years=int(input("Enter years of service"))

    if years>=3:
        print("Promotion approved")
    else:
        print("More experience requied")

else:
    print("performance improvement required")
