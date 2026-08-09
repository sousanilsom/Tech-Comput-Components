# Dictionary example: access, update, add, and delete key-value pairs

student = {"name": "Alice", "age": 21, "major": "Computer Science"}

# Accessing a value
print("Name:", student["name"])

# Updating a value
student["age"] = 22
print("Updated age:", student["age"])

# Adding a new key-value pair
student["gpa"] = 3.8
print("After adding gpa:", student)

# Deleting a key-value pair
del student["major"]
print("After deleting major:", student)
