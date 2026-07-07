price1=float(input("Enter price of product 1"))
qty1=int(input("Enter quatity of product 1"))

price2=float(input("Enter price of product 2"))
qty2=int(input("Enter quatity of product 2"))

price3=float(input("Enter price of product 3"))
qty3=int(input("Enter quatity of product 3"))

dilivery_charge=float(input("Enter dilivery charge"))
discount_percent=float(input("Enter discount percentage"))

tot1=price1*qty1
tot2=price2*qty2
tot3=price3*qty3

subtotal=tot1+tot2+tot3
discount=(discount_percent/100)*subtotal
final_total=subtotal-discount_percent+dilivery_charge

print("Subtotal",subtotal)
print("Discount",discount)
print("Final Total",final_total)


