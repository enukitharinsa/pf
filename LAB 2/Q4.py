basic_salary=float(input("Enter basic salary"))
overtime_hours=int(input("Enter overtime hours"))
overtime_rate=float(input("Enter overtime rate per hour"))
bonus=float(input("Enter bonus amount"))
tax_percentage=float(input("Enter tax percentage"))

overtime_pay=overtime_hours*overtime_rate
gross_salary=overtime_pay+basic_salary+bonus
tax_amount=(gross_salary*tax_percentage)/100
net_salary=gross_salary-tax_amount

print("Gross Salary", gross_salary)
print("Tax Amount", tax_amount)
print("Net Salary", net_salary)
