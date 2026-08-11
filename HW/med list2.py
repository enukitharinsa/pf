med_code=["MED001","MED002","MED003","MED004","MED005","MED006","MED007","MED008","MED009","MED010"]
med_name=["Paracetamol","Vitamin c","Cough Syrup","Antacid","Pain Relief Gel","Face Mask Pack","Hand Sanitizer","Bandage Roll","Antibiotic Cream","Digital Thermometer"]
med_price=[120,450,780,350,920,180,520,250,680,2150]

print(f"{'Medicine Code':<20}{'Medicine Name':<30}{'Price':<20}")
print("-"*55)

for i in range(10):
    print(f"{med_code[i]:<20}{med_name[i]:<30}{med_price[i]:<20}")

code=input("Medicine Code?")
qty=int(input("Enter Quantity?"))
count=0

while count<10:
    if med_code[count]==code:
        tot=med_price[count]*qty
    count=count+1

print("Total bill is",tot)


con=int(input("Enter 1 for next item OR Enter 0 to Exit !"))
tot=0

while con!=0:
    code=input("Medicine Code?")
    qty=int(input("Enter Quantity?"))
    count=0
    while count<10:
        if med_code[count]==code:
            tot=tot+(med_price[count]*qty)
        count=count+1
    con=int(input("Enter 1 for next item OR Enter 0 to Exit !"))

print("Total bill is",tot)
                     
        


    

