# Q2

# define function
def printRepeat(msg, n):
    for i in range(n):
        print(msg)

# A - positional arguments
printRepeat("Hello", 4)
print()

# B - keyword arguments
printRepeat(n = 4, msg = "Hello")
print()

# C - mixed
printRepeat("Hello", n = 4)
print()

# illegal
# printRepeat(n = 4, "Hello")
