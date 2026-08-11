#addition of first 10 odd numbers

i=1
add=0

while i<=10:
    if i%2==1:
        add=add+i
    i=i+1

print("Addition=",add)
