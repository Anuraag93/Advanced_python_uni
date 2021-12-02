# Q6
# Without creating extra lists

a = [1, 2, 3, 4, -5, 6, 7, -8, 9]

"""
marker = 0  # 'marker' tells where to put an even number
            # as we move it to the front

for each index i:
    if a[i] is even:
        inser  it at 'marker' position
        remove it from the lis, using method pop
        increment 'marker'
"""      

N = len(a)

marker = 0
for i in range(N):
    if a[i] % 2 == 0:
        value = a.pop(i)
        a.insert(marker, value)
        marker += 1

print(a)
