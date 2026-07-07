data_usage=float(input("Enter data usage in GB"))
cost_per=float(input("Enter cost per GB"))
additional_charges=float(input("Enter additional service charges"))

data_cost=data_usage*cost_per
final_bill=data_cost+additional_charges

print("Data Cost =",data_cost)
print("Additional Charges =",additional_charges)
print("Final Bill =",final_bill)
