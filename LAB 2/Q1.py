room_charge=float(input("Enter room charge per day:"))
number_of_days=int(input("Enter number of days:"))
food_charges=float(input("Enter food charges:"))
service_percentage=float(input("Enter service charge percentage:"))

subtotal=(room_charge*number_of_days)+ food_charges
service_charge=subtotal*(service_percentage/100)
final_bill=subtotal+service_charge

print("Subtotal=",subtotal)
print("Service Charge=",service_charge)
print("Final Bill=",final_bill)
