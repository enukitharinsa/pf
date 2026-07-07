total=0
eligible=0
not_eligible=0
i=1

while i<=10:
    att_percentage=float(input("Enter your attendance percentage"))

    total=total+att_percentage

    if att_percentage>=75:
        eligible=eligible+1
    else:
        not_eligible=not_eligible+1

    i=i+1

average=total/10

print("Eligible students=",eligible)
print("Not_eligible students=",not_eligible)
print("Average=",average)


        
