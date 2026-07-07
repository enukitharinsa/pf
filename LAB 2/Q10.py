loan_amount=float(input("Enter loan amount"))
interest_rate=float(input("Enter annual interest rate"))
repayment_period=int(input("Enter repayment period in months"))

years=repayment_period/12
total_interest=loan_amount*(interest_rate/100)*years
final_payment=loan_amount+total_interest
monthly_installment=final_payment/repayment_period

print("Toatl Interest=",total_interest)
print("Final Payment=",final_payment)
print("Monthly Installment=",monthly_installment)
