# Task 1: Concatenate three dictionaries into a new dictionary

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Use dictionary unpacking (**) to merge all three dictionaries
new_dict = {**dic1, **dic2, **dic3}

print(new_dict)
