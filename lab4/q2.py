length = 6


for i in range(length):
    for j in range(length):
        if i == j:
            print(end = 'X ')
        else:
            print(end = f'{i+1} ')
    print()
