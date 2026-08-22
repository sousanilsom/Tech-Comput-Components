# Task 2: Generate a dictionary containing numbers 1 to n mapped to their squares

n = 5
square_dict = {}

# Loop through numbers 1 to n and store each number with its square as (x, x*x)
for x in range(1, n + 1):
    square_dict[x] = x * x

print(square_dict)
