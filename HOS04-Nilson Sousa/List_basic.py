# Create list1 containing mixed data types (strings and integers)
list1 = ['physics', 'chemistry', 1997, 2000]
# Create list2 containing a sequence of integers
list2 = [1, 2, 3, 4, 5]

# Access the first item in list1 using index 0
print("list1[0] : ", list1[0])
# Access a slice of list2 from index 1 up to (not including) index 5
print("list2[1:5] : ", list2[1:5])

# Print list2 before updating a value, to compare later
print(f"Value before update: {list2}")
# Update the value at index 2 of list2 from 3 to 10
list2[2] = 10
# Print list2 after the update to confirm the change
print(f"Value after update: {list2}")

# Add a new item (2020) to the end of list1
list1.append(2020)
# Print list1 to show the appended value
print("New list:", list1)

# Insert 'Python' at index 0, shifting all other items to the right
list1.insert(0, 'Python')
# Print list1 to show the item inserted at the beginning
print("After inserting: ", list1)
