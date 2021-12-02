N = 100
num_list = list(range(N))
print(num_list)
for _ in range(N):
    for i in range(N-1):
        if num_list[i] <num_list[i+1]:
            num_list[i], num_list[i+1] = num_list[i+1], num_list[i]

print(num_list)