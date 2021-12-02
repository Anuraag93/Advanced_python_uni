# Q3

# Reads three numbers, prints them out in order

# a sample of test cases
n1, n2, n3 = 30, 10, 20
n1, n2, n3 = 10, 30, 20
n1, n2, n3 = 20, 10, 30
n1, n2, n3 = 10, 20, 30
n1, n2, n3 = 10, 20, 30
n1, n2, n3 = 20, 10, 20

# display original order
print(n1, n2, n3)

# put the min of n1, n2 in n1
if n1 > n2:
    n1, n2 = n2, n1
    # at this stage, n1 is min of n1, n2

# put the min of n1, n3 in n1
if n1 > n3:
    n1, n3 = n3, n1
    # at this stage, n1 is min of n1, n2, n3

# put min of n2, n3 in n2
if n2 > n3:
    n2, n3 = n3, n2
    # at this stage, n2 is min of n2, n3
    # Hence 1, n2, n3 are in increasing order

# display increasing order
print(n1, n2, n3)

"""
One way to understand the solution clearly:
Trace the execution
"""




