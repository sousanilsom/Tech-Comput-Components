# Tuple of five foods offered by the buffet-style restaurant
foods = ("rice", "salad", "chicken", "pasta", "soup")

# Use a for loop to print each food the restaurant offers
for food in foods:
    print(food)

# Try to modify one of the items; Python rejects changes to tuples
try:
    foods[0] = "pizza"
except TypeError as error:
    print("Error:", error)

# The restaurant changes its menu, replacing two items with different foods.
# Tuples can't be modified in place, so we rewrite the whole tuple.
foods = ("pizza", "salad", "chicken", "sushi", "soup")

# Use a for loop to print each item on the revised menu
for food in foods:
    print(food)
