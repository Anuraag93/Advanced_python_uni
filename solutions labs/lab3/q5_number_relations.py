# Q5

# Reads 3 numbers, prints "all the same",
# "all different", or "neither"

n1, n2, n3 = 10, 10, 10
n1, n2, n3 = 10, 20, 30
n1, n2, n3 = 10, 20, 10

print(n1, n2, n3)

if n1 == n2 and n2 == n3:
    print("all the same")
    
elif n1 != n2 and n1 != n3 and n2 != n3:
    print("all different")
    
else:
    print("neither")
