original = [8, 20, -10, 55, -777]

# Loop through the list by index and replace any negative value with its absolute value
for i in range(len(original)):
    if original[i] < 0:
        original[i] = abs(original[i])

print("Modified list:", original)
