#display a square of star

i=1
while i<=4:
    j=1
    while j<=4:
        print("*",end=" ")
        j=j+1
    print()
    i=i+1

#display a triangle of stars

i=1
while i<=4:
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    print()
    i=i+1

#revers triangle star pattern

i=5
while i>=1:
    j=1
    while j<=i:
        print("*", end=" ")
        j=j+1
    print()
    i=i-1 