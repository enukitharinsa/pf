hall_rental=float(input("Enter hall rental cost"))
deco_cost=float(input("Enter decoration cost"))
food_cost_per=float(input("Enter food cost for per person"))
guests=int(input("Enter nuber of guests"))
sound_rental=float(input("Enter sound system rental cost"))

food_cost=food_cost_per*guests
total_budget=hall_rental+deco_cost+food_cost+sound_rental

print("Total Event Budget:",total_budget)
