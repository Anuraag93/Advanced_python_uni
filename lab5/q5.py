
a = [1, 2, 3, 4, -5, 6, 7, -8, 9]

N = len(a)

marker = 0
for i in range(N):
    if a[i] % 2 == 0:
        value = a.pop(i)
        a.insert(marker, value)
        marker += 1

print(a)
