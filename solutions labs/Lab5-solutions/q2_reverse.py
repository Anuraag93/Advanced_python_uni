# Q2
# Reverse a list
# Use an extra list (option 1)

"""
Create second list b
for i from N-1 to 0:
    append a[i] to b
"""

a = [0, 1, 2, 3, 4, 5, 6, 7]

N = len(a)

b = []
for i in range(N - 1, - 1, -1):
    b.append(a[i])

for i in range(0, N):
    a[i] = b[i]

print(a)

