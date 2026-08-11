#average of 5 values given by users

i=1
tot=0

while i<=5:
    num=int(input(f"Enter number {i}"))
    tot=tot+num
    i=i+1

avg=tot/5

print("Average=",avg)
