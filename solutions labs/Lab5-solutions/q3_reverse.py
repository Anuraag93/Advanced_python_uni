# Q3
# Reverse a list
# Without creating an extra list

"""
We swap an element with the one opposite at the other end.

For example,
element at index 0 with element at indes N-1,
element at index 1 with element at index N-2, etc.

In general, we swap element at index i with the 'opposite'
one at index N-1-i, as shown in the table below:

index     opposite     expression
0         N-1          N-0-1
1         N-2          N-1-1
2         N-3          N-2-1


i                      N-i-1

N//2
"""

a = [0, 1, 2, 3, 4, 5, 6, 7]

N = len(a)

for i in range(0, N // 2):
    
    # swap these
    a[i], a[N-i-1] = a[N-i-1], a[i]

print(a)

