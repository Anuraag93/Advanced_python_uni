# Q11 - Sets

# A
"""
- Set of 2 elements, 1 element, 0 elements
"""
s1 = {10, 20}
s2 = {10}
s3 = set()          # not {}, which is an empty dictionary

# B
"""
Given list L, get the list with duplicates removed
"""
L = { 1, 2, 3, 4, 3, 4, 5, 6}
list(set(L))

# C
"""
Method to add an element, remove an element, to
check if an element is in a set are:

    add
    remove
    in
"""

# D
"""
Construct union, intersection and difference of sets S1 and S2
"""
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))

