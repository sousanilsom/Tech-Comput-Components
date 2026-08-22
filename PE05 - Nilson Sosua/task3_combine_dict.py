# Task 3: Combine two dictionaries, adding the values for keys that appear in both

from collections import Counter

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Counter objects support addition, which sums values for matching keys
# and keeps keys that only exist in one dictionary
combined = Counter(d1) + Counter(d2)

print(combined)
