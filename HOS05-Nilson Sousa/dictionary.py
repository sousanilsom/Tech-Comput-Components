y_dict = {"name": "abc", "age": 30}

print(my_dict)

# Updating
my_dict["age"] = 31
print("Updated:", my_dict)

# Adding
my_dict["city"] = "New York"
print("After adding:", my_dict)

# Deleting
del my_dict["age"]
print("After deleting 'age':", my_dict)