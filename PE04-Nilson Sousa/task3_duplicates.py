# Given list of integers with duplicate elements
numbers = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

# Build a new list containing only the values that appear more than once,
# keeping just one copy of each duplicate and preserving first-seen order
output_list = []
for number in numbers:
    if numbers.count(number) > 1 and number not in output_list:
        output_list.append(number)

print("output_list =", output_list)
