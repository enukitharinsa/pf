#library fine checking system

small_fines=0
large_fines=0

while True:
    late_days=int(input("Enter the number of late days for library books(-1 to stop)"))

    if late_days==-1:
        break

    if late_days<=7:
        print("Small fine")
        small_fines=small_fines+1

    else:
        print("Large fine")
        large_fines=large_fines+1

total=small_fines+large_fines
print("Number of books with small fines:",small_fines)
print("Number of books with large fines:",large_fines)
print("Total number of books checked:",total)




    


