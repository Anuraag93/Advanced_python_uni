# Q12 - Dictionaries

# example
d = {1:"dog", 2:"cat"}


# A
"""
Create dictionary with 2 elements, 1 element and 0 elements
"""
d1 = {1: "dog", 2: "cat"}
d2 = {1: "dog"}
d3 = {}
# or dict()


# B
"""
ADD a pair to a dictionary
"""
d[3] = "bird"


# C
"""
CHANGE the value of a key
"""
d[2] = "fish"

# D
"""
REMOVE a pair
"""
d.pop(2)


# E
"""
GET the value of a key
"""
d[1]

# F
"""
GET ALL the keys, values, pairs
"""
d.keys()
d.values()
d.items()

# G
"""
iterate over a dictionary
"""


"""
iterate over the keys
"""
for x in d:
    print(x)

"""
equivalent loop
"""
for x in d.keys():
    print(x)

"""
iterate over values
"""
for x in d.values():
    print(x)

"""
iterate over key-value pairs
"""
for x in d.items():
    print(x)

