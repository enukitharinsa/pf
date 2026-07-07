distance=float(input("Enter distance travel"))
fuel_efficiency=float(input("Enter fuel efficiency"))
fuel_price=float(input("Enter fuel price per liter"))
highway_charges=float(input("Enter highway charges"))


fuel_used=distance/fuel_efficiency
fuel_cost=fuel_used*fuel_price
final_trip_cost=fuel_cost+highway_charges

print("Fuel Used=",fuel_used)
print("Fuel Cost=",fuel_cost)
print("Final Trip Cost=",final_trip_cost)
