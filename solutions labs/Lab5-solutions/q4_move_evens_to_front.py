# Q6
# With extra lists

a = [1, 2, 3, 4, -5, 6, 7, -8, 9]

N = len(a)
b1 = []  # to store even numbers
b2 = []  # to store odd numbers

for n in a:
    if n % 2 == 0:
        b1.append(n)
    else:
        b2.append(n)

b3 = b1 + b2

for i in range(N):
    a[i] = b3[i]
    
print(a)

