# Q6

# The definition is a straight forward implementation
# of the algorithm given in the handout
L = [-5, 2, -3, 1, 8, 7]
N = len(L)
for x in range(N-1):
    for i in range(0, N-1):
        if L[i] > L[i+1]:
            L[i], L[i+1] = L[i+1], L[i]


print(L)

