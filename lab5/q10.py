f = (2,1,1)
fib = [f]
N = 20

for i in range(N):
    n1 = fib[i][2]
    n2 = fib[i][0]

    fib.append((n1+n2, n1, n2))

print(len(fib))
print(fib)