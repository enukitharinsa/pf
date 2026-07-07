units=int(input("Enter number of units"))

if units<=30:
    charge=units*20

elif units<=60:
    charge=(30*20)+((units-30)*40)

else:
    charge=(30*20)+(30*40)+((units-60)*60)

print("consumed units=",units)
print("Total bill amount=",charge)
