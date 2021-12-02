# Sieve of Eratoshenes
# To list prime numbers from 2 to some number N

# Suppose we take this test value for N
N = 1000

L = list(range(2, N + 1))

for n in range(2, int(N**0.5)):
    for e in L:
        if e > n and e % n == 0:
            L.remove(e)
    # print(L)

print(L)

"""
Remark:
Simple algorithm
But performs well
"""
