# Q8
# Reads a +ve intger, count its digits
# Shows "has 1 digit", ..., "has 4 digits", "has more than 4 digits"

n = 1
n = 12
n = 123
n = 1234
n = 123456

# n = -123 # invalid input

print(n)
if n < 10:
    print("has 1 digit")
    
elif n < 100:
    print("has 2 digits")
    
elif n < 1000:
    print("has 3 digits")
    
elif n < 10_000:
    print("has 4 digits")
    
else:
    print("has more than 4 digits")
