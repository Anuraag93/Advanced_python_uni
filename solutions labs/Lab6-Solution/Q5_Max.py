# Q5


# Part A

# version 1 - multiple return statements
def max2(x1, x2):
    if x1 >= x2:
        return x1
    else:
        return x2

# test cases
print(max2(2, 4))
print(max2(4, 2))
print(max2(4, 4))
print()

# version 2 - one return statement
def max2(x1, x2):
    if x1 >= x2:
        bigger = x1
    else:
        bigger = x2
    return bigger

# test cases
print(max2(2, 4))
print(max2(4, 2))
print(max2(4, 4))
print()


# Part B

def max3(x1, x2, x3):
    bigger = max2(x1, x2)
    biggest = max2(bigger, x3)
    return biggest

print(max3(2, 4, 6))
print(max3(2, 6, 4))
print(max3(6, 2, 4))
print()

def max3(x1, x2, x3):
    return max2(x3, max(x1, x2))

print(max3(2, 4, 6))
print(max3(2, 6, 4))
print(max3(6, 2, 4))
print()   
