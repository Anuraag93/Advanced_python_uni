from math import sqrt

N = 100
num_lst = list(range(2,N))
print(num_lst)
multi = 2
while multi < sqrt(N):
    for num in num_lst:
        if num != multi and num%multi == 0:
            num_lst.remove(num)
    print(multi)
    print(num_lst)
    multi += 1

print("prime numbers")
print(num_lst)