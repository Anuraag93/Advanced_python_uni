# x = input("Enter a string ")
x= 'beautiful'
x= 'beauty'
print(x[0],x[-1])
l = len(x)
print(int(l/2))
if(l %2 != 0):
    print(x[round(l/2)])
else:
    print(x[int((l/2)-1)],x[int(l/2)])