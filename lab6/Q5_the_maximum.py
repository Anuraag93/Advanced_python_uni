def max2(a, b):
    if a > b: return a 
    else: return b

def max3(a, b, c):
    m = 0
    if a > b: m = a 
    else: m = b

    if c > m:
        m = c
    
    return m


print(max2(1,2))
print(max3(1,2, 4))
