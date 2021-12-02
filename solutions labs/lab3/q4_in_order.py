# Q4

# Reads 3 numbers, prints "stricly increasing",
# "stricly deceasing", "neither"

n1, n2, n3 = 10, 20, 30
n1, n2, n3 = 30, 20, 10
n1, n2, n3 = 10, 30, 20
n1, n2, n3 = 10, 20, 20

print(n1, n2, n3)

if n1 < n2 and n2 < n3:
    print("strictly increasing")
    
elif n1 > n2 and n2 > n3:
    print("strictly decreasing")
else:
    print("neither")
