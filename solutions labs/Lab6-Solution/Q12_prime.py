# Q12

#A

# a simple definition with no optimization

def isPrime(number):
    
    factors = 0
    for n in range(2, number):
        if number % n == 0:
            factors = factors + 1

    return factors == 0
        

# B

# Find the first prime after 50
N = 50

n = N
found = False

while not found:
    n = n + 1
    if isPrime(n):
        found = True

print(n)
