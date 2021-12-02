# Q10

for n in range(1, 20 + 1):
    if n == 1: 
        print (1, end = " ") 
        continue
    if n == 2: 
        print (",",1, end = " ")
        continue
    # for n >= 3

    f = (2, 1, 1)
    for time in range(3, n + 1):
        f = (f[0] +1, f[2], f[1] + f[2])
    print(",", f[2], end = " ")