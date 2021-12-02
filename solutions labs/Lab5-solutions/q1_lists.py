# Q1

# A
"""
i.  Create list of even integers from 2 to 100
    Use functions range and list
"""
a = list(range(2, 100 + 1))

"""
ii. Create list of one hundred zeroes
    Use * operator
"""
a = [0] * 100

# B
"""
append: add element to the end of the list
insert: insert element to a particular position
"""

# C
"""
remove: remove the specified element
pop:    remove element at specified index
both can raise exception
"""

# D
"""
Print all even numbers of a list L
for e in L
    print(e)
Do not need to use indexes
"""

# E
"""
Double each element of a list
"""
# This will NOT work:
L = [1, 2, 3, 4]
for e in L:
    e = e * 2

# Must use this:
for i in range(0, len(L)):
    L[i] = L[i] * 2


# F
"""
index: get the first index of the specified element
count: count number of occurrences of the element
in   : determine if the element is in the list
"""

# G
"""
Sort list by absolute value
"""
a = [4, 3, 1, 2, -1, -2]
a.sort(key = abs)

