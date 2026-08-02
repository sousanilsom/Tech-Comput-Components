def first(n):
    return n[0]

def sort_list_first(tuples):
    return sorted(tuples, key=first)

print(sort_list_first([(5, 2), (2, 1), (4, 4), (3, 2), (1, 2)]))

# Experiment 1: change first() to "return n[1]" -> the list sorts by the
# SECOND element of each tuple instead of the first, e.g.:
# [(2, 1), (5, 2), (3, 2), (1, 2), (4, 4)]

# Experiment 2: with first() still returning n[1], add a one-element tuple
# to the list, e.g. sort_list_first([(5, 2), (2, 1), (6,)]).
# This raises "IndexError: tuple index out of range" because (6,) has no
# index 1. Asking an AI chat agent about this error correctly points to
# the missing second element as the cause, but always verify the fix
# rather than accepting a full rewrite.
