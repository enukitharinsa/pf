wattage=float(input("Enter appliance wattage"))
hours_per_day=float(input("Enter hours used per day"))
cost_per_kwh=float(input("Enter cost per kWH"))

daily_kwh=(wattage*hours_per_day)/1000
total_kwh=daily_kwh*30
final_bill=total_kwh*cost_per_kwh

print("Total power consumption=",total_kwh)
print("Final Bill=",final_bill)
