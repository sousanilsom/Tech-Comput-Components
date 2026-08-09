# Compare a list and a dictionary that hold the same values in a different order

list_a = [1, 2, 3]
list_b = [3, 2, 1]

dict_a = {"x": 1, "y": 2, "z": 3}
dict_b = {"z": 3, "y": 2, "x": 1}

print(list_a == list_b)
print(dict_a == dict_b)
