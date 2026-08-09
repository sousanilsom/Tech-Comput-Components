# Using the set() constructor and joining two sets

fruits_a = set(["apple", "banana", "cherry"])
fruits_b = {"cherry", "date", "elderberry"}

combined_union = fruits_a.union(fruits_b)
print("Union:", combined_union)

fruits_a.update(fruits_b)
print("After update:", fruits_a)
