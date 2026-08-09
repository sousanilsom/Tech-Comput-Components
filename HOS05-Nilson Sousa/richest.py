# Find the richest (and poorest) person from a dictionary of net worths

net_worth = {
    "Stark": 950,
    "Wayne": 700,
    "Banner": 50,
}

richest_person = max(net_worth, key=net_worth.get)
print(f"{richest_person} is the richest, with a net worth of {net_worth[richest_person]}.")

# Modification: find the person with the lowest net worth
poorest_person = min(net_worth, key=net_worth.get)
print(f"{poorest_person} has the lowest net worth, at {net_worth[poorest_person]}.")
