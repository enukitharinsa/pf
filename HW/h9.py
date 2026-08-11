#job interview eligibility system

wri_mark=float(input("Enter your candidate's written test mark"))

if wri_mark>=60:
    int_mark=float(input("Enter your interview mark"))

    if int_mark>=50:
        print("Selected")

    else:
        print("Rejected due to interview")

else:
    print("Rejected")
