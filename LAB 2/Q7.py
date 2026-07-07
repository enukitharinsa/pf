module=int(input("Enter number of modules"))
fee_per_module=float(input("Enter fee for per module"))
library_fee=float(input("Enter library fee"))
registration_fee=float(input("Enter registration fee"))

module_fee=module*fee_per_module
full_payment=module_fee+library_fee+registration_fee

print("Full Payment",full_payment)
