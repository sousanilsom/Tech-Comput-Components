# Using del to remove an item by its index
motorcycle = ['Honda', 'yamaha', 'suzuki']
del motorcycle[1]
print(motorcycle)

# Using pop() to remove and return an item so it can still be used
motorcycles = ['Honda', 'Yamaha', 'Suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
first_owned = motorcycles.pop(0)
print("The first owned motorcycle is a", first_owned)

# Using remove() to delete an item by its value
motorcycles = ['Honda', 'Yamaha', 'Suzuki']
motorcycles.remove('Suzuki')
print(motorcycles)
