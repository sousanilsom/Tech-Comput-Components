# List of at least three people I'd like to invite to dinner
dinner_guests = ["Maria", "John", "Aisha"]

# Print the original guest list
print("Dinner guest list:", dinner_guests)

# One guest (John) can't make it, so replace him with a new guest (Carlos)
dinner_guests[1] = "Carlos"
print("Updated guest list:", dinner_guests)

# Use insert() to add a new guest to the beginning of the list
dinner_guests.insert(0, "Sofia")

# Use insert() to add a new guest to the middle of the list
middle_index = len(dinner_guests) // 2
dinner_guests.insert(middle_index, "Diego")

# Use append() to add a new guest to the end of the list
dinner_guests.append("Priya")

# Print the new list after all additions
print("Final guest list:", dinner_guests)

# Use pop() to remove guests one at a time until only two names remain,
# sending each removed guest an apology message
while len(dinner_guests) > 2:
    removed_guest = dinner_guests.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner.")

# Print who is left on the final list
print("Remaining guests:", dinner_guests)
