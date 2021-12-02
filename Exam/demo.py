# row = int(input('Enter number of rows required: '))
row = 5

for i in range(row,0,-1):
    for j in range(row-i):
        print(' ', end='') # printing space and staying in same line
    
    for j in range(i):
        print('* ',end='') # printing * and staying in same line
    print() # printing new line
