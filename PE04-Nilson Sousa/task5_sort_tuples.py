# Given list of tuples
data = [('452', 10), ('256', 5), ('100', 20), ('135', 15)]

# Sort the tuples by the second item of each tuple
sorted_data = sorted(data, key=lambda item: item[1])

print(sorted_data)
