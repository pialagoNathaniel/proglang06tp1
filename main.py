# Pialago, Nathaniel Christian M.
# BSCS 601

# Ask the user for estimated costs
venue = float(input("Enter the cost for Venue: "))
catering = float(input("Enter the cost for Catering: "))
decorations = float(input("Enter the cost for Decorations: "))
entertainment = float(input("Enter the cost for Entertainment: "))
miscellaneous = float(input("Enter the cost for Miscellaneous: "))

# Calculate total estimated cost
total_cost = 0
total_cost += venue
total_cost += catering
total_cost += decorations
total_cost += entertainment
total_cost += miscellaneous

#  Define a pre-defined budget
budget = 1000  # You can change this

# Print the total estimated cost
print("\nTotal Estimated Cost: $", total_cost)

#  Check if the cost is within the budget
if total_cost <= budget:
    print("The total cost is within the budget.")
else:
    print("Warning: The total cost exceeds the budget.")