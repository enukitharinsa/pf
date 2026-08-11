#student name list

names=[]

for i in range(5):
    name=input(f"Enter {i+1} student name")
    names.append(name)

print(names)

#print element one by one

for name in names:
    print(name)

#print with position using enumerate

for index,name in enumerate(names,start=1):
    print(index,name)
