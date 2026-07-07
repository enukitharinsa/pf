adult_tickets=int(input("Enter number of adult tickets"))
child_tickets=int(input("Enter number of child tickets"))
adult_per_prices=float(input("Enter adult ticket price"))
child_per_prices=float(input("Enter child ticket price"))
snack_cost=float(input("Enter snack package cost"))

adult_prices=adult_tickets*adult_per_prices
child_prices=child_tickets*child_per_prices
total_payment=adult_prices+child_prices+snack_cost

print("Adult tickets prices=",adult_prices)
print("Child tickets prices=",child_prices)
print("Snack package cost=", snack_cost)
print("Total ticket payment=",total_payment)
