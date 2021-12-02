# Q2

#A
"""
tuple of 2 elements
"""
t1 = (1, 2)

"""
tuple of 1 element
"""
t2 = (1, )

"""
empty tuple
"""
t3 = ()
t4 = tuple()


# B
t1 = (1, 2, 3, 4, 5)

t2 = tuple( list(t1) + [6, 7] )

print(t2)

# C
date = (25, 4, 2020)
month = date[1]
print(month)

"""
get day, month, year
"""

dd, mm, yy = date
print(dd, mm, yy)


# D
"""
Cannot use append to add an element to a tuple
Tuples are immutable
"""
