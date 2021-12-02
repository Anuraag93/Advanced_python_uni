

a = [0, 1, 2, 3, 4, 5, 6, 7]

N = len(a)

for i in range(0, N // 2):
    
    # swap these
    a[i], a[N-i-1] = a[N-i-1], a[i]

print(a)

