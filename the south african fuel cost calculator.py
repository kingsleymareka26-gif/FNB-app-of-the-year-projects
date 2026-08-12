# Get user input 
kilometers = float(input("How many kilometers do you want to drive? "))
petrol_price = float(input("Enter the current petrol price per liter (in ZAR): "))

# Calculate liters needed (1 liter per 10 kilometers)
liters_needed = kilometers / 10

# Calculate total cost
total_cost = liters_needed * petrol_price

# Round to 2 decimal places
total_cost = round(total_cost, 2)

# Display the result
print(f"To drive {kilometers} km, you will need {round(liters_needed, 2)} liters of petrol.")
print(f"The total cost of petrol will be: ZAR {total_cost}")