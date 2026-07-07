monthly_fee=float(input("Enter monthly fee"))
months=int(input("Enter number of month"))
registration_fee=float(input("Enter registration fee"))
trainer_fee=float(input("Enter personal trainer fee"))
tax_rate=float(input("Enter tax percentage"))

membership_cost=monthly_fee*months
total_before_tax=membership_cost+registration_fee+trainer_fee
tax=(tax_rate/100)*total_before_tax
final_payment=total_before_tax+tax

print("Total Before Tax", total_before_tax)
print("Tax", tax)
print("Final Payment", final_payment)
