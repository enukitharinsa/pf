cement_bag=int(input("Enter count of cement bag"))
price_per_bag=float(input("Enter price per bag"))
sand_cost=float(input("Enter sand cost"))
labor_cost=float(input("Enter labor cost"))
trans_cost=float(input("Enter transportation cost"))

cement_bag_price=cement_bag*price_per_bag
full_cost=cement_bag_price+sand_cost+labor_cost+trans_cost

print("Construction cost:",full_cost)
